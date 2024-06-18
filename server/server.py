import asyncio, socket, threading

host = '0.0.0.0'                                                      #LocalHost
port = 8889                                                             #Choosing unreserved port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              #socket initialization
server.bind((host, port))                                               #binding host and port to socket
server.listen()
print(f'[!] - Server started :\nport "{port}"\nhost "{host}"')

clients = []
nicknames = []

# Broadcast message to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handle individual client connections
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            decoded_message = message.decode('utf-8').strip()
            if len(decoded_message) == 0:
                client.send("[!] - You can't send empty messages".encode('utf-8'))
            else:
                broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

# Accept new connections
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICKNAME'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()