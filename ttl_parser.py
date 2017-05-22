#!/usr/bin/python
#The script has to be run as root and only works in python2   
from scapy.all import *

threshhold = 5
def ttl_parser(pkt):
        if pkt.haslayer(IP):
                packet = pkt.getlayer(IP)
                src = packet.src  # The src address of the IP packet
                ttl = str(packet.ttl)  # The time-to-live of the packet
                print "TTL: {}".format(ttl)
                result = re.findall(r'127.\d.\d.\d|10.\d.\d.\d|172.16.\d.\d|172.31.\d.\d',str(src))  # using regular expressions to exclude pri$

                if len(result) > 0:
                        print "Private IP "
                        return

                print result
                print "Source: {} ttl: {} ".format(src,ttl)

                response = sr1(IP(dst = src)/ICMP(),retry = 0,timeout = 1)  # Sending ICMP packet to the source address of the previous packet
                if "None" in str((type(response))):  # If no response was recieved
                        print "NO response"
                        return
                new_ttl = response.getlayer(IP).ttl  # So if the ttl for us to reach the destination and the ttl packet recieved was found to b$
                if(int(ttl) - int(new_ttl)) > threshhold:
                        print "SPOOFING"
sniff(prn = ttl_parser)
