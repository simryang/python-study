from socket import *
from time import sleep # for sleep

print('starting server...')
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)

print('server is ready. waiting client...')
connectionSock, addr = serverSock.accept()
print(str(addr),'에서 접속이 확인되었습니다.')

while True:
    connectionSock.send('종료하시려면 exit 나 quit 를 입력하세요'.encode('utf-8'))
    data = connectionSock.recv(1024)
    
    print('받은 데이터 : ', data.decode('utf-8'))

    if data.decode('utf-8') in ('exit', 'quit'):
        connectionSock.send('exit or quit as received bye'.encode('utf-8'))
        sleep(0.01)
        connectionSock.shutdown(SHUT_WR)
        connectionSock.close()
        break
    else:
        str = 'I am a server: ' + data.decode('utf-8')
        connectionSock.send(str.encode('utf-8'))
        print('메시지를 보냈습니다.')