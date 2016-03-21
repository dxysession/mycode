#!/usr/bin/env python
# coding:utf-8
# filename : backpy

import os
import time

source = ['/home/dxy/Desktop/svn']
target_dir = '/home/dxy/Desktop/svn_backup/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr %s %s" %(target,''.join(source))

if os.system(zip_command) == 0:
	print 'Successful backup'
else:
	print 'Backup Failed'

