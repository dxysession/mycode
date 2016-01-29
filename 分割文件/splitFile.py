#coding:utf-8
__author__ = 'dxy'
from os.path import getsize

class spiltFileTool:
	def spileByLine(self,filename):
		sourcefile = open(filename,'r')
		i = 1
		filename = filename.replace(".txt","")
		newfilename = filename+'_part'+str(i)+".txt"
		part = open(newfilename,'w')
		for line in sourcefile:
			if getsize(newfilename) <= 50*1024*1024:
				part.write(line);
			else:
				part.close()
				i = i + 1
				newfilename = filename+'_part'+str(i)+".txt"
				part = open(newfilename,'w')
		part.close()
				

if __name__ == '__main__':
	filename = 'jd_phone_all20151022.txt'
	tool = spiltFileTool()
	tool.spileByLine(filename)
