from Tharmsylogging import *
initialize()
import socket 
import sys
import os
import time
import threading



info('Starting server...')

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Message from {client_socket.getpeername()}: {message}")
                broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(client)


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = int(input("Enter port: "))

    server_socket.bind((host, port))
    server_socket.listen()

    good(f"Server is running on port {port}")


    while True:
        client_socket, addr = server_socket.accept()
        good(f"Connection from {addr}")

        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

clients = []
server()
