#!/usr/bin/python
import pygeoip
import socket
dat_file = pygeoip.GeoIP("/root/GeoLiteCity.dat")  # Create a GeoIP object, the string is the path to the .dat file containing the IP to city m$
                                                   # Downloaded from http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
                                                   # Unpack the gz file "gunzip GeoLiteCity.dat.gz " and then set the path to the the file
def query(ip):
        try:
                print socket.gethostbyaddr(ip)     # Trying to get a name for the IP address
        except:
                print "NO hostname found"

        data = dat_file.record_by_name(ip)  # Get information for the IP adress, returns a dictionary
        country = data['country_name']
        city = data['city']
        long = data['longitude']
        lat = data['latitude']
        print "The source IP is located at: "
        print "country={}       city={}         longitude={}            latitude={}\n".format(str(country),str(city),str(long),str(lat))

ip_src = raw_input("Please enter the IP address: ")
query(ip_src)




