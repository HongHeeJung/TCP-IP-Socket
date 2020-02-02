# TCP-IP-Socket
TCP/IP Socket Programming  
:paperclip:코드 설명  
라즈베리파이와 ubuntu 간의 Socket 통신  
1. 라즈베리파이에서 ubuntu로 pi-camera 스트리밍  
2. ubuntu에서 라즈베리파이로 html파일 데이터 전송  


> ## :sunflower: HTTP 통신 VS Socket 통신  
> ### 접속을 유지하느냐  
> * HTTP 통신  
> HyperText Transfer Protocol  
> Client가 요청을 보내는 경우에만 Server가 응답 -> 단방향적 통신  
> Server로부터 응답을 받은 후에는 연결이 바로 종료됨  
> 실시간 통신이 아닌 필요한 경우에만 Server로 접근하는 콘텐츠 위주의 데이터를 사용할 때 쓰임  
>
> * Socket 통신  
> Server와 Client가 계속 연결을 하고 있음 -> 실시간으로 양방향 통신  
> Server 역시 Client로 요청을 보낼 수 있음  
> 실시간 동영상 Streaming이나 온라인 게임에서 쓰임  
> TCP/IP와 UDP가 있음  
>
>
> ## :sunflower: TCP/IP 통신 VS UDP 통신  
> ### 속도냐 정확도냐  
> * TCP/IP Socket  
> Transmission Control Protocol  
> 데이터를 주고 받을 양단 간에 먼저 연결 설정 후, 설정된 연결을 통해 양방향으로 데이터 전송  
> 메시지 수신 확인 -> 신뢰성 좋음  
> 메시지가 보내진 순서를 보장하기 위해 재조립함 -> 순서 보장  
> 사용: 웹 브라우저들이 World Wide Web에서 서버에 연결할 때, 이메일 전송이나 파일 전송할 때  
> 
> * UDP Socket  
> User Datagram Protocol  
> 연결 설정하지 않음
> 수신자가 데이터를 받을 준비를 확인하는 단계를 거치지 않고 단방향으로 정보 전송 (전송 방식 단순)  
> 수신자가 메시지 수신했는지 확인할 수 없음 -> 신뢰성 낮음 (메시지 중복/누락 가능)  
> 메시지(데이터그램) 도착 순서를 예측할 수 없음 -> 순차 보장 없음  
> TCP보다 속도가 일반적으로 빠르고 오버헤드가 적음  
> 사용: TCP의 안정성을 필요로 하지 않는 애플리케이션 (DNS, IPTV, IP 터널, 온라인 게임 등)  
>
>
>참고
>https://ko.wikipedia.org/wiki/%EC%A0%84%EC%86%A1_%EC%A0%9C%EC%96%B4_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C  
>https://ko.wikipedia.org/wiki/%EC%82%AC%EC%9A%A9%EC%9E%90_%EB%8D%B0%EC%9D%B4%ED%84%B0%EA%B7%B8%EB%9E%A8_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C  
>https://mangkyu.tistory.com/48  
