import os

for filename in os.listdir(r'H:\网课\test'):   #‘logo/’是文件夹路径，你也可以替换其他
	print(filename)
	newname = filename.replace('', '')  #把jpg替换成png
	os.rename('H:\\网课\\test\\'+filename, 'H:\\网课\\test\\'+newname)