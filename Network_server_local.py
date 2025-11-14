import socket
HOST = '192.168.100.22'
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5) # I can put a number for the number of players per time

while True:
    communication_socket, address = server.accept()
    print(f"Connected To {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"THE MESSAGE: {message}")
    communication_socket.send(f"GOT Your Message!".encode('utf-8'))
    print(f"Communication with {address} Ended!")