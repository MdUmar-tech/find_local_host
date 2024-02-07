import socket

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

local_ip = get_local_ip()
print("Local IP Address:", local_ip)
