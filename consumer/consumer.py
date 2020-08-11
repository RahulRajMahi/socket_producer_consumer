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

try:
    s.connect((HOST, PORT))
except socket.error as message:
    s.close()
    s = None
    sys.exit(1)

print("I am client and I'll accept data on port 45559")

full_msg = b''
new_msg = True
while True:
    msg = s.recv(256)
    if not msg:
        #break
        continue
    if new_msg:
        msglen = int(msg[:HEADERSIZE])
        new_msg = False

    full_msg += msg
    if len(full_msg) - HEADERSIZE == msglen:
        data = pickle.loads(full_msg[HEADERSIZE:])
        if data == "quit":
            print("Disconnecting!!!")
            break
        print("I've received the data and its type is :", type(data))
        print("Received data : ", data)
        print()
        new_msg = True
        full_msg = b""
s.close()
