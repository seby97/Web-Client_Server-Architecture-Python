import time
from socket import *
from time import strftime, gmtime
from math import sqrt
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
print ("Running")
serverName = "127.0.0.1"
clientSocket = socket(AF_INET,SOCK_DGRAM)
minRTT = 0
maxRTT = 0
compiledRTT = 0
list = []
packet_count = 0
clientSocket.settimeout(2)
x = int(input("Please input the number of packets that you want to send?"))


for i in range(x):
    now = dt.datetime.now()
    sequence_message = "ping_request" + " " + str(i+1)
    time_stamp =  str(now.strftime('%Y/%m/%d'))
    start = time.perf_counter()
    message = sequence_message + " " + time_stamp + " " + str(start)
    clientSocket.sendto((message.encode('utf-8')), (serverName, 12000))

    try:
        message, address = clientSocket.recvfrom(1024)
        elapsed = (time.perf_counter()-start)
        message = message.decode('utf-8')
        print(message, "(System Time) ,   RTT", " - ", elapsed)
        list.append(elapsed)

    except timeout:
        print("Request" , i+1, " timed out")
        packet_count += 1


clientSocket.settimeout(2)
clientSocket.close()



