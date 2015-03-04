While making syslog input configuration make sure that  $InputFileStateFile  is unique , otherwise  logger will not work,

Refer below examples , for 3 different files we have 3 state files.

 

$InputFileStateFile state-10-tomcat-tsnwdsscatalin_debug

$InputFileStateFile state-10-tomcat-consoleabcd_debug

$InputFileStateFile state-10-tomcat-consoleauth_debug

 

 

 

Snw Server:   source for logs

 

 

root@SNWAPPUBPEPROD01:~# cat /opt/rsyslogbackup/rsyslog.conf

$ModLoad imuxsock # provides support for local system logging

$ModLoad imklog   # provides kernel logging support

$ActionFileDefaultTemplate RSYSLOG_TraditionalFileFormat

$RepeatedMsgReduction on

$FileOwner syslog

$FileGroup adm

$FileCreateMode 0640

$DirCreateMode 0755

$Umask 0022

$PrivDropToUser syslog

$PrivDropToGroup syslog

$WorkDirectory /var/spool/rsyslog

$IncludeConfig /etc/rsyslog.d/*.conf

*.* @@10.135.63.208:10514               ### this is for tcp connection ,   for  udp     *.* @10.135.60.35:514;RemoteLog,open iptables & ACCESS & SECURITY rules in horizon

 

 

 

 

 

cat /opt/rsyslogbackup/20-tomcatlogs.conf_orig_4mar2015

$ModLoad imfile

 

$InputFileName  /var/log/tomcatsnwdsscatalina.log

$InputFileTag 10.15.81.210.snw-dss-catalina

$InputFileStateFile state-10-tomcat-tsnwdsscatalin_debug

$InputFileSeverity INFO

$InputFileFacility LOCAL6

$InputFilePollInterval 10

$InputRunFileMonitor

 

$InputFileName  /usrdata/logs/tomcatlogs/snw-dss-catalina.log

$InputFileTag 10.15.81.210.snw-dss-catalina

$InputFileStateFile state-10-tomcat-consoleabcd_debug

$InputFileSeverity INFO

$InputFileFacility LOCAL6

$InputFilePollInterval 10

$InputRunFileMonitor

 

$InputFileName  /usrdata/logs/tomcatlogs/localhost_access_log.2015-03-04.logs

$InputFileTag 10.15.81.210.localhost_access_log

$InputFileStateFile state-10-tomcat-consoleauth_debug

$InputFileSeverity INFO

$InputFileFacility LOCAL6

$InputFilePollInterval 10

$InputRunFileMonitor

 

 

 

 

 

 

 

 

 

####################################################################################################################
zabbix server  ###  syslog server,

 

root@zabbix-server:/opt/rsyslogbackup# cat rsyslog.conf

$ModLoad imuxsock # provides support for local system logging

$ModLoad imklog   # provides kernel logging support

$ModLoad imtcp

$InputTCPServerRun 10514

$ActionFileDefaultTemplate RSYSLOG_TraditionalFileFormat

$template FILENAME,"/var/log/%fromhost-ip%/auth.log.log"

*.* ?FILENAME

$FileOwner syslog

$FileGroup adm

$FileCreateMode 0640

$DirCreateMode 0755

$Umask 0022

$PrivDropToUser syslog

$PrivDropToGroup syslog

$WorkDirectory /var/spool/rsyslog

$IncludeConfig /etc/rsyslog.d/*.conf
