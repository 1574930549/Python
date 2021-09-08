myFile=open(r'input2.fa', 'r')
s=myFile.readlines()
print(s)
dataset1=[]
dataset2=[]
for line in s:
    temp1 = line.strip('\n')
    dataset1.append(temp1)
    temp1 = temp1.strip('\t')
    temp2 = temp1.split('\t')
    dataset2.append(temp2)

print(dataset1)
print(dataset2)
# del dataset2[0]
print(dataset2)
for i in range(0,len(dataset2)):
    a='\t'.join(dataset2[i])
    print(a,end='')
print(len(str(dataset2[2])))