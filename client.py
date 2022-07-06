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
    if msg == "stop":
        break
    else:
        client.send(msg.encode())
    
    redata = client.recv(1024)
    if redata == "stop":
        break
    else:
        print("对方 >>>" + redata.decode())
    
bye = str("对方已终止连接。")
client.send(bye.encode())
client.close

