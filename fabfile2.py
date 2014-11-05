###fab file for  apt get & yum 


from fabric.api import *

# We can then specify host(s) and run the same commands across those systems

#env.host = ['10.0.0.17']

#env.hosts = ["ec2-user@54.179.150.144"]      ## puppet agent server ip & user name with sudo access
#env.user = 'ec2-user'
#env.key_filename = '/opt/test/dss-admin-key.pem'

env.hosts = ["ec2-user@54.179.149.42"]   ### puppet server keys login
env.key_filename = '/opt/test/snw-prod-as-key'

#env.hosts = ["ubuntu@54.169.19.59"]   ### puppet server keys login
#env.key_filename = '/root/zabbix_aws_new.pem'


#env.hosts = ["ec2-user@54.179.150.236"]
#env.key_filename = '/root/snw-app-key.pem'

def local_uname():
    local('sudo uname -a')

def remote_uname():
    run('sudo uname -a')
##give  server="ip-172-31-1-5.ap-southeast-1.compute.internal for puppet master
### function pup to set up a puppet client , give params carefully
def pup(server="ip-172-31-1-5.ap-southeast-1.compute.internal"):
    """Configure slaves [server], default: puppetmaster.local"""
    sudo('iptables -A INPUT -p tcp --dport 10050 -m state --state NEW,ESTABLISHED -j ACCEPT')
    sudo('iptables -A OUTPUT  -p tcp --sport 10050 -m state --state ESTABLISHED -j ACCEPT')
    sudo('iptables -I INPUT  -p tcp -m state --state NEW -m tcp --dport 10050 -j ACCEPT')
    sudo('sudo rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm')
    sudo("yum -y install puppet")
    sudo("echo '[main]\nlogdir=/var/log/puppet\nvardir=/var/lib/puppet\nssldir=/var/lib/puppet/ssl\nrundir=/var/run/puppet\n\n[agent]\nserver = %s\nreport = true\npluginsync = true\ncertname = ip-172-31-2-0' > /etc/puppet/puppet.conf" % server)
## in above line , give certname same as dns names of puppet agent

   # sudo('sed s/START=no/START=yes/ /etc/default/puppet > /tmp/puppi')
   # sudo('mv /tmp/puppi /etc/default/puppet')
    sudo('service puppet restart')
    sudo('puppet agent -t')


def pupagent_aptget(server="ip-172-31-1-5.ap-southeast-1.compute.internal"):
    """Configure slaves [server], default: puppetmaster.local"""
    sudo('iptables -A INPUT -p tcp --dport 10050 -m state --state NEW,ESTABLISHED -j ACCEPT')
    sudo('iptables -A OUTPUT  -p tcp --sport 10050 -m state --state ESTABLISHED -j ACCEPT')
    sudo('iptables -I INPUT  -p tcp -m state --state NEW -m tcp --dport 10050 -j ACCEPT')
    sudo('sudo wget https://apt.puppetlabs.com/puppetlabs-release-precise.deb')
    sudo('sudo dpkg -i puppetlabs-release-precise.deb')
    sudo('sudo apt-get update')
    sudo('sudo apt-get -y install puppet')
    sudo('sudo wget http://repo.zabbix.com/zabbix/2.4/debian/pool/main/z/zabbix-release/zabbix-release_2.4-1+wheezy_all.deb')
    sudo('sudo dpkg -i zabbix-release_2.4-1+wheezy_all.deb')
    sudo('sudo apt-get update')
    sudo('sudo apt-get install -y zabbix-agent')

   # sudo('')
    sudo("echo '[main]\nlogdir=/var/log/puppet\nvardir=/var/lib/puppet\nssldir=/var/lib/puppet/ssl\nrundir=/var/run/puppet\n\n[agent]\nserver = %s\nreport = true\npluginsync = true\ncertname = ip-172-31-4-175' > /etc/puppet/puppet.conf" % server)
## in above line , give certname same as dns names of puppet agent

    sudo('sed s/START=no/START=yes/ /etc/default/puppet > /tmp/puppi')
    sudo('mv /tmp/puppi /etc/default/puppet')
    sudo('service puppet restart')
    sudo('puppet agent -t')



def uptime():
    run("uptime")

def host_type():
    run('uname -s')

### pupm  function to update puppet master nodes.pp file
def pupm():
    sudo("echo 'node \"ip-172-31-2-0\" {\n class { \"zabbixagentt\":\n servers  => \"172.31.5.161\",\nsa => \"172.31.5.161\",\nhostname => \"snw-TomcatAS2\"\n}\nyumrepo { \"zabbix2.4\":\nbaseurl => \"http://repo.zabbix.com/zabbix/2.4/rhel/6/x86_64/\",\ndescr => \"myzabbix2.4\",\nenabled => 1,\ngpgcheck => 0,\n}\n}' >> /etc/puppet/manifests/nodes.pp")
    sudo('service puppetmaster restart')

def pupmaster_apt():
    sudo("echo 'node \"ip-172-31-4-175\" {\n class { \"zabbixagentt\":\n servers  => \"172.31.5.161\",\nsa => \"172.31.5.161\",\nhostname => \"snw-httpd2\"\n}\n}'>> /etc/puppet/manifests/nodes.pp")
    sudo('service puppetmaster restart')


