class Person:


    def getLocalIp():
        '''Get the local ip'''
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.connect(('8.8.8.8',80))
            ip=s.getsockname()[0]
        finally:
            s.close()
        return ip
p=Person('Bill')
print (p.sayhello())