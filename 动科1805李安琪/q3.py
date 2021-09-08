#!py -3.7
seq2 = 'GCCAUUGUAAUGACGUGGGAAGGCCGCUGAAAGGGUGCCCGAUAG'
fanyi = ''
zidian = {'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
         'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
         'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
         'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
         'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
         'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
         'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
         'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
         'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
         'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
         'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
         'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
         'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
         'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
         'UAC': 'Y', 'UAU': 'Y', 'UAA': '', 'UAG': '',
         'UGC': 'C', 'UGU': 'C', 'UGA': '', 'UGG': 'W'}
def peidui(i):
    return seq2[i:i+3]

def my_function(str1,str2):
    return int(str1.count(str2)/len(str1)*100)
tiaoshu = 0
panduan = 0

for i in range(len(seq2)-2):
    if (tiaoshu > 0):
        tiaoshu -= 1
        continue
    if (peidui(i)=='UAA' or peidui(i)=='UAG' or peidui(i)=='UGA'):
        panduan = 0
    if peidui(i)=='AUG':
        panduan = 1 
    if (panduan == 1):
        tiaoshu = 2
        fanyi += zidian[peidui(i)]

print(fanyi)

assert my_function("MSRSLLLRFLLFLLLLPPLP","M") == 5
print(my_function(fanyi,"M"))

# MTWEGR
# 16