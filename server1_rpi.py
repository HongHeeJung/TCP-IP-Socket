import socket
import numpy as np
 

def recv(sock, count):
    
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf
 
HOST = '192.168.255.21'
PORT = 6000
 
#TCP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')
 
#
s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(1)
print('Socket now listening')
 

conn,addr = s.accept()
 
while True:
    # (==(str(len(stringData))).encode().ljust(16))
    length = recv(conn, 16)
    stringData = recv(conn, int(length))
    data = np.fromstring(stringData, dtype = 'uint8')
	print data
    
 
