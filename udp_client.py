import socket

target_host = input('Target host: \n') #"127.0.0.1"
target_port = int(input('Target host: \n'))

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto(b"AAABBBCCC", (target_host, target_port))

# receive some data
data, addr = client.recvfrom(4096)

client.close()

print(data)