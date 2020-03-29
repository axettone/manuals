#!/usr/bin/env python3

"""
Sockets.py
Author: Paolo Niccolò Giubelli <paoloniccolo.giubelli@itestense.it>

This is a demo to show how to build a simple echo server
in python (server sockets).

"""

import argparse
import socket
import threading

class MyServer:
    port = 1234
    socket = None
    def __init__(self, port=1234):
        self.port = port

    def client_thread(self, clientsocket, address):
        print(f"Client {address} connected")
        # Receive 1024 bytes
        data = clientsocket.recv(1024)
        # String heaven
        my_str = str(data.decode("utf-8")).rstrip('\n')
        print(my_str)

    def listen(self):
        print(f"Listening on port {self.port}")
        # Initialize the socket (IP, TCP)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind to network card:port
        self.socket.bind(("0.0.0.0", self.port))
        # Listen
        self.socket.listen(5)
        while True:
            # A client connects
            (clientsocket, address) = self.socket.accept()
            # Bind the connection to a handling thread
            ct = threading.Thread(target=self.client_thread, args=(clientsocket,address))
            # Start the thread, detach and listen for new connections
            ct.start()

server = None

def main():
    global server
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description="Socket creation example")
    parser.add_argument("port", type=int, help="Listen on this port")
    args = parser.parse_args()
    server = MyServer(args.port)
    server.listen()

if __name__ == "__main__":
    main()