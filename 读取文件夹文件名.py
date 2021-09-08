import os
file_dir = r"G:\代码\HTML\newtest\images\小彤彤"
i = 1
a = os.walk(file_dir)

for root, dirs, files in os.walk(file_dir):
    print(i)
    i += 1
    # print(root) #当前目录路径
    # print(dirs) #当前路径下所有子目录
    print(files) #当前路径下所有非目录子文件
for name in files:
    str1='<a href="images/小彤彤/'+str(name)+'" target="_blank">\n\t<img src="images/小彤彤/'+str(name)+'" onload="javascript:DrawImage(this,200,200)" title="小彤彤" />\n</a>'
    # print(name)
    print(str1)