"""
CODE
# Raspberry pi to ubuntu: pi-camera streaming
# ubuntu to Raspberry pi: sending html data
[Correction - 2020.02.02.] - ubuntu: html file scraping code
"""

import socket
import cv2
import numpy as np
# import requests
# from threading import Thread
 
# buffer return
def recvall(sock, count):
   
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

# HOST = socket.gethostname() 
HOST = '192.168.255.21'
PORT = 5000
# ADDR = (HOST, PORT)
# BUFF_SIZE = 1024

#TCP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')
 
# server IP, port
s.bind((HOST,PORT))
print('Socket bind complete')
# wait client 
s.listen(1)
print('Socket now listening')
 
# connection, conn: socket, addr: bind address
conn,addr=s.accept()
 
while True:
    # size of stringData (==(str(len(stringData))).encode().ljust(16))
    length = recvall(conn, 16)
    stringData = recvall(conn, int(length))
    data = np.fromstring(stringData, dtype = 'uint8')
    
    # decoding data
    frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
    print(np.shape(frame))
    cv2.imshow('ImageWindow',frame)
    cv2.waitKey(1)

    f = open("/home/heejunghong/BlackfencerWeb/index.html", 'r')
    data = f.read()
    s.send(data)
    f.close()

