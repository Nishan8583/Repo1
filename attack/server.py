import socket

def attack():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind(('127.0.0.1',50000))
    print("Binding successful, now listening for connections")
    s.listen(1)
    client,addr = s.accept()
    while True:
        msg = input('enter something to send: ')
        client.send(msg.encode('utf-8'))
        msg = client.recv(4098)
        print(msg.decode('utf-8'))

    
if __name__ == '__main__':
    attack()


