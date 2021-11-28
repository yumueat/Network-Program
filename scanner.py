import  socket
from optparse import OptionParser

def open(ip,host):
    s=socket.socket()
    try:
        s.connect((ip,host))
        return  True
    except:
        return False

def scan(ip,port):
    for x in port:
        if open(ip,x):
            print("%s host %s port open"%(ip,x))
        else:
            print("%s host %s port close" % (ip, x))

def rscan(ip,s,e):
    for x in range(s,e+1):
        if open(ip,x):
            print("%s host %s port open"%(ip,x))
        else:
            print("%s host %s port close" % (ip, x))

def main():
    usage="usage:xxx.py -i ip地址 -p 端口"
    parse=OptionParser(usage=usage)
    parse.add_option("-i","--ip",type="string",dest="ipaddress",help="your target ip here")
    parse.add_option("-p","--port",type="string",dest="port",help="your target port here")
    (options,args)=parse.parse_args()

    ip=options.ipaddress
    port=options.port
    defaultport=[135,139,445,3306,3389,5944]

    if ',' in port:
        port=port.split(',')
        a=[]
        for x in port:
            a.append(int(x))
        scan(ip,a)
    elif '-' in port:
        port=port.split('-')
        s=int(port[0])
        e=int(port[1])
        rscan(ip,s,e)
    elif 'all' in port:
        rscan(ip,1,65335)
    elif 'default' in port:
        scan(ip,defaultport)
    pass


'''
import sys,socket

def open(ip,port):
    s=socket.socket()
    try:
        s.connect((ip,port))
        return  True
    except:
        return False

def scan(ip,portlist):
    for x in portlist:
        if open(ip,x):
            print("%s host %s port open"%(ip,x))
        else:
            print("%s host %s port close"%(ip,x))

def rscan(ip,s,e):
    for x in range(s,e):
        if open(ip,x):
            print("%s host %s port open"%(ip,x))
        else:
            print("%s host %s port close" % (ip, x))
def main():
    defaultport=[135,139,445,1433,3306,3389,5944]

    str=sys.argv[1]
    if len(sys.argv)==2:
        if str[0]=='-':
            option = sys.argv[1][1:]
            if option == 'version':
                print("软件版本是1.0")
            elif option=='help':
                print("python xxx.py [ip] [port:80,99,89 or 80-99]")
            sys.exit()
        scan(sys.argv[1],defaultport)
    elif len(sys.argv)==3:
        if ',' in sys.argv[2]:
            p=sys.argv[2]
            p=p.split(',')
            a=[]
            for x in p:
                a.append(int(x))
            scan(sys.argv[1],a)
        elif '-' in sys.argv[2]:
            a=sys.argv[2]
            a=a.split('-')
            s=int(a[0])
            e=int(a[1])
            rscan(sys.argv[1],s,e)

    pass

'''
if __name__=='__main__':
    main()