import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 12345)
client_socket.connect(server_address)

try:
    message = b"Hello, server!"
    print("Sending:", message)
    client_socket.sendall(message)

    data = client_socket.recv(1024)
    print("Received:", data.decode())

finally:
    client_socket.close()
