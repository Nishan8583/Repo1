'''THis script must be run in the windows with python2.7 installed
comments are placed there to help understand the written function as well the function of the _winreg module
if not clear please usse the help() function or refer to the book Violent Python, from which this code was learned from'''
from _winreg import *

def value2addr(value):
    addr = ''
    for ch in value:
        addr = addr + ("%02x "%ord(ch))  # ord(ch) wiil get ascii value of a string and "%02x " will give the two byte hexadecimal value
    addr = addr.strip(' ').replace(' ',':')[0:17]  # replacing the spaces with : and getting only the frist 18th value
    return addr

def check():
    net = 'SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged'  # this will be the subkey
    key = OpenKey(HKEY_LOCAL_MACHINE,net)  # opens the key

    for i in range(100):  # We are using the loop, helps in case don't know the number of subkeys
        try:
            guid = EnumKey(key,i)  # Reutrns the name of subkey, if present else an error is thrown, useful if dont know the number of keys
            netKey = OpenKey(key,str(guid))  # NOw opening the subkey

            (n,addr,type) = EnumValue(netKey,5)  # Returns a tupe of name of key, data in key and type of key, 5 is the index
                                                    # FIfthe has the default gateway
            (n,name,type) = EnumValue(netKey,4)  # Fourth is the mac address

            mac = value2addr(addr)
            net_name = str(name)

            print "[+]Success in getting info\nNAME= {}     MAC_ADDRESS= {}\n".format(net_name,mac)
        except:
            break

if __name__ == '__main__':
    check()
