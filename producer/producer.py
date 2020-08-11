import socket
import sys
import pickle

HEADERSIZE = 8
HOST = '127.0.0.1'
PORT = 45559

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as message:
    s = None
    sys.exit(1)

socket.setdefaulttimeout(5.0)

try:
    s.bind((HOST, PORT))
    s.listen()
except socket.error as message:
    s.close()
    s = None
    sys.exit(1)

#print("I am server and I'm running on port ", PORT)
print(f"I am server and I'm running on port {PORT}")
print(" -- Waiting for client's request --")

client_socket, address = s.accept()
print(f"Connection from {address} has been established.")

def start_listen():
    try:
        d = eval(input('Enter the data to be sent <Type "quit" for disconnecting client....>: '))
        print('Sending data of type : ', type(d))
        print(d)
        msg = pickle.dumps(d)
        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8') + msg
        global client_socket
        global address
        client_socket.send(msg)
        msg = pickle.loads(msg[HEADERSIZE:])
        if msg == "quit":
            print(f"Connection from {address} has been disconnected!!!")
            print()
            print(" -- Waiting for client's request --")
            try:
                client_socket, address = s.accept()
                print(f"Connection from {address} has been established.")
                start_listen()
            except TimeoutException:
                client_socket = False
                print('Timeout !!!')
            except KeyboardInterrupt:
                client_socket = False
                print('"ctrl+c" encountered!!')
    except KeyboardInterrupt:
        client_socket = False
        print('"ctrl+c" encountered!!')

while True:
    if not client_socket:
        s.close()
        print('Good Bye !!!')
        sys.exit(1)
    else:
        start_listen()
