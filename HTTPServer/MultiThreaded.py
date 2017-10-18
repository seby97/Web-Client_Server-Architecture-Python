from socket import *
from threading import Thread
import datetime as dt

serverPort = 8888
TCP_IP = "127.0.0.1"
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((TCP_IP,serverPort))
serverSocket.listen(5)
print ("Running and Listening for Knocks")
buffer_size = 1024
threads = []


class ClientThread(Thread):

    def __init__(self,ip,port,sock):
            Thread.__init__(self)
            self.ip = ip
            self.port = port
            self.sock = sock
            print("New thread started for " + str(ip) + ":" + str(port) )

    def run(self):
        try:
            message = connectionSocket.recv(buffer_size)
            message = message.decode('utf-8') #added this line cause i will be encoding the get message
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            print("output data\n", outputdata)
            now = dt.datetime.now()
            first_header = "HTTP/1.1 200 OK"

            header_info = {
			"Date": now.strftime("%Y-%m-%d %H:%M"),
			"Content-Length": len(outputdata),
			"Keep-Alive": "timeout=%d,max=%d" %(10,100),
			"Connection": "Keep-Alive",
			"Content-Type": "text/html"
		}

            following_header = "\r\n".join("%s:%s" % (item, header_info[item]) for item in header_info)
            response_message = "%s\r\n%s\r\n\r\n" %(first_header, following_header)
            response_message = response_message.encode('utf-8')
            connectionSocket.send(response_message)

                  #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode('utf-8'))

            #connectionSocket.send("\r\n".encode('utf-8'))
            connectionSocket.close()

        except IOError:
            error_message = "HTTP/1.1 404 Not Found\n" + "Content-Type: text/html\n" + "\n" + "<html><body>ERROR 404 FILE NOT FOUND</body></html>\n"
            print("output data\n", error_message)
            error_message = error_message.encode('utf-8')
            connectionSocket.send(error_message)
            connectionSocket.close()


while True:
    serverSocket.listen(5)
    connectionSocket, (IP,PORT) = serverSocket.accept()
    newthread = ClientThread(IP,PORT,connectionSocket)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()


sys.exit()


