import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 5192
BUFFER_SIZE = 2048

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen(1)
conn,addr = s.accept()
print (('connection address:',addr))
data1, data2 = [int(i) for i in conn.recv(BUFFER_SIZE).decode('utf-8').split('\n')]
data = int(data1)+int(data2)
conn.send((str(data).encode()))
conn.close()
