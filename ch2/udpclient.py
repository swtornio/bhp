# simple UDP client

import socket

target_host = "127.0.0.1"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
# python3 note - encoding send string
send_data = "AABBCCDD"
client.sendto(send_data.encode('utf-8'),(target_host,target_port))

# receive some data
data, addr = client.recvfrom(4096)

# python3 note - print()
print(data)