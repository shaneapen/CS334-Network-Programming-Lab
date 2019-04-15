import socket

TCP_IP="127.0.0.1"
TCP_PORT=5191
BUFFER_SIZE=1

MSG1 =raw_input("Enter 1st number")
MSG2 =raw_input("Enter 2nd number")

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
s.send(MSG1)
s.send(MSG2)
data = s.recv(2)
s.close()
print "sum is:",data
