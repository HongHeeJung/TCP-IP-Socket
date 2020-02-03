# -*- coding: utf8 -*-
#import requests
import socket
import numpy as np
 
## TCP 사용
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
## server ip, port
s.connect(('192.168.255.26', 6000))
print('Connected')
 
while True:
    
    # 제대로 읽으면 ret = True, 실패면 ret = False, frame에는 읽은 프레임
    #ret, frame = cam.read()
 
    #서버에 데이터 전송
    #(str(len(stringData))).encode().ljust(16)
	#resp = requests.get('http://home/heejunghong/BlackfencerWeb/index.html')
	#conn.sendall(resp.txt)
    f = open("/home/heejunghong/BlackfencerWeb/index.html", 'r')
    data = f.read()
    s.send(data)
    f.close()
s.close()

