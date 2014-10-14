zabbix-yum
==========

install zabbix agent with puppet , control server,serveractive,hostname with puppet

file puppet_init.pp will allow to install zabbix agent on Redhat,centos, ubuntu ,
here you can also set zabbix agent parameters  servers,serveractive  & hostname,

keep this file on puppetmaster under path /etc/puppet/modules/zabbixagentt/manifests  by name init.pp & use it as module zabbixagentt


file  nodes.pp  will allow to control zabbix agent version to 2.4 , as above file puppet_init.pp(init.pp) holds 
condition   require => Yumrepo[ "zabbix2.4" ],
also this file contains complete sample for a node configuration , to instal/update a zabbix agent .

