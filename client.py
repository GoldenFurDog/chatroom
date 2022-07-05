# python3
# chatroom v1.0.0
# GoldenFurDog

import socket

client = socket.socket()

ip = input("请键入服务器IP:")
port = int(input("请输入服务器开放的端口:"))
print("已记录为%s:%s"%(ip,port))
client.connect((ip,port))
print("已成功连接！")

while True:
    msg = input("你 >>>")
    client.send(msg.encode())
    redata = client.recv(1024)
    print("对方 >>>" + redata.decode())
