import socket
ip_port = ('192.168.1.246',9999)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall('请求占领地球')

server_reply = sk.recv(1024)
print server_reply

sk.close()

socket client