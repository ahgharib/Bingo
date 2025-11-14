import socket

HOST = '192.168.100.22' # server IP (if only then the public IP address with myip.is)
PORT = 9999 # must be same port

socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((HOST, PORT))

socket.send("Hello Server this is Me!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))