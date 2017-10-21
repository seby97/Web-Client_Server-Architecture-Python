#import socket module
from socket import *
import sys # In order to terminate the program


#Prepare a sever socket
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ("Running")
while True:

    connectionSocket, (IP,PORT) = serverSocket.accept()
    print("New connection created for " + IP)

    try:
        message = connectionSocket.recv(1024)#Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        response_message = "HTTP/1.1 200 OK\n" + "Content-Type: text/html\n\n"
        response_message = response_message.encode('utf-8')
        connectionSocket.send(response_message)

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode('utf-8'))
        connectionSocket.send("\r\n".encode('utf-8'))
        connectionSocket.close()
    except IOError:
        error_message = "HTTP/1.1 404 Not Found\n" + "Content-Type: text/html\n" + "\n" + "<html><body>ERROR 404 FILE NOT FOUND</body></html>\n"
        error_message = error_message.encode('utf-8')
        connectionSocket.send(error_message)
        connectionSocket.close()

    serverSocket.close()

    sys.exit()  # Terminate the program after sending the corresponding data

