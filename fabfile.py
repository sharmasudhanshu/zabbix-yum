## below is how to use a pem file , for aws remote login ,if you have ppk file convert it in ti pem file
### like  this ::  puttygen /home/anshu/snw-app-key.ppk -O private-openssh -o snw-app-key.pem

### your server & pem file for puppetmaster will differ , so change env.host & env.key_filename according 

env.hosts = ["ubuntu@54.169.19.59"]
env.key_filename = '/root/zabbix_aws_new.pem'



def pupmaster():
    sudo("echo 'node \"ip-172-31-31-124\" {\n class { \"zabbixagentt\":\n servers  => \"172.31.31.124\",\nsa => \"172.31.31.124\",\nhostname => \"Switchnwalk-prod1\"\n}\nyumrepo { \"zabbix2.4\":\nbaseurl => \"http://repo.zabbix.com/zabbix/2.4/rhel/6/x86_64/\",\ndescr => \"myzabbix2.4\",\nenabled => 1,\ngpgcheck => 0,\n}\n}' >> /etc/puppet/manifests/nodes.pp")    
    sudo('service puppetmaster restart')


def pupagent(server="ip-172-31-1-5.ap-southeast-1.compute.internal"):  
    """Configure slaves [server], default: puppetmaster.local"""
    sudo('sudo rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm')
    sudo("yum -y install puppet")
    sudo("echo '[main]\nlogdir=/var/log/puppet\nvardir=/var/lib/puppet\nssldir=/var/lib/puppet/ssl\nrundir=/var/run/puppet\n\n[agent]\nserver = %s\nreport = true\npluginsync = true\ncertname = ip-172-31-31-124' > /etc/puppet/puppet.conf" % server) 

	## in above line , give certname same as dns names of puppet agent

 #   sudo('sed s/START=no/START=yes/ /etc/default/puppet > /tmp/puppi')
 #   sudo('mv /tmp/puppi /etc/default/puppet')
    sudo('service puppet restart')
    sudo('puppet agent -t')
    
    
  ###################
  apt-get puppet agent ,
  
  def pup(server="pmaster"):
    """Configure slaves [server], default: puppetmaster.local"""
    sudo('wget https://apt.puppetlabs.com/puppetlabs-release-precise.deb')
    sudo('sudo dpkg -i puppetlabs-release-precise.deb')
    sudo('sudo apt-get update')
    sudo("apt-get update")
    sudo("apt-get -y install puppet")
    sudo("echo '[main]\nlogdir=/var/log/puppet\nvardir=/var/lib/puppet\nssldir=/var/lib/puppet/ssl\nrundir=/var/run/puppet\nfactpath=$vardir/lib/facter\n\n[agent]\nserver = %s\nreport = true\npluginsync = true\ncertname = controller' > /etc/puppet/puppet.conf" % server)
    sudo('sed s/START=no/START=yes/ /etc/default/puppet > /tmp/puppi')
    sudo('mv /tmp/puppi /etc/default/puppet')
    sudo('service puppet restart')
    sudo('puppet agent -t')


def clist():
    """List certificate requests"""
    sudo("puppet cert --list")
    

def csign(agent="--all"):
    """Sign certificate requests, default=all"""
    sudo("puppet cert --sign %s" % agent)
    
    
