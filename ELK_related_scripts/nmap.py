#!/usr/bin/env python
'''Need to create logstash script that parses json, script may have to be tested first'''
import nmap # import nmap.py module
import json,time
from sdaemon import Daemon

def scanner():
  nm = nmap.PortScanner() # instantiate nmap.PortScanner object
  nm.scan('10.10.66.0/24', arguments='-sn') # scan host host, ports from 22 to 443
  # a more usefull example :
  d = {}
  file = open("/var/log/result.json","a")
  for host in nm.all_hosts():
          d['ip'] = host # get one hostname for host host, usualy the user record
          # [{'name':'hostname1', 'type':'PTR'}, {'name':'hostname2', 'type':'user'}]
          d['state'] = nm[host].state() # get state of host host (up|down|unknown|skipped)
          d['tcp_ports'] =nm[host].all_tcp() # get all ports for tcp protocol (sorted version)
          d['udp_ports'] = nm[host].all_udp() # get all ports for udp protocol (sorted version)
          print d
          json.dump(d,file,separators=(',',':'))
          file.write('\n')
          d = {}

class MyDaemon(Daemon):
        def run(self):
                while True:
                        scanner()
                         time.slee()

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
