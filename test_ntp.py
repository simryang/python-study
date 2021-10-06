import ntplib
import time

strNtpAddress = 'europe.pool.ntp.org'
def ntpCurTime(strNtpAddress) :
    c = ntplib.NTPClient()
    response = c.request(strNtpAddress)
    print (time.ctime(response.tx_time))
    print (time.time())
    print (time.localtime())
    #return time.time(response.tx_time)

from socket import AF_INET, SOCK_DGRAM
import sys
import socket
import struct, time
 
def getNTPTime(host = "pool.ntp.org"):
        port = 123
        buf = 1024
        address = (host,port)
        msg = '\x1b' + 47 * '\0'
 
        # reference time (in seconds since 1900-01-01 00:00:00)
        TIME1970 = 2208988800 # 1970-01-01 00:00:00
 
        # connect to server
        client = socket.socket( AF_INET, SOCK_DGRAM)
        client.sendto(msg.encode('utf-8'), address)
        msg, address = client.recvfrom( buf )
 
        t = struct.unpack( "!12I", msg )[10]
        t -= TIME1970
        return time.ctime(t).replace("  "," ")
 
if __name__ == "__main__":
        print(getNTPTime())

#print(ntpCurTime())
        from multiprocessing import Process
        proc = Process(target=getNTPTime)
        proc.start()
        print(proc.name)