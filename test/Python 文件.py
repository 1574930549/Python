# 打开一个文件
fo = open("text.txt", "a")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)
str0 = "test"
fo.write(str0)
fo.close()
fo = open("text.txt", "r+")
str1 = fo.read(10)
print("读取的字符串是 : ", str1)

# 查找当前位置
position = fo.tell()
print("当前文件位置 : ", position)

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str1 = fo.read(10)
print("重新读取字符串 : ", str1)
# 关闭打开的文件
fo.close()
