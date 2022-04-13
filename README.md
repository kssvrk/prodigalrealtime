# prodigalrealtime

There are 2 files , which are of importance.

The main processing service lies inside async_reader.py
where as the simulation file lies inside async_test.py

Procedure to run,
1) First run python async_reader.py
2) On succesful run of async_reader.py , run python async_test.py
3) async_test will fire 20 data packets at the reader shuffled and mixed,
4) Once the connection is closed, we get an empty packet decoding error, ignore that for time being
5) Wait for 60 seconds as that is the minimal time to wait for all missing packets to arrive as explained in the code ( CONFIGURABLE, change it to 2 seconds if you dont want to wait )
6) See the sorted packets according to their indexes.

Assumptions:-
1) Packets have complete data ( no packet appending implemented )
2) Assumption that the service will have max connections as that of the file descriptors on the server side ( reasonable , for now ), can be over come through a load balanced proxy redirecting the connections to various inside ips
3) We should not wait for all the data to come before sending it for processing ( one of the design suggestion in the FAQs, because then , the whole asynchronous low latency is out of question. )
4) The architecture of this project is the server receives data as fast as it can and submits this to the ancillary service ( which is just a method in this implementation, but in real life it can be some external service and we can submit jobs to that broker through some redis queues or rabbit mqs or the interface supported by the broker) 
