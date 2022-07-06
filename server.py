# python3
# chatroom v1.0.0
# GoldenFurDog

import socket

server = socket.socket() 

ip = input("输入本机IP地址(可用ifconfig,arp -a等命令获取):")
port = int(input("输入空闲的端口(1~65535):"))
name = input("请输入用户名:")
print("已记录为%s:%s,用户名:%s"%(ip,port,name))
server.bind((ip,port))
server.listen(5)
print("等待连接挂起。")
while True:
    client,addr = server.accept()
    print("客户端发现:%s"%(str(addr)))
    client.send(name.encode())
    rname = client.recv(1024).decode()
    while True:
        redata = client.recv(1024)
        if redata == "stop":
            break
        else:
            print("%s >>>"%(rname) + redata.decode())
        
        msg = input("%s >>>"%(name))
        if msg == "stop":
            break
        else:
            client.send(msg.encode())
        
    break
bye = str("对方已终止连接。")
client.send(bye.encode())
client.close
