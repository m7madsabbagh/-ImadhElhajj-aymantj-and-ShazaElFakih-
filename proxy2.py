#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
202002816

@author: mohammedsabbagh
"""

import socket
import datetime

HOST = ''  # listen on all available interfaces
PORT = 8080  # use a port of your choice

def handle_request(client_socket):
    request = client_socket.recv(1024)
    request_str = request.decode('utf-8')
    print('Proxy server is listeing on {}:{}'.format(HOST,PORT))
    proxy_socket.listen(1)
    # extract destination server IP address from request
    dest_ip = request_str.split()[1].split('/')[2]

    # print message with request details and time
    now = datetime.datetime.now()
    print(f"Received request for {dest_ip} at {now}")

    # send request to destination server
    dest_port = 80  # assume HTTP protocol
    dest_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_socket.connect((dest_ip, dest_port))
    dest_socket.sendall(request)

    # receive response from destination server
    response = b''
    while True:
        data = dest_socket.recv(1024)
        if not data:
            break
        response += data

    # print message with response details and time
    now = datetime.datetime.now()
    print(f"Received response from {dest_ip} at {now}")

    # send response back to client
    client_socket.sendall(response)

    # print message with sent response details and time
    now = datetime.datetime.now()
    print(f"Sent response back to client at {now}")

    # close connections
    dest_socket.close()
    client_socket.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_socket:
    proxy_socket.bind((HOST, PORT))
    proxy_socket.listen()

    while True:
        # wait for incoming connections
        client_socket, addr = proxy_socket.accept()

        # handle each request in a separate thread (optional)
        handle_request(client_socket)
