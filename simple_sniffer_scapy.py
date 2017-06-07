# Run tis code as root, scapy needs to be installed
#!/usr/bin/python
from scapy.all import *

def display(pkt):
        pkt.show()

sniff(prn = display)

# In prn different type of function can be passed, that acts accordingly

