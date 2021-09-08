count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1

print("Good bye!")

# continue 和 break 用法
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print(i,end="") # 输出双数2、自动弹出网页甘特图、6、8、10
print()
i = 1
while 1:  # 循环条件为1必定成立
    print(i,end="")  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break

count = 0
while count < 5:
   print (count, "<  5")
   count = count + 1
else:
   print (count, ">= 5")