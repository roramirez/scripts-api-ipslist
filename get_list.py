#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
  Get data from ipslist.com
"""
#http request
import urllib

#parser xml
from xml.dom import minidom

import os, sys

sys.path.insert(1, "/sbin")

key = 'ADD YOUR API KEY HERE'
url_api = 'http://ipslist.com/api'

#command iptables
#iptables_allow = 'iptables -D ipslist  -s %s -j DROP'
iptables_allow = 'iptables -I ipslist 1 -s %s -j ACCEPT'
iptables_deny  = 'iptables -I ipslist 1 -s %s -j REJECT'


def get_list_xml(url):

    dom = minidom.parse(urllib.urlopen(url))

    ips = []
    for node in dom.getElementsByTagName('ip'):
        ips.append({
            'ip': node.getElementsByTagName('address')[0].firstChild.data,
            'status': node.getElementsByTagName('status')[0].firstChild.data
        });

    return ips

def iptables(ips):
    #Create chains

    os.popen('iptables -F ipslist')
    os.popen('iptables -X ipslist')

    os.popen('iptables -N ipslist')
    
    for ip in ips:
        if ip['status'] == 'allow':
          os.popen(iptables_allow % ip['ip'])
        elif ip['status'] == 'deny':
          os.popen(iptables_deny % ip['ip'])
  
    os.popen('iptables -A ipslist -j RETURN')
    os.popen('iptables -D INPUT -j ipslist')
    os.popen('iptables -I INPUT -j ipslist')


if __name__ == "__main__":
 
    method = 'list'
    format = 'xml'
    url = url_api + '/' + key + '/' + method + '.' + format
    print url 
        
    ips = get_list_xml(url)
    
    if ips: 
      iptables(ips)
