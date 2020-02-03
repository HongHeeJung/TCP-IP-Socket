'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
코드 내용
# 1. 라즈베리파이3B+에서 ubuntu로 pi-camera 스트리밍_server
# 2. ubuntu에서 라즈베리파이3B+로 html파일 데이터 전송
# 3. ubuntu에서 라즈베리파이0로 신호(단일비트) 전송
# 4. ubuntu에서 안드로이드로 신호(단일비트) 전송
[시작 - 2020.01.20.] - pi-camera 스트리밍 코드
[수정 - 2020.02.02.] - ubuntu에서 html파일 scraping 코드 추가
[수정 - 2020.02.03.] - BlackIce 탐지 버퍼 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import socket
import cv2
import numpy as np
import requests

# import thread module
from _thread import *
import threading

print_lock = threading.Lock()

# thread function
def threaded(c):
	while True:

		# data received from client
		data = 
 
#socket에서 수신한 버퍼를 반환하는 함수
def recvall(sock, count):
    # 바이트 문자열
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def main():
	# localhost IP
	host = ""
    port = 5000
 
	# Create TCP Socket
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	# 서버의 IP와 PORT 지정
	s.bind((host, port))
	print('Socket binded to port', port)

    # put the socket into listening mode_waiting client (client 4개까지 ok)
    s.listen(4)
    print('Socket is listening')

    while True:

	    # establish connection with client (conn: 소켓 객체, addr: 소켓에 바인드 된 주소) 
	    conn,addr = s.accept()

        # client1_받은 stringData의 크기 (==(str(len(stringData))).encode().ljust(16))
        length = recvall(conn, 16)
        stringData = recvall(conn, int(length))
        data = np.fromstring(stringData, dtype = 'uint8')
    
        #client1_decoding data_영상 스트리밍
        frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
        print(np.shape(frame))
        cv2.imshow('ImageWindow',frame)
        cv2.waitKey(1)

	    #client2_yolo_mark bounding box 좌표값 전송(확인 안함)
	    resp = requests.get('http://home/heejunghong/BlackfencerWeb/index.html')
	    conn.send(resp.txt)

		#client3_rpi0에게 단일 비트 보내기
        conn.send(1)
		print("Alert to TTC")

        #client4_android에게 단일 비트 보내기
		conn.send("BlackIce was detected", 'UTF-8'))
		print("Alert to Android")

