#!/usr/bin/env python
import pexpect
import sys,time,getpass
from pexpect import pxssh

timestr = time.strftime("%m%d%Y-%H")
txt =".txt"

f=open('avere_connect.txt', 'r')
content = f.read().split("\n")
hostname = (content[0])
username = (content[1])
password = (content[2])
print str(hostname)
f.close()

#hostname = raw_input('hostname: ')
#username = raw_input('username: ')
#password = getpass.getpass('password: ')

s = pxssh.pxssh()
if not s.login(hostname, username, password):

    print "SSH session failed on login."
    print str(s)
else:
    print "SSH session login successful"
   # s.sendline ('uptime')
   # s.sendline ('for VSERVER in `averecmd vserver.list`; do for POLICY in `averecmd nfs.listPolicies $VSERVER`; do echo "vserver: $VSERVER";echo "Policy: $POLICY"; averecmd --pretty nfs.listRules $VSERVER $POLICY|egrep filter;echo;done;done')
    print "Before file"
    content = s.sendline ('name_mapping.py --exports')
    if content:

        s.prompt()
        f =open("MTA_AVERE_EXPORT_OP.txt","w")
        f.write(str(s.before))
        f.close()
        print(s.before)
        # print everything before the prompt.
        s.logout()
    else:
        print "Nothing retrived"


   # sys.stdout=open("/mappings/Infra_midstor_DeviceMetaInfo_NAS_PROD01/Avere_NFS_EXPORT_Output/Do_Not_Delete/MTA/MTA_AVERE_Name_Mapping_OP_" + timestr + txt ,"w")
    
    



#sys.stdout.close()