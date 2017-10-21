import time
from socket import *

from time import strftime, gmtime

print ("Running")
serverName = "127.0.0.1"
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(2)
for i in range(10):

    message = "ping request" + " " + str(i+1) + ",  " + strftime("%d %b %Y %H:%M:%S +0000", gmtime())
    start=time.time()
    clientSocket.sendto(message.encode('utf-8'),(serverName, 12000))

    try:
        message, address = clientSocket.recvfrom(1024)

        elapsed = (time.time()-start)
        message = message.decode('utf-8')
        print(message, "RTT", elapsed )


    except timeout:
        print("Request" , i, " time out")


clientSocket.close()
