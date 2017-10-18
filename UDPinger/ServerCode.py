# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *
import time

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
setdefaulttimeout(5)
timeout_value = 0;
previous_sequence_number = 0;
while True:
    try:
        rand = random.randint(0, 10)
        # Receive the client packet along with the address it is coming from

        message, address = serverSocket.recvfrom(1024)
        server_time = time.perf_counter()
        serverSocket.settimeout(10)
        message = message.decode()
        messageArry = message.split(" ")
        sequence_number = messageArry[1];
        delay = float(float(messageArry[3]) - server_time)

        print("sequence number: ", sequence_number, " | time: ", delay)
        message = message.upper()

        if timeout_value > 0:
             if((sequence_number-1) != previous_sequence_number):
                    print("Packet was lost")

        else:
                print("Packet was received \n")
                timeout_value = 0

        previous_sequence_number = sequence_number

    except timeout:
        if timeout_value == 0:
                print("The client connection is down , closing socket")
                serverSocket.close()

# If rand is less is than 3, we consider the packet lost and do not respond
    if rand < 3:
         continue
    else:
         serverSocket.sendto(message.encode('utf-8'),address)
