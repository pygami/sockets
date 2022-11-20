import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 12345)
server_socket.bind(server_address)

server_socket.listen(5)

while True:
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()
    try:
        print("Connection from", client_address)

        while True:
            data = connection.recv(1024)
            if not data:
                break
            print("Received:", data.decode())
            connection.sendall(data)
    finally:

        connection.close()
