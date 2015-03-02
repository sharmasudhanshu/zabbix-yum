#!/usr/bin/python3.4



import sys
from getpass import getpass
import zabbix_api


username = input('Username: ')
password = getpass()


def create_host(host,ip,gid,tid):
    """Function that will create host on Zabbix Server."""
    result = zapi.host.create({ "host" : (host),
        "interfaces" : [{
            "type": 1,
            "main": 1,
            "useip" : 1,
            "ip" : (ip),
            "dns" : "",
            "port" : "10050",
            }],
        "groups" : [{
            "groupid" : (gid),
            }],
         "templates": [{
         "templateid": (tid),
            }],
        })
    try:
        result['hostids']
    except NameError:
        """API throws an exception if such host already exists"""
        print ('There was na error while creating host')
    print ('Host "'+ host +'" has been created with id: '+ \
        result['hostids'][0])
    return result['hostids'][0]




zapi = zabbix_api.ZabbixAPI("http://10.0.0.92/zabbix")
zapi.login(username, password)

#test_API_version()
#groupid = create_group('Linux servers')
for b in  open("file.txt"):
 a=b.split()
 h=a[0]
 i=a[1]
 hostid = create_host(h,i,'2','10001')
 ##hostid = create_host(h,i,'2','10081')  ## for windows  make if for linux/windows
 
#####################################################################################################################

 
 
