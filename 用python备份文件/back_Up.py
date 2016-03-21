#!/usr/bin/env python
# coding:utf-8
# Filename : back_Up.py

import os
import time

#基本变量
source = ["/home/dxy/Desktop/svn/"]
target_dir = "/home/dxy/Desktop/svn_backup/"

today_dir = target_dir + time.strftime('%Y%m%d')
time_dir = time.strftime("%H%M%S")

touch = today_dir + os.sep + time_dir + '.zip'
command_touch = "zip -qr " + touch + ' ' + ' '.join(source)

#逻辑思路判断
if os.path.exists(today_dir) == 0:
	os.mkdir(today_dir)
if os.system(command_touch) == 0:
	print 'Success backup Up'
else:
	print 'Failed backup'
