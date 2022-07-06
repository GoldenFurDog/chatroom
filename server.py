# python3
# chatroom v1.0.0
# GoldenFurDog

import socket

server = socket.socket() 

ip = input("键入本机IP地址(可用ifconfig,arp -a等命令获取):")
port = int(input("键入空闲的端口(1~65535):"))
print("已记录为%s:%s"%(ip,port))
server.bind((ip,port))
server.listen(5)
while True:
    client,addr = server.accept()
    print("客户端发现:%s"%(str(addr)))
    while True:
        redata = client.recv(1024)
        if redata == "stop":
            break
        else:
            print("对方 >>>" + redata.decode())
        
        msg = input("你 >>>")
        if msg == "stop":
            break
        else:
            client.send(msg.encode())
        
    break
bye = str("对方已终止连接。")
client.send(bye.encode())
client.close
