import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("localhost", 12345)
message = b"Hello, server!"
print("Sending:", message)
client_socket.sendto(message, server_address)

data, server_address = client_socket.recvfrom(4096)
print("Received:", data.decode(), "from", server_address)

client_socket.close()
