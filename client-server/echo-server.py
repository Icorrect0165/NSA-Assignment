# Server side of the network application

import socket
# 1-Server sets up a listening socket

HOST = "127.0.0.1"
PORT = 45677

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(12)
    print(f"Server is listening on port", PORT)
    conn, addr = s.accept()

# 3-Data exchange between client and server
# server is Willy
    with conn:
        print(f"Connected by:{addr}")
        print(f"you are talking to Max!!")

        # Data is the message received from client
        # ("message") is the message sent by the server.
        while True:
            data = conn.recv(1024)
            if not data:
                conn.close()
            print("Max:", data)
            message = input(b"Willy:")
            conn.sendall(message.encode())


