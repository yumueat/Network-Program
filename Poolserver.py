import os,time
from socket import *
from multiprocessing import Pool,Process

server=socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.listen(5)

def talk(conn,addr):
    print("进程 %s 用户 %s"%(os.getpid(),addr))
    while True:
        try:
            msg=conn.recv(1024)
            if not msg:break
            conn.send(msg.upper())
        except Exception:
            break

def main():
    p=Pool(4)
    while True:
        conn,addr=server.accept()
        p.apply_async(talk,args=(conn,addr,))

    pass


if __name__=='__main__':
    main()