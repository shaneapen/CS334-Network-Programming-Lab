import socket

TCP_IP="127.0.0.1"
TCP_PORT=5191
BUFFER_SIZE=1

MSG1 =input("Enter 1st number: ")
MSG2 =input("Enter 2nd number: ")

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
s.send((str(MSG1).encode()))
s.send((str(MSG2).encode()))
data = s.recv(2).decode()
s.close()
print (("sum is:",data))
