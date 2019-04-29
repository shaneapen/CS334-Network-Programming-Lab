import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5012
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP

num1 = input("Enter 1st number:")
num2 = input("Enter 2st number:")

num = "\n".join([num1,num2]).encode()

sock.sendto(num, (UDP_IP, UDP_PORT))
data,addr = sock.recvfrom(1024)

print ("Sum is",data.decode())
