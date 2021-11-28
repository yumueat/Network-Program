import socket
def send_file_2_client(new_client_socket,client_addr):
    file_name=new_client_socket.recv(1024).decode("utf-8")
    print("客户端 %s 要下载 %s"%(str(client_addr),file_name))
    file_content=None
    try:
        f=open('r'+file_name,"r")
        file_content=f.read()
        f.close()
    except:
        print("没有要下载的文件%s"%(file_name))

    if file_content:
        new_client_socket.send(file_content)
def main():
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.bind(("192.168.31.205",7788))
    tcp_server_socket.listen(100)
    while True:
        new_client_socket,client_addr=tcp_server_socket.accept()
        send_file_2_client(new_client_socket,client_addr)
        new_client_socket.close()
    tcp_server_socket.close()
    pass

if __name__=='__main__':
    main()