# python3
# chatroom_server v1.0.0
# GoldenFurDog

import time
import socket

server_start():
host = socket.socket()
ip = input("输入主机IP地址:")
port = int(input("输入未被占用的端口:"))
print("已记录为%s:%s"%(ip,port))
time.sleep(2)
host.bind((ip,port))
host.listen(15)
print("服务端开启成功")
while True:
    con = host.accept()
    while True:
        redata = con.recv(1024)
        print("对方 >>>" + redata.decode())
        message = input("你 >>>")
        con.send(message.encode)
        if redata == "bye" or message == "bye":
            con.close()
