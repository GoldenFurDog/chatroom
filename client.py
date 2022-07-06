# python3
# chatroom v1.0.0
# GoldenFurDog

import socket

client = socket.socket()

ip = input("请输入服务器IP:")
port = int(input("请输入服务器开放的端口:"))
name = input("请输入用户名:")
print("已记录为%s:%s,用户名:%s"%(ip,port,name))
client.connect((ip,port))
print("已成功连接！")
rname = client.recv(1024).decode()
client.send(name.encode())

while True:
    msg = input("%s >>>"%(name))
    if msg == "stop":
        break
    else:
        client.send(msg.encode())
    
    redata = client.recv(1024)
    if redata == "stop":
        break
    else:
        print("%s >>>"%(rname) + redata.decode())
    
bye = str("对方已终止连接。")
client.send(bye.encode())
client.close
