import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5012

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("Data received from", addr)

    num = data.decode().split("\n")
    s=int(num[0])+int(num[1])
    sock.sendto(str(s).encode(), (addr[0], addr[1]))
