from socket import *

print('연결을 시도합니다...')
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))

print('연결 확인 됐습니다.')
clientSock.send('I am a client'.encode('utf-8'))
while True:
    clientSock.send(input().encode('utf-8'))

    print('메시지를 전송했습니다.')

    data = clientSock.recv(1024)
    if not data:
        break;
    print('len : ', len(data))
    print('받은 데이터 : ', data.decode('utf-8'))

clientSock.close()