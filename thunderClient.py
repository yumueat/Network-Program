import socket
def main():
   tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   dest_ip=input("从哪个服务器下载：")
   dest_port=int(input("请输入下载的端口:"))
   tcp_socket.connect((dest_ip,dest_port))

   down_file_name=input("请输入要下载的文件名:")
   tcp_socket.send(down_file_name.encode("utf-8"))
   recv_data=tcp_socket.recv(1024*1024)
   with open("new_"+down_file_name,"wb") as f:
       f.write(recv_data)
   tcp_socket.close()
   pass

if __name__=='__main__':
    main()