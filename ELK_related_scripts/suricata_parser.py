#!/usr/bin/python
import time
import subprocess
import select
from elasticsearch import Elasticsearch
import json
import datetime
import sys
from sdaemon import Daemon

__author__ = "Nishan Maharjan"
def worker():
        file = open("/var/log/my_worker.log",'w')
        try:
                es = Elasticsearch("10.10.66.66:9200")  # Connecting to Elasticsearch host
                file.write("[*]Connection with ES successfull\n")
        except:
                file.write("[*]Connection with ES failed\n")
                sys.exit(-1)

        index1 = "suricata-"+str(datetime.datetime.now().year)+'.'+str(datetime.datetime.now().month)+'.'+str(datetime.datetime.now().day)  # Creating a proper index format

        f = subprocess.Popen(['tail','-F',"/var/log/suricata/eve.json"],\
                stdout=subprocess.PIPE,stderr=subprocess.PIPE)  # Reading the file in tail mode
        p = select.poll()  # polling the process
        p.register(f.stdout)  # Regfistering the standard output
        file.write("[*]tail successfull\n")
        t = str(f.stdout.readline())

        while True:
            if p.poll(1):
                t = str(f.stdout.readline())
                print t
                try:
                        es.create(index=index1,doc_type='suricata-idstype',body=json.loads(t))  # Fails if index was not created
                        file.write("Value updated successfull\n")
                except:
                        es.index(index=index1,doc_type='suricata-idstype',body=json.loads(t))
                        file.close()
                        file = open("/var/log/my_worker.log",'w')
                        file.write("Previous log was cleaned this is new day\n")

                index1 = "suricata-"+str(datetime.datetime.now().year)+'.'+str(datetime.datetime.now().month)+'.'+str(datetime.datetime.now().day)
                time.sleep(1)

class MyDaemon(Daemon):
        def run(self):
                while True:
                        worker()

if __name__ == "__main__":
        daemon = MyDaemon('/tmp/suricata_parser.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)
