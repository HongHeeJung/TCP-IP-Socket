import socket
import cv2
import numpy as np
import requests
from threading import Thread
 
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
ADDR = (HOST, PORT)
BUFF_SIZE = 1024

#TCP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
# server IP, port
s.bind(ADDR)
print('Socket bind complete')
threads = []

 
# connection, conn: socket, addr: bind address
conn,addr=s.accept()
 
class ClientTread(Thread):

    def __init__(self,host,port,sock):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.sock = sock
        print ("Check the new thread "+host+":"+str(port))
        
    def run(self):
        f = open("/home/heejunghong/BlackfencerWeb/index.html", 'r')
        while True:
            l = f.read(BUFF_SIZE)
            while(l):
                self.sock.send(l)
                print('Sent ',repr(l))
                l = f.read(BUFF_SIZE)
            if not l:
                f.close()
                self.sock.close()
                break
                
                 
while True:

    # wait client 
    s.listen(1)
    print('Socket now listening')
    (clientSocket, (host, port)) = s.accept()
    print ('Connection from ', (host, port))
    newthread = ClientThread(host, port, clientSocket)
    newthread.start()
    threads.append(newthread)
    
    for t in threads:
        t.join()
    
    # size of stringData (==(str(len(stringData))).encode().ljust(16))
    length = recvall(conn, 16)
    stringData = recvall(conn, int(length))
    data = np.fromstring(stringData, dtype = 'uint8')
    
    # decoding data
    frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
    print(np.shape(frame))
    cv2.imshow('ImageWindow',frame)
    cv2.waitKey(1)



