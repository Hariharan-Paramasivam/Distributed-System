import time,socket,sys

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080
#socket.socket: Create a new socket using the given address family, socket type and protocol number. The address family should be AF_INET (the default), AF_INET6 or AF_UNIX. The socket type should be SOCK_STREAM (the default), SOCK_DGRAM or perhaps one of the other SOCK_ constants. The protocol number is usually zero and may be omitted in that case.
#socket.gethostname(): Return a string containing the hostname of the machine where the Python interpreter is currently executing
#socket.gethostbyname(): Translate a host name to IPv4 address format. The IPv4 address is returned as a string, such as '
print("welcome to chat room")
print("Server will start on host: ", host_name)
print("Server IP: ", s_ip)

new_socket.bind((host_name, port))
#bind(): This method binds the address (hostname, port number pair) to the socket.
print("Binded successfully")
print("Server is waiting for incoming connections")
print("This is your IP: ", s_ip)    
name = input("Enter name: ")
new_socket.listen(1) #1 here means can connect to one client only
conn , add = new_socket.accept()
#listen(): This method sets up and start TCP listener. Here 1 means we can connect to one client
#accept(): This passively accept TCP client connection, waiting until connection arrives (blocking).

print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0]) #displaying the IP address of the client
#Exchange of messages
client = (conn.recv(1024)).decode()
print(client + ' has connected.')

conn.send(name.encode()) #sending server name to client
#recv(): This method receives TCP message
#displaying the name of the client who just connected
#sending greeting to the client
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
    #starts an infinite loop where messages are received from the client and displayed on the server
    #input() is used to take the message from the server
    #send() is used to send the message to the client
    #recv() is used to receive the message from the client
    #decode() is used to decode the message from the client
    if message == 'exit':
        break