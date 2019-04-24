import socket                  

s = socket.socket()            
host = socket.gethostname()     
port = 60000                    

s.connect((host, port))
s.send(input("\nEnter filename: ").encode())

status = s.recv(1024).decode()
if status == "found":
    print("File found")
    with open('received_file', 'wb') as f:
        while True:
            data = s.recv(1024)
            if not data:
                break
            f.write(data)
        f.close()
    print("Recieved file")
else:
    print("File not found")

s.close()
