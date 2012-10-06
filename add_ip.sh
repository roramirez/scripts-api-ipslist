#!/bin/sh
CURL=/usr/bin/curl
KEY='ADD YOUR KEY HERE'
IP=$1

$CURL http://www.ipslist.com/api/add/$KEY/$IP

