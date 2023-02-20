#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
202002816

@author: mohammedsabbagh
"""


import socket
import datetime
import time
import uuid

# get website IP from user input
#get Mac address
mac_address=":".join(['{:02x}'.format((uuid.getnode()>>elements) & 0xff)
                       for elements in range(0,8*6,8)][::-1])
print("Mac address is: ",mac_address)
dest_ip = input("Enter website IP: ")

# send request to proxy server
HOST = 'localhost'  # use localhost or the IP of the proxy server
PORT = 8080  # use the same port as the proxy server
start_time=time.time()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    # create HTTP GET request string
    request_str = f"GET http://{dest_ip}/ HTTP/1.1\r\nHost: {dest_ip}\r\n\r\n"

    # send request to proxy server
    now = datetime.datetime.now()
    client_socket.sendall(request_str.encode('utf-8'))
    print(f"Sent request to proxy server at {now}")

    # receive response from proxy server
    response = b''
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response += data

    # print response and total round-trip time
    now = datetime.datetime.now()
    end_time=time.time()
    print(f"Received response from proxy server at {now}")
    print(response.decode('utf-8'))
    round_trip_time=end_time-start_time
    print("Round time is: ",round_trip_time,"seconds")

    # close connection
    client_socket.close()
