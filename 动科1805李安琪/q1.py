#!py -3.7
seq1 = 'ATGCTTCCGGCTGTTCCCTGAGACCTCAAGTGTGAGGAATTCTGTACTATTGATGCTTCACACCT'

seq111 = seq1.replace("A",'t').replace("C",'g').replace("T",'a').replace("G",'c').upper()
print(seq111)

HH = len(seq1)*2
for i in seq1:
    if i == "G" or i == "C":
        HH += 1
print(HH)

shuchu = seq1[:23]+seq1[23:50].lower()+seq1[50:]
print(shuchu )

qiege = seq1.find('GAATTC')
qiege = qiege + 1
qiewan1 = seq1[:qiege]
qiewan2 = seq1[qiege:]
print(len(qiewan1),qiewan1)
print(len(qiewan2),qiewan2)

# TACGAAGGCCGACAAGGGACTCTGGAGTTCACACTCCTTAAGACATGATAACTACGAAGTGTGGA
# 161
# ATGCTTCCGGCTGTTCCCTGAGAcctcaagtgtgaggaattctgtactatTGATGCTTCACACCT
# 37 ATGCTTCCGGCTGTTCCCTGAGACCTCAAGTGTGAGG
# 28 AATTCTGTACTATTGATGCTTCACACCT