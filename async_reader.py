import asyncio, socket,json
import heapq as hq
from threading import Timer

class StreamService():
    
    def __init__(self):
        self.streams={}
        
        print("Starting Stream Service")
        
    
    def ancillary_service(self,chunk):
        '''
        

        Parameters
        ----------
        chunk : String
            A Piece of data on which some processing has to be done ( String here ).

        Returns
        -------
        Integer
            Returns the out put of the processign ( length of string here ).

        '''
        return len(chunk)
    
    async def handle_client(self,reader, writer):
        '''
        

        Parameters
        ----------
        reader : asyncio reader
            DESCRIPTION.
        writer : asncyio writer
            DESCRIPTION.

        Returns
        -------
        
        -> this handles the incoming data, pusshes the data into priority queues based on the index in the packet.
        -> When we receieve a last chunk for any particular stream, this triggers a thread for submitting the data
        ->  Heapqs are used here to handle the priority , ( min heap in python )
        -> As provided in the details, the minimum amount of time in which we get missing data is 60 seconds, 
        -> So on the last receipt of chunk , we fire submit_results function after 60 seconds so that some data might be missing
        -> This can be avoided if we track each index and have a knowledge of what is the index space
        

        '''
        
        request = None
        while request != 'quit':
            request = (await reader.read(1000)).decode('utf8')
            response = str((request))# + '\n'
            
            response_dict=json.loads(response)
            print(response_dict)
            if(response_dict['primary_id'] not in self.streams):
                self.streams[response_dict['primary_id']]=[]
            hq.heappush(self.streams[response_dict['primary_id']],(response_dict['index'], self.ancillary_service(response_dict['payload'])))
            writer.write(response.encode('utf8'))
            await writer.drain()
            if(response_dict['last_chunk']==1):
                t = Timer(60, self.submit_results,[response_dict['primary_id']])
                t.start()
                
        writer.close()
    
    async def run_server(self,):

        # ASYNCIO SERVER

        
        server = await asyncio.start_server(self.handle_client, 'localhost', 8888)
        async with server:
            await server.serve_forever()
    
    def submit_results(self,pid):
        
        '''
        
        This function is triggered once all the pieces of a stream are received. 
        This is an asynchronous call , because this is anyways running in a seperate thread with no wait!
        
        '''
        
        while(len(self.streams[pid])!=0):
            element=(hq.heappop(self.streams[pid])[1])
            print(element)
        print("Call an asynchronous webhook and send the data as required at this point.")

streamer=StreamService()
asyncio.run(streamer.run_server())
print(streamer.jobs)


