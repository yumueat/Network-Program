import socket
def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='192.168.31.205'
    port=9999
    s.connect((host,port))

    while True:
        data_recv=s.recv(1024*1024)
        print(data_recv.decode("utf-8"))
        msg=input("请输入:")
        if msg=='out':
            break
        s.send(msg.encode("utf-8"))
    s.close()

    pass

if __name__=='__main__':
    main()
'''import socket
def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='192.168.31.205'
    port=12345
    s.connect((host,port))

    while True:
        data_recv=s.recv(1024)
        print(data_recv.decode("utf-8"))
        msg=input("send msg:")
        s.send(msg.encode("utf-8"))
    s.close()

    pass

if __name__=='__main__':
    main()'''