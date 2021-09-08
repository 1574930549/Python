#!py -3.7

with open("input2.fa","r") as f:
    fcon = f.readlines()

all = []
allnums = {}
tag = -1
for i in fcon:
    if i.startswith(">"):
        tls = i.split(" ")
        name = tls[1]+" "+tls[2]
        if name in allnums:
            allnums[name] += 1
        else:
            allnums[name] = 1

        tag += 1
        all.append("")
        continue
    all[tag] += i.replace("\n","")
tag = 0
longlong = 0
for i in range(len(all)):
    lenth = len(all[i])
    if lenth > longlong:
        tag = i
        longlong = lenth

print(all[tag])

for key,value in allnums.items():
    print(key,(str(value)+"条"))

# GGTCTCCGGGTCCCGGGGACCCGGGGGCCCGGGGTGCGCGGCTGGGGACCTGAGGGCGAGGAGCGAGGACACACACCGAGGACTCTTGCGAGGGATCTCGGGGCCCAGCTCGGCCTCCCTCCTAGCGCTGGGGGCCTGCCCGGAACCCGAGTCCGCGGCTGTCCCTGGGGTTTGGCGCTGCGCGGAGGTCGGGTCTGGGGACCGCAGCGACTCTGGGTCTTCGGGTTGTCCCCTCGGAGGGTGGACTCAACAGTTTGTGGCAAGACAAGCTCAGAACTGAGAAGCTGTCACCACAGGTAAATAGAAGGTT
# Homo sapiens 2条
# Ovis aries 1条
# Bos taurus 1条
# Drosophila melanogaster 1条