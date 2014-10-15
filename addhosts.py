

##Script , it will require zabbix_api module &   zabbix admin user/password
 
 
#!/usr/bin/python
 
 
 
 
import sys
from getpass import getpass
import zabbix_api
 
 
username = raw_input('Username: ')
password = getpass()
 
 
def create_group(group):
    """Function that will create host group on Zabbix Server."""
    result = zapi.hostgroup.create({ 'name' : group })
    try:
        result['groupids']
    except NameError:
        """API throws an exception if such group already exists"""
        print 'There was na error while creating group'
 
    print 'Group "'+ group +'" has been created with id: '+ \
            result['groupids'][0]
    return result['groupids'][0]
 
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
        print 'There was na error while creating host'
    print 'Host "'+ host +'" has been created with id: '+ \
        result['hostids'][0]
    return result['hostids'][0]
 
def test_API_version():
    """Method to check if server has compatible version of API."""
    if zapi.api_version() <= 1.4:
        raise Exception('Example script works only with API 1.4 or higher.')
 
 
zapi = zabbix_api.ZabbixAPI("http://10.0.0.12/zabbix")
zapi.login(username, password)
 
test_API_version()
#groupid = create_group('Linux servers')
for b in  open("file.txt"):
 a=b.split()
 h=a[0]
 i=a[1]
 hostid = create_host(h,i,'2','10001')
