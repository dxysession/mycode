# coding:utf-8
__author__ = 'dxy'
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

# 删除文件最后一行
def delete_last_line(filename):
	with open(filename, 'r') as f:
		lines = f.readlines()
		current = lines[:-1]
	newfile = open(filename,'w')
	newfile.writelines(current)
	newfile.close()

# 判断文件最后一行是否完整
def is_intact(filename):
	with open(filename,'rb') as f:
		offs = -1
		while True:
			# file.seek(off, whence=0)
			# 从文件中移动off个操作标记（文件指针），正往结束方向移动，负往开始方向移动。
			# 如果设定了whence参数，就以whence设定的起始位为准，0代表从头开始，1代表当前位置，2代表文件最末尾位置。
			f.seek(offs, 2)
			lines = f.readlines()
			if len(lines)>1:
				last = lines[-1]
				break
			offs *= 2
		last = last.strip()
		print "最后两个字符-->"+last[-2:]
		if last[-2:]=='}}':
			print "Ture"
			return True
		else:
			print "False"
			return False

# 处理searchresult.txt文件,获取需要删除最后一行的文件列表
def get_filename_list(searchresult):
	file_list = []
	with open(searchresult,'r') as f:
		for line in f.readlines():
			if line.find("filesize.txt")!= -1:
				# print line
				path = line[:line.find("filesize.txt")]
				# print path
				file_list.append(path+get_min_name_file(path))
	return file_list

# 获取文件路径下包含‘jd_’名字最短的txt文件
def get_min_name_file(path):
	length = 100
	return_file = ''
	for filename in os.listdir(path):
		if filename.find("jd_")!= -1 and filename.find(".txt")!= -1:
			if length > len(filename):
				length = len(filename)
				return_file = filename
	return return_file

if __name__ == '__main__':
	searchresult = 'searchresult.txt'
	filelist = get_filename_list(searchresult)
	n = 0
	for filename in filelist:
		print filename
		if not is_intact(filename):
			n += 1
			pass
			delete_last_line(filename)
	print str(n)+'/'+str(len(filelist))