import socket
import threading

# Client setup
nickname = input("[*] - Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8889))  # Ensure this matches the server port

# Receive messages from the server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("[!] - An error occurred!")
            client.close()
            break

# Send messages to the server
def write():
    while True:
        message = input('')
        if message.strip():  # Ensure the message is not empty or whitespace
            client.send(f'{nickname}: {message}'.encode('utf-8'))
        else:
            print("[!] - You can't send empty messages")

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
