#!/usr/bin/env python

import xmlrpclib
import sys
import commands 
SATELLITE_URL = (sys.argv[1])
SATELLITE_LOGIN = "batch"
SATELLITE_PASSWORD = "st1ngray"

client = xmlrpclib.Server(SATELLITE_URL, verbose=0)
key = client.auth.login(SATELLITE_LOGIN, SATELLITE_PASSWORD)
list = client.system.listSystems(key)
cmd = 'echo '+SATELLITE_URL+' | sed -e \'s%.*\/\/%%g\' -e \'s%\..*%%g\''
sathost = commands.getoutput(cmd)

for group in list:
    sysname = group.get('name')
    sysid =  group.get('id')
    details = client.system.getDetails(key, sysid)
    guestrelease = details.get('release')
    osastat = details.get('osa_status')
    virt = details.get('virtualization')
    print '{0},{2}, ,{4},Linux,{5},{3}, ,' .format (sysname, sysid, virt, sathost, guestrelease, osastat)


client.auth.logout(key)
