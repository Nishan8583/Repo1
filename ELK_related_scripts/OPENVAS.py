import json
import time
import codecs
import struct
import locale
import glob
import sys
import getopt
import xml.etree.ElementTree as xml
import re
from elasticsearch import Elasticsearch
from datetime import datetime
class OpenVasES:
        "This class will parse an OpenVAS XML file and send it to Elasticsearch"

        def __init__(self, input_file,es_ip,es_port,index_name):
                self.input_file = input_file
                self.displayInputFileName()
                self.tree = self.__importXML()
                self.root = self.tree.getroot()
                self.issueList = self.__createIssuesList()
                self.portList = self.__createPortsList()
                self.es = Elasticsearch([{'host':es_ip,'port':es_port}])
                self.index_name = index_name

        def displayInputFileName(self):
                print self.input_file

        def __importXML(self):
                #Parse XML directly from the file path
                self.displayInputFileName()
                return xml.parse(self.input_file)
                self.displayInputFileName()

        def __createIssuesList(self):
                "Returns a list of dictionaries for each issue in the report"
                issuesList = [];
                for result in self.root.iter('result'):
                        issueDict = {};
                        issueDict['scanner'] = 'openvas'
                        issueDict['@timestamp'] = datetime.now().isoformat()
                        if result.find('host') is not None:
                                issueDict['ip'] = unicode(result.find('host').text)
                                #print issueDict['host']
                        for nvt in result.iter('nvt'):
                                issueDict['oid'] = unicode(nvt.attrib['oid'])
                                for child in nvt:
                                        issueDict[child.tag] = unicode(child.text)

                        if result.find('description') is not None:
                                issueDict['description'] = unicode(result.find('description').text)
                        if result.find('port') is not None:
                                issueDict['port'] = unicode(result.find('port').text)
                        if result.find('threat') is not None:
                                issueDict['threat'] = unicode(result.find('threat').text)
                        if result.find('severity') is not None:
                                issueDict['severity'] = unicode(result.find('severity').text)
                        if result.find('scan_nvt_version') is not None:
                            issueDict['scan_nvt_version'] = unicode(result.find('scan_nvt_version').text)
                        if issueDict:
                                issuesList.append(issueDict)

                #for x in issuesList:
                #       print x['description']
                return issuesList



        def __createPortsList(self):
                "Returns a list of dictionaries for each ports in the report"
                portsList = [];
                for p in self.root.iter('ports'):
                        for port in p:
                                portDict = {};
                                portDict['scanner'] = 'openvas'
                                if port.text != 'general/tcp':
                                        d = self.parsePort(port.text)
                                        #print d['service']
                                        if port.find('host') is not None: portDict['ip'] = port.find('host').text
                                        if d != None:
                                                portDict['service'] = d['service']
                                                portDict['port'] = d['port']
                                                portDict['protocol'] = d['protocol']
                                                portsList.append(portDict)



                return portsList

        def parsePort(self,string):
                fieldsDict={};
                portsParsed = re.search(r'(\S*\b)\s\((\d+)\/(\w+)',string)
                #portsParsed = re.search('(\S*)\s\((\d+)\/(\w+)',string)
                #print string
                if portsParsed:
                        fieldsDict['service'] = unicode(portsParsed.group(1))
                        fieldsDict['port'] = unicode(portsParsed.group(2))
                        fieldsDict['protocol'] = unicode(portsParsed.group(3))
                        #print fieldsDict
                        return fieldsDict
                return None


        def toES(self):
                for item in self.issueList:
                        try:
                                self.es.create(index=self.index_name,doc_type="vuln", body=json.dumps(item))
                        except:
                                self.es.index(index=self.index_name,doc_type="vuln", body=json.dumps(item))
                for port in self.portList:
                        try:
                                self.es.create(index=self.index_name,doc_type="vuln", body=json.dumps(port))
                        except:
                                self.es.index(index=self.index_name,doc_type="vuln", body=json.dumps(port))


