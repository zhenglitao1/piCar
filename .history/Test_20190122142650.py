import socket

def getLocalIp():
    '''Get the local ip'''
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()
    return ip


def main():
    '''The main thread, control the motor'''
    host=getLocalIp()
    print('localhost ip :'+host)
    port=5050

    #Init the tcp socket
    tcpServer=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcpServer.bind((host,port))
    tcpServer.setblocking(0) #Set unblock mode
    tcpServer.listen(5)

    (client,addr)=tcpServer.accept()
    print('accept the client!')
    # oled.writeArea4(' Connect')
    client.setblocking(0)
    while True:
        time.sleep(0.001)
        try:
            data=client.recv(1024)
            data=bytes.decode(data)
            if(len(data)==0):
                print('client is closed')
                # oled.writeArea4(' Disconnect')
                break

        except socket.error:
            continue

print (main())