import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 5192
BUFFER_SIZE = 2048

num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
s.sendall(str.encode("\n".join([str(num1), str(num2)])))
data = s.recv(2*BUFFER_SIZE).decode()
s.close()
print ("sum is:",data)
