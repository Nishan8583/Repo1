#!/usr/bin/python

from threading import Semaphore
from functools import partial
from os import system
from time import sleep
from openvas_lib import VulnscanManager, VulnscanException
import sys
from OPENVAS import OpenVasES
from datetime import datetime
from elasticsearch import Elasticsearch
__author__ = "Nishan Maharjan"

print
'''
_________________***************************__________________

                WELCOME TO RIGO OPENVAS SCANNER

                                        Author:{}
________________****************************_________________
\n\n
'''.format(__author__)

def my_print_status(i):
    print(str(i))

def my_launch_scanner():

        sem = Semaphore(0)

        # Configure
        try:
                manager = VulnscanManager("127.0.0.1", "nishan", "e6cded22-43a3-4ca5-967f-5b3bf7eff4ce", 9390, 5)
                print "Connection successful"
        except:
                print "Connection failed"
                sys.exit(-1)
        # Launch
        try:
                scan_id, task_id = manager.launch_scan(target = "127.0.0.1", profile = "Full and fast", callback_end = partial(lambda x: x.release(), sem),callback_progress = my_print_status)
                print "Scan ID is : {}\n".format(t)
                print "Task Created Successfull"
        except:
                print "Task Creation Unsuccessfull"
        # Wait
        sem.acquire()

        # Finished scan
        print("finished")
        id = manager.get_report_id(scan_id)
        command = "omp -u nishan -w e6cded22-43a3-4ca5-967f-5b3bf7eff4ce -R {} > /home/nishan/logs/log.xml".format(id)
        system(command)
        sleep(2)
        now = datetime.now()
        index = "openvas-{}.{}.{}".format(now.year,now.month,now.day)

        np = OpenVasES('/home/nishan/logs/log.xml','10.10.66.66','9200',index)
        np.toES()


my_launch_scanner()
