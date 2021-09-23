import os

for filename in os.listdir(r'C:\Users\zlh\Desktop\Vue源码解析之虚拟DOM和diff算法'):   #‘logo/’是文件夹路径，你也可以替换其他
	# print(filename)
	newname = filename.replace('【尚硅谷】Vue源码解析之虚拟DOM和diff算法 (', '').replace(')', '').replace('尚硅谷-虚拟DOM和diff算法-', '')
	# newname = filename.replace('-尚硅谷-Vue源码mustache模板引擎', '')
	# print(newname)
	newname=newname.split('.')
	newname=newname[1].replace(' ','')+'.'+newname[2]
	print(newname)
	os.rename('C:\\Users\\zlh\\Desktop\\Vue源码解析之虚拟DOM和diff算法\\'+filename, 'C:\\Users\\zlh\\Desktop\\Vue源码解析之虚拟DOM和diff算法\\'+newname)