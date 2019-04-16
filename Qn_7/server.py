import socket 
import select 
import sys 
from _thread import *
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
  
IP_address = "127.0.0.1"
Port = 8081

server.bind((IP_address, Port)) 
server.listen(100) 
  
list_of_clients = [] 
  
def clientthread(conn, addr): 
  
    conn.send("Welcome to this chatroom!".encode()) 
  
    while True: 
            try: 
                message = conn.recv(2048).decode() 
                if message: 

                    print("<user " + str(list_of_clients.index(conn)+1) + "> " + message) 
  
                    # Calls broadcast function to send message to all 
                    message_to_send = ("<user "+ str(list_of_clients.index(conn)+1)  + "> " + message) 
                    broadcast(message_to_send.encode(), conn) 
  
                else: 
                    """message may have no content if the connection 
                    is broken, in this case we remove the connection"""
                    remove(conn) 
  
            except: 
                continue
  
def broadcast(message, connection): 
    for clients in list_of_clients: 
        if clients!=connection: #broadcast message to all clients apart from the current client
            try: 
                clients.send(message) 
            except: 
                clients.close() 
  
                # if the link is broken, we remove the client 
                remove(clients) 
  
def remove(connection): 
    if connection in list_of_clients: 
        list_of_clients.remove(connection) 
  
while True: 

    conn, addr = server.accept() 
    list_of_clients.append(conn) 
  
    # prints the address of the user that just connected 
    print(addr[0] + " connected")
  
    # creates and individual thread for every user that connects
    start_new_thread(clientthread,(conn,addr))     
  
conn.close() 
server.close() 