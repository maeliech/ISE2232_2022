from socket import * #library containing all the useful functions
import json
import time

#we first create a client server: 

serverName = gethostname()                  #socket function is used to get host name
serverPort = 12000                          #specifying the port number
clientSocket = socket(AF_INET, SOCK_DGRAM)  #socket used by server

f= open('wheel_rotation_ sensor_data.json')        #Opening the file
data = json.load(f)             

message = ('Simple message')      #first message to send

for i in data['Data']:
    clientSocket.settimeout(1)  #starts measuring time   
    start = time.perf_counter() #starts counting time
    
    clientSocket.sendto(message.encode(), (serverName, serverPort))  #user writes the message to send, server name/port is attached to message
                                    
    message, serverAddress = clientSocket.recvfrom(2048)     #message is modified into a computer readable string
    try:
        end = time.perf_counter()                           #finish
        print (message.decode())                                  #message is printed and then
        ms = (end-start) * 10**6
        print(f"RTT {ms:.03f} micro secs.")
    except timeout:                                         #if it takes more than one second
        print('Packet has been lost')
    message = json.dumps(i)                                                   #json.dumps() to retrieve data

clientSocket.close()                                             #the socket is closed after use

