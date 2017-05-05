#!/usr/bin/python
import zipfile, optparse
from sys import exit
from threading import Thread

def cracker(zip_file,password):
	try:
		print "[*] Trying password: ",password
		zip_file.extractall(pwd = password)
		print "[+] Success in cracking, the password seems to be: ",password
		sys.exit()
	except:
		"[-] FAILED TO CRACK THE PASSWORD\n"


def main():
	parser = optparse.OptionParser("usage%prog"+"-f <zipfile-name> -d <dictionary-file-name>")
	parser.add_option('-f', dest = "zname",type = 'string',help = 'specify zipfile name')
	parser.add_option('-d', dest = 'dname', type= 'string', help = 'specify dictionary file name')

	(options, args) = parser.parse_args()
	print options.zname,options.dname
	
	if options.zname == None or  options.dname == None:
		print "Heres the usage",parser.usage
		exit() 

	zname = options.zname
	dname = options.dname
	file = zipfile.ZipFile(zname)
	dict = open(dname,'r')
	for word in dict.readlines():
		password = word.strip('\n')
		t = Thread(target = cracker,args = (file,password))
		t.start()

if __name__ == '__main__':
	main()
