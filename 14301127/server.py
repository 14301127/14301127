import socket
import threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建socket类型的对象s
s.bind(("127.0.0.1",3333)) #调用socket对象s里的bind方法绑定IP:127.0.0.1和端口:3333
s.listen(1) #监听
count=0 #用来计数连接上的客户端

#自定义函数mutilclient
def mutilclient(sock,count):
    print("Got connection from client" ,count) #打印客户端连接状态
    while True:
        data = sock.recv(1024) #接受客户端发送的数据
        if data.decode()=='exit': #如果客户端发送‘exit’，则退出
            break
        else:
            print("Recevie message from client" ,count ,":",data.decode()) #打印从客户端接收到的数据
            sock.sendall(data[::-1]) #向客户端发送接收到的字符串的逆序
    print ("close client%s connection." % count) #打印关闭客户端连接状态
    sock.close() #关闭客户端连接

while 1:
    sock, addr = s.accept() #接受客户端连接
    count=count+1
    #多线程
    trd = threading.Thread(target=mutilclient, args=(sock,count)) #调用自定义的mutilclient函数，并传递sock对象，参数count
    trd.start()

s.close() #关闭连接