#coding:utf-8
__author__ = 'dxy'
from os.path import getsize

def join(filename_01,filename_02):
	newfilename = "join.txt"
	targetfile = open(newfilename,'w')
	sourcefile_01 = open(filename_01,'r')
	for line in sourcefile_01:
			targetfile.write(line)
	sourcefile_02 = open(filename_02,'r')
	for line in sourcefile_02:
			targetfile.write(line)

filename_01 = 'jd_mouse_5000_20151103.txt'
filename_02 = 'jd_mouse_5000_20151104.txt'
join(filename_01,filename_02)