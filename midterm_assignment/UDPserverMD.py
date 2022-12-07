from socket import * #library containing all the useful functions
import random

#Then we create an actual UDP server

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)                       #udp socket is created
serverSocket.bind(('', serverPort))                               #the server port is 12000
print("The server is ready to receive")

lost = random.randint(0, 9)                                         #4/10 chances to be lost

while True:                                                        #always looping     
    message, clientAddress = serverSocket.recvfrom(2048)            #receive informations on client
    print(message.decode())   
    message = 'OK'                   #message is decoded and read
    if (lost > 3):
        serverSocket.sendto(message.encode(), clientAddress)    #send the modified message back to client if not lost