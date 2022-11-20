import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("localhost", 12345))

server_socket.listen(5)
print("Server is listening for incoming connections...")

client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} established.")

client_socket.send(b"Hello from the server!")

data = client_socket.recv(1024)
print("Received data:", data.decode())

client_socket.close()
