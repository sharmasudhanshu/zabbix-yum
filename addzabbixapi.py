
first add pip & moudles

pip install  zabbix-api  ### giving below error
ImportError: cannot import name IncompleteRead

apt-get install python3-setuptools
easy_install3 -U pip    ### to install latest  pip 
root@zabbixs:/opt# pip
pip     pip2    pip3    pip3.4   ### now  you will see many pip's

root@zabbixs:/opt# pip3.4 install zabbix-api   ##use latest pip for installtions
Collecting zabbix-api
  Downloading zabbix-api-0.4.tar.gz
Installing collected packages: zabbix-api
  Running setup.py install for zabbix-api
Successfully installed zabbix-api-0.4


& use   #!/usr/bin/python3.4  in script to run code

### now use below scripts

#!/usr/bin/python3.4

###########use  pythin 3.4 & pip3.4 for zabbix api install & run programms
import sys
from getpass import getpass
import zabbix_api


username = input('Username: ')
password = getpass()





#def test_API_version():
#    """Method to check if server has compatible version of API."""
#    if zapi.api_version() <= 1.4:
 #       raise Exception('Example script works only with API 1.4 or higher.')


zapi = zabbix_api.ZabbixAPI("http://10.0.0.92/zabbix")
zapi.login(username, password)


#for host in zapi.host.get({"filter":{"host":"Linux server"}, "output":"extend"}):
    #print (host)
#template="Template App FTP Service"

template="Template App MySQL"
get = zapi.template.get({
            "output": "extend",
            "filter": {
                "host": [template]
            }
        })
result = get[0]['templateid']

print (result)



key='jgite.ume'
#zapi.item.create({ 'hostid' : (result),'key_' : key })
name='anshu'
interfaceid='0'
zapi.item.create({ 'name' : name,
                                  'description' : 'description',
                                  'key_' : key,
                                  'type' : 0, # Zabbix agent
                                  'value_type': 0, # numeric float
                                  'hostid' : result,
                                  'delay' : 30,
                                  })


zapi.template.massadd({"templates": [{ "templateid": result}] , "hosts": [{"hostid": "10116"} ] })
zapi.template.massadd({"templates": [{ "templateid": result}] , "groups": [{"groupid": "11"} ] })  ##mass add by groupid's
zapi.trigger.create({ 'host' : '10073' , 'description' : 'added  for  test', 'status' : 0 , 'type' : 0 ,'priority' : 3 , 'expression' : '{Template App MySQL:jgite.ume.last(0)}=0'})
#test_API_version()
#groupid = create_group('Linux servers')
for b in  open("file.txt"):
 a=b.split()
 h=a[0]
 i=a[1]
# hostid = create_host(h,i,'2','10001')
