node 'http-server1' {


class { 'zabbixagentt':
  servers  => '172.31.5.161', # Optional: defaults to localhost (accepts an array)
  sa => '172.31.5.161',
  hostname => 'http-server1' # Optional: defaults to the fully qualified domain name of the machine
}


yumrepo { "zabbix2.4":
baseurl => "http://repo.zabbix.com/zabbix/2.4/rhel/6/x86_64/",
descr => "myzabbix2.4",
enabled => 1,
gpgcheck => 0,
}


}
