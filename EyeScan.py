#!/usr/bin/python


from socket import *
import optparse
from threading import *


def Scan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print("tcp open", tgtPort)
    except:
        print("tcp closed", tgtPort)
    finally:
        sock.close()


def portScan(Host, Ports):
    try:
        tgtIP = gethostbyname(Host)
    except:
        print("Unkown Host or can't resolve this Ip ", Host)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("Scan Results for : " + tgtIP)
    except:
        print(" Scan Resultss for " + tgtName[0])
    setdefaulttimeout(1)
    for port in Ports:
        t = Thread(target=Scan, args=(tgtHost, int(port)))
        t.start()


def main():
    parser = optparse.OptionParser('Usage of program : ' + '-H <target host> -P <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-P', dest='tgtPort', type='string', help='specify target ports seperated by comma')
    (options, args) = parser.parse_args()
    Host = options.tgtHost
    Ports = str(options.tgtPort).split(',')
    if (Host == None) | (Ports[0] == None):
        print(parser.usage)
        exit(0)
    portScan(Host, Ports)


if __name__ == '__main__':
    main()
