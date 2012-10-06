This contains 2 file for initial to manipulate api of ipslist.com
Do you need add your API KEY in both file.


add_ip.sh
=========
This file is to the sending notice to ipslist.com for block IP. For parameter receives ip

Example:
/path/add_ip.sh 190.x.x.x

You can use this blocking by fail2ban. On actionban configuration on /etc/fail2ban/iptables*.conf

Example configuration on fail2ban
actionban = iptables -I fail2ban-<name> 1 -s <ip> -j DROP | /root/add_ip.sh <ip> 


get_list.py
===========
Get list from ipslist.com and banned by chains of iptables on system.

You can configure this script on crontab on your system

# m h  dom mon dow   command
   0-59/10  *  *   *   *   /path/get_list.py
 
