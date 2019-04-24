import socket                  

port = 60000                    
s = socket.socket()             
host = socket.gethostname()     
s.bind((host, port))           
s.listen(5)                     

print('Server listening...')

while True:
    conn, addr = s.accept()    
    print('\nGot connection from', addr)
    filename = conn.recv(1024).decode()
    print('Client requested', filename)
    
    try:
      f = open(filename,'rb')
      conn.send("found".encode())
      l = f.read(1024)
      while (l):
         conn.send(l)
         l = f.read(1024)
      f.close()
      print('\nDone sending')

    except FileNotFoundError:
       print('\nFile not found')

    finally:
       print("Closing connection")
       conn.close()
       break #to break out of the loop or continue listening

