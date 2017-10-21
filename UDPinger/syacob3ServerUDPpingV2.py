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
serverSocket.settimeout(15)
timeout_value = 10;
previous_sequence_number = 1;
while True:
    try:

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

        if delay > timeout_value:
             if((sequence_number-1) != previous_sequence_number):
                    print("Packet was lost")

        else:
                print("Heartbeat Detected")

        previous_sequence_number = sequence_number
        serverSocket.sendto(message.encode('utf-8'), address)

    except timeout:
            print("\nHeartbeat Down, Client Assumed Down , Closing Connection")
            serverSocket.close()
            exit(0)

