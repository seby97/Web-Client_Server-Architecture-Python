from socket import *
from time import strftime, gmtime
from math import sqrt
import sys
from sys import argv
serverName = argv[1]
Port = argv[2]
filename = argv[3]
buffer_size = 1024
print ("Running")
serverHost_address = (serverName , int(Port))
clientSocket = socket(AF_INET,SOCK_STREAM)
final_message = ""
while True:

    try:
        clientSocket.connect(serverHost_address)
        header = {
	        "first_header" : "GET /%s HTTP/1.1" %(filename),
	        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	        "Accept-Language": "en-us",
	        "Host": "%s:%s" %(serverName, Port),
	    }

        http_header = "\r\n".join("%s:%s" %(item,header[item]) for item in header)
        print(http_header)
        final_header = "%s\r\n\r\n" %(http_header)
        clientSocket.send(final_header.encode('utf-8'))

        response_message = clientSocket.recv(buffer_size)
        response_message = response_message.decode('utf-8')
        print("bug")
        while response_message:
             final_message+= response_message
             response_message =clientSocket.recv(buffer_size)
             response_message = response_message.decode('utf-8')
        print(final_message)
    except IOError:
        sys.exit()


response_message = clientSocket.recv(buffer_size)
response_message = response_message.decode('utf-8')
print("bug")
while response_message:
    final_message+= response_message
    response_message =clientSocket.recv(buffer_size)
    response_message = response_message.decode('utf-8')

print(final_message)
clientSocket.close()