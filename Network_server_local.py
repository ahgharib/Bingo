import socket
import threading

HOST = '192.168.100.22' # 0.0.0.0 for the private IP address online
PORT = 9998

CODE = 'ascii' # 'utf-8'   Must be the same as the client/ message encode decode
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen() # I can put a number for the number of players per time

clients = []
nicknames = []

def broadcast(msg):
    for client in clients:
        client.send(msg)


def delete_client(client, clients, nicknames):
    index = clients.index(client)
    clients.remove(client)
    client.close()
    nickname = nicknames[index]
    msg = f"{nickname} Logged out".encode(CODE)
    broadcast(msg)
    nicknames.remove(nickname)
    return clients, nicknames
            

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            msg = f"{nickname} Logged out".encode(CODE)
            broadcast(msg)
            nicknames.remove(nickname)
            break

            
def recive():
    while True:
        client, address = server.accept()
        print(f"Connected To {str(address)}")
        client.send('NICK'.encode(CODE))
        nickname = client.recv(1024).decode(CODE)
        nicknames.append(nickname)
        clients.append(client)
        print(f"Successfully recived the Client nickname: {nickname}")
        msg = f"{nickname} logged in".encode(CODE)
        # if msg == f'{nickname}: Quit^-^':
        #     client.close()
        #     msg = f
        #     broadcast(msg)
        broadcast(msg)
        client.send('you have Logged in Successfully ^-^'.encode(CODE))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is Listining........")
recive()