#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:12:37 2022

@author: radhakrishna
"""


import asyncio,json,random


'''

Data simmulation file for testing the stream service implemented in async_reader.py

This simulation has 2 streams with 10 packet data which is shuffled to simulate a 

distrubted processing source

'''

async def tcp_echo_client(list_of_packets):
    
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    
    for packet in list_of_packets:
        print(f'Send: {packet!r}')
        writer.write(json.dumps(packet).encode())
        await writer.drain()
        print('Data Sent')
    
        data = await reader.read(100)






packet_1_1={
    
    "primary_id":1,
    "payload":"Hello my name is",
    "index":1,
    "last_chunk":0
    
    }
packet_1_2={
    
    "primary_id":1,
    "payload":"Radha Krishna",
    "index":2,
    "last_chunk":0
    
    }
packet_1_3={
    
    "primary_id":1,
    "payload":"I am applying for this position",
    "index":3,
    "last_chunk":0
    
    }
packet_1_4={
    
    "primary_id":1,
    "payload":"This is the assignment",
    "index":4,
    "last_chunk":0
    
    }
packet_1_5={
    
    "primary_id":1,
    "payload":"That they have given me",
    "index":5,
    "last_chunk":0
    
    }
packet_1_6={
    
    "primary_id":1,
    "payload":"This is basically",
    "index":6,
    "last_chunk":0
    
    }
packet_1_7={
    
    "primary_id":1,
    "payload":"a real time stream processing routine",
    "index":7,
    "last_chunk":0
    
    }
packet_1_8={
    
    "primary_id":1,
    "payload":"with out of order packets",
    "index":8,
    "last_chunk":0
    
    }
packet_1_9={
    
    "primary_id":1,
    "payload":"this packet is the 9th one",
    "index":9,
    "last_chunk":0
    
    }
packet_1_10={
    
    "primary_id":1,
    "payload":"of all the ten packets present",
    "index":10,
    "last_chunk":1
    
    }
data_packets=[
    packet_1_1,
    packet_1_2,
    packet_1_3,
    packet_1_4,
    packet_1_5,
    packet_1_6,
    packet_1_7,
    packet_1_8,
    packet_1_9,
    packet_1_10,
    ]
for i in range(0,len(data_packets)):
    newpidpacket=data_packets[i].copy()
    newpidpacket["primary_id"]=2
    data_packets.append(newpidpacket)
random.shuffle(data_packets)
asyncio.run(tcp_echo_client(data_packets))