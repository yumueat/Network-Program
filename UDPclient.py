import socket

def send_msg(udp_socket):
    dest_ip=input("请输入对方ip:")
    dest_port=int(input("请输入对方的端口:"))
    send_data=input("你想说啥:")
    udp_socket.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))

def recv_msg(udp_socket):
    recv_data=udp_socket.recvfrom(1024)
    print("%s 说了 %s"%(str(recv_data[1]),recv_data[0].decode("utf-8")))

def main():
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",7789))
    while True:
        recv_msg(udp_socket)
        send_msg(udp_socket)

    pass

if __name__=='__main__':
    main()