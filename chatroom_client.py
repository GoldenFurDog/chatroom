#python3
#chatroom_client v1.0.0
#GoldenFurDog

import socket
import time

client = socket.socket()
ip = input("输入主机IP:")
port = int(input("输入主机端口:"))
print("已记录为%s:%s"%(ip,port))
time.sleep(2)
client.connect((ip,port))
while True:
    message = input("你 >>>")
    client.send(message.encode())
    redata = client.recv(1024)
    print("对方 >>>" + redata.decode())
