import socket
import threading

emoji_map = {
    ":smile:": "😄",
    ":sad:": "😢",
    ":laugh:": "😂",
    # TODO: ADD API
}

def replace_emojis(message):
    for text, emoji in emoji_map.items():
        message = message.replace(text, emoji)
    return message

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if "Username is already taken" in message:
                print("Username is already taken. Please retry with a different username.")
                return False
            print(message)
        except:
            print("Disconnected from the server.")
            return True

def start_client():
    global username
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Enter the server IP address: ")
    port = int(input("Enter the server port number: "))
    username = input("Enter your username: ")
    client_socket.connect((host, port))
    client_socket.send(username.encode())
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()
    while True:
        message = input('')
        if message:
            if message == '/disconnect':
                break
            message = replace_emojis(message)
            client_socket.send(message.encode())
    client_socket.close()

start_client()
