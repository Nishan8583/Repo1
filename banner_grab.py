'''The code is imilar to tcp_full_scan.py, except for we send and recieve some info'''
#!/usr/bin/python
import socket,optparse
from sys import exit

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

'''main() handles arguments and calls specific scanner as necessary'''
def main():
	parser = optparse.OptionParser("USAGE: -i <ip address> -p <port scanner>")
	parser.add_option('-i',type = 'string',dest = 'target_ip',help = 'specifys ip')
	parser.add_option('-p',type = 'int',dest = 'target_port',help = 'specifys port')
	(options,args) = parser.parse_args()

	target_ip = options.target_ip
	target_port = options.target_port

	if target_ip == None:
		print parser.usage
		exit()
	elif target_ip != None and target_port == None:
		range_scan(target_ip)
	else:
		specific_scan(target_ip,target_port)

'''FOr when want to scan a specific port'''
def specific_scan(ip,port):
	try:
		s.connect((ip,port))
		print "Target {} has port {} open\n trying to get some info".format(ip,port)
    s.send("GIve Me SoMe")
    print "The host replied: "s.recv(100)
	except:
		print "target {} does not have port {} open".format(ip,port)


'''Scanning a range of ports'''	
def range_scan(ip):
	for port in range(0,65535):
		try:
			s.connect((ip,port))
			print "Target {} has port {} open".format(ip,port)
      print "Target {} has port {} open\n trying to get some info".format(ip,port)
      s.send("GIve Me SoMe")
      print "The host replied: "s.recv(100)
    except:
      print "target {} does not have port {} open".format(ip,port)
if __name__ == '__main__':
	main()
