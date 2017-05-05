#!/usr/bin/python
'''THIS CODE HAS BEEN LEARNED FROM THE BOOK VIOLENT PYTHON'''
import crypt

def password_cracker(hash_code):
        salt = hash_code[:2]  # The first two string is the salt 
        dict_file = open("dict.txt",'r')  # opening the file containg the list of possible passwords

        for line in dict_file.readlines():
                password = line.strip('\n')
                hash = crypt.crypt(password,salt)  # crypt() function geenrates a has

                if (hash == hash_code):
                        print "         [+] Success cracking, Password:  {}".format(password)
                        return
        print "         [-] FAiLURE TO CRACK"
def main():
        pass_file = open("password.txt",'r')
        for line in pass_file.readlines():
                if ":" in line:
                        user = line.split(":")[0]
                        hash = line.split(":")[1].strip(' ').strip('\n')
                        print "[*] Trying for USER: {}",format(user)
                        password_cracker(hash)
                else:
                        print "Not a VALID file"

if __name__ == '__main__':
        main()
