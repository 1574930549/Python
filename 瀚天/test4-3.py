import operator
from functools import reduce
myFile=open(r'gene_log2fc.txt', 'r')
s=myFile.readlines()
# print(s)
dataset1=[]
dataset2=[]
for line in s:
    temp1 = line.strip('\n')
    dataset1.append(temp1)
    temp1 = temp1.strip('\t')
    temp2 = temp1.split('\t')
    dataset2.append(temp2)

# print(dataset1)
# print(dataset2)
del dataset2[0]
# print(dataset2)
# print(len(dataset2))
up=[]
down=[]
for i in range(0,len(dataset2)):
    if float(dataset2[i][1])>0:
        up.append(dataset2[i])
    else:
        down.append(dataset2[i])
myFileWrite = open(r'output4-up.txt', 'w', newline='')
for i in range(0,len(up)):
    a='\t'.join(up[i])
    myFileWrite.write(a)
    myFileWrite.write('\r\n')
myFileWrite.close()
myFileWrite = open(r'output4-down.txt', 'w', newline='')
for i in range(0,len(down)):
    a='\t'.join(down[i])
    myFileWrite.write(a)
    myFileWrite.write('\r\n')
myFileWrite.close()
# print(up)
# print(down)
        # print(dataset2[i][1])
# print(dataset2[1][1])
# dataset3=reduce(operator.add, dataset2)
# print(dataset3)
# dict={}
# for list in dataset3:
#     keys=list.split(",")
#     for key in keys:
#         if key in dict.keys():
#             dict[key]=dict[key]+1
#         else:
#             dict[key]=1
# print(dict)