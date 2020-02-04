import socket
import cv2
import numpy as np
# import requests
import _thread
import threading
import thread
from thread import *
import time
import random

 
# Streaming_return buffer
def recvall(sock, count):
    
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

# Send_open/read file
def sendcord(str):                                 #CHANGE THIS NUM

    #client2_yolo_mark bounding box 
    f = open("/home/heejunghong/BlackfencerWeb/index.html", 'r')
    data = f.read()
    conn.send(str(data))
    f.close()
    
    global tot
    lock.aquire()
    try:
        tot += amount
    finally:
        lock.release()
    print (threading.currentThread().getName()+' Synchronized :',tot)

# Connect
def connect():
	# localhost IP
    host = "192.168.255.21"
    port = 5000
 
    # Create TCP Socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.bind((host, port))
    print('Socket binded to port', port)

    # put the socket into listening mode_waiting client (client 4 ok)
    s.listen(4)
    print('Socket is listening')


    while True:
        # establish connection with client (conn: socket, addr: binded address) 
        conn,addr = s.accept() 
        
        # lock aquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
                
        #  stringData size (==(str(len(stringData))).encode().ljust(16))
        length = recvall(conn, 16)
        stringData = recvall(conn, int(length))
        data = np.fromstring(stringData, dtype = 'uint8')
    
        # client1_decoding data_streaming
        frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
        print(np.shape(frame))
        cv2.imshow('ImageWindow',frame)
        cv2.waitKey(1)

if __name__== '__main__':
    connect()
    # for i in range(10000):
    thread.start_new_thread(recvall)
    thread.start_new_thread(sendcord)
    print('STOP?')
        # thread1 = threading.Thread(recvall, args=(i))
        # thread1.start()   
        # thread2 = threading.Thread(target = sendcord, args=(i))
        # thread2.start()        
        

