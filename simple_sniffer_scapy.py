# Run tis code as root, scapy needs to be installed
#!/usr/bin/python
from scapy.all import *
limit = 2500
var = 0
ip_list = {}
def display(pkt):
        pkt.show()

def filter(pkt):
        if pkt.getlayer(IP).src == "127.0.0.1":
                print "local IP"

def check_DDOS(pkt):
        source = pkt.getlayer(IP).src
        if source not in ip_list:
                ip_list[source] = 1
        else:
                ip_list[source] = ip_list[source] + 1

        for source,number in ip_list.items():
                if number > limit:
                        print "[*] WARNING TOO MANY PACKET FROM {} [*]".format(source)
                        return
                else:
                        pkt.show()
sniff(prn = check_DDOS)


# In prn different type of function can be passed, that acts accordingly

