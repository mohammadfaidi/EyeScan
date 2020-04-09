#!/usr/bin/python

from socket import *
import optparse
from threading import *


def connScan(tgtHost , tgtPort):
	try:
		sock = socket(AF_INET , SOCK_STREAM)
		sock.connect((tgtHost,tgtPort))
		print("tcp open", tgtPort)
	except:
		print("tcp closed", tgtPort)
	
	finally:
		sock.close()

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print("Unkown Host or can't resolve this Ip " , tgtHost)

	try:
		tgtName = gethostbyaddr(tgtIP)
		print("Scan Results for : " + tgtIP)
	except:
		print(" Scan Resultss for " + tgtName[0])
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()
	
def main():
	parser = optparse.OptionParser('Usage of program : ' + '-H <target host> -P <target port>')
	parser.add_option('-H', dest='tgtHost' , type='string' , help='specify target host')
	parser.add_option('-P', dest='tgtPort' , type ='string' , help='specify target ports seperated by comma')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print(parser.usage)
		exit(0)
	portScan(tgtHost,tgtPorts)








if __name__ == '__main__':
	main()
