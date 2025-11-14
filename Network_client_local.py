import socket
import threading

nickname = input("Enter your nickname: ")

HOST = '192.168.100.22' # server IP (if only then the public IP address with myip.is)
PORT = 9998 # must be same port
CODE = 'ascii' # 'utf-8'   Must be the same as the server/ message encode decode

client =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

def wait_and_recive():
    while True:
        try:
            msg = client.recv(1024).decode(CODE)
            if msg == 'NICK':
                client.send(nickname.encode(CODE))
            else:
                print(msg)
        except:
            print("An Unexpected Error has Occured please try to login again!")
            client.close()
            break


def write_and_send():
    while True:
        msg = f'{nickname}: {input("")}'
        # if msg == f'{nickname}: Quit^-^':
        #     client.send(msg.encode(CODE))
        #     print("BYE!")
        #     client.close()
        #     break
        client.send(msg.encode(CODE))

recive_thread = threading.Thread(target=wait_and_recive)
recive_thread.start()
send_thread = threading.Thread(target=write_and_send)
send_thread.start()