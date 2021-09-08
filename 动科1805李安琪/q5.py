#!py -3.7
import math
dna1 = 'ACATCTCAAACTGGCAAAACTCAGTCTTAGCAGATTCAGTGTGGAAGCAGCTATCAAAAAGGCCATAAGGATTTTGTCCCCAAATTTCACATGAGCTACCTTGCTTCAAACTACTGAGATGAAGGGGGCAAGATTATTTGTCCTTCTTTCTAGTTTATGGAGTGGGGGCATTGGGCTTAACAACAGTAAGCATTCTTGGACTATACCTGA'
dna2 = 'ATTTCATTTCCACGCCAACCATCGTGCGCCGCGGTCTGAACGCTCCTGCCACAGAAAAAGAAAATAAAAGCAAGGAAAATTCTAATCGAATACCAAATATCGTGCTTGTGTGCTCTTTCCGCAATTGATTTTTTTTAAGTAGTGCATGACAATAACCGTTGAGTTGACTCCAACCGAAGTAACCATAAC'
readscount = {"a1":0,"b1":0,"a2":0,"b2":0}


def duwenjian(filename):
    with open(filename,'r') as f:
        fcon = f.readlines()
    result = []
    for i in fcon:
        i = i.replace("\n","")
        result.append(i)
    return result

def jisuan(file,belong,chain):
    dna = []
    for i in file:
        changdu = []
        if i in chain:
            changdu.append(chain.find(i))
            changdu.append(chain.find(i)+len(i))
            dna.append(changdu)
    dna.sort()
   
    while not dna[0][0]:
        lianjie =[]
        changdu = dna[0][1]
        lianjie.append(dna[0])
        for i in dna:
            if i[0] == changdu:
                changdu = i[1]
                lianjie.append(i)
                if changdu == len(chain):
                    readscount[belong] += 1
                    for k in lianjie:
                        dna.remove(k)
                    lianjie.clear()
                    changdu = 0
                    break
                elif changdu > len(chain):
                    changdu = 0
                    break
        if len(dna) and len(lianjie):
            dna.remove(lianjie.pop())
        if not len(dna):
            break
    
jisuan(duwenjian("input5-1.fa"),'a1',dna1)
jisuan(duwenjian("input5-1.fa"),'b1',dna2)
jisuan(duwenjian("input5-2.fa"),'a2',dna1)
jisuan(duwenjian("input5-2.fa"),'b2',dna2)

print(readscount['a1'],readscount['b1'],readscount['a2'],readscount['b2'])
jieguoA = math.log(readscount['a1']/readscount['a2'],2)
jieguoB = math.log(readscount['b1']/readscount['b2'],2)

if jieguoB < jieguoA:
    print("基因A",jieguoA)
else:
    print("基因B",jieguoB)

# 3 1 1 3
# 基因A 1.5849625007211563