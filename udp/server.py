import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("localhost", 12345)
server_socket.bind(server_address)

while True:
    print("Waiting to receive data...")
    data, client_address = server_socket.recvfrom(4096)
    print("Received:", data.decode(), "from", client_address)

    server_socket.sendto(data, client_address)
