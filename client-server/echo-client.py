# Client side of the network application
# This program sends a message to the server and receives a response from the server.

import socket

HOST = "127.0.0.1"
PORT = 45677

# 2-Client connects to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to server on port", PORT)
    print (f"you are talking to Willy!!")
    # 3-Data exchange between client and server
    # the client is Max
    message = (b"Hello Willy!!")
    s.sendall(message)
    while True:
        data = s.recv(1024)
        if not data:
            s.close()
        print(f'Willy:', data)
        message = input(b'Max:' )
        s.sendall(message.encode())
    


        # if not data:
        #     break
    


