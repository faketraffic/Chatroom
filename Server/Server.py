from Tharmsylogging import *
initialize()
import socket 
import sys
import os
import time
import threading



info('Starting server...')

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                if message == '/disconnect':
                    break
                print(f"{username}: {message}")
                broadcast(f"{username}: {message}", client_socket)
        except:
            break
    client_socket.close()
    for i, client in enumerate(clients):
        if client[0] == client_socket:
            clients.pop(i)
            break
    broadcast(f"{username} has left the chat.", None)
    error(f"{username} disconnected.")

def broadcast(message, sender_socket):
    for client in clients:
        if client[0] != sender_socket:
            client[0].send(message.encode())

def accept_connections(server_socket):
    while True:
        client_socket, addr = server_socket.accept()
        client_socket.send("USERNAME".encode())
        username = client_socket.recv(1024).decode()

        if any(username == u for _, u in clients):
            client_socket.send("Username is already taken. Please retry with a different username.".encode())
            client_socket.close()
            continue

        print(f"{username} connected")
        client_socket.send('Welcome to the chat room! Type /stop to exit.'.encode())
        clients.append((client_socket, username))
        thread = threading.Thread(target=handle_client, args=(client_socket, username))
        thread.start()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = int(input("Enter the port server on: "))
    server_socket.bind((host, port))
    server_socket.listen()
    good(f"Server is running on port {port}")
    accept_connections(server_socket)

clients = []
start_server()