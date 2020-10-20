# simple TCP client
import socket

target_host = "www.google.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data
# python3 note - 
#   originally client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")\
#   resulted in TypeError: a bytes-like object is required, not 'str'
#   modified to encode the request
request = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.sendall(request.encode('utf-8'))

#receive some data
response = client.recv(4096)

# python3 note - print()
print(response)