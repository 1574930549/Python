#!py -3.7
with open("kegg.txt", "r") as f:
    fcon = f.readlines()

del fcon[0]
with open("gene_log2fc.txt", "r") as f:
    data = f.readlines()
del data[0]

shuju = []
for i in data:
    shuju.append(i.replace("\n", "").split("\t"))
zidian = {}
for i in shuju:
    zidian[i[0]] = float(i[1])

kegg = []
jiyin1 = []
jiyin2 = []

for i in fcon:
    kegg.append(i.split("\t"))

for i in kegg:
    if int(i[2]) > 20:
        print(i[1])
    if "Ovarian steroidogenesis" in i:
        jiyin1 = i
    elif "Estrogen signaling pathway" in i:
        jiyin2 = i

jiyin1 = jiyin1[5].split(", ")
jiyin2 = jiyin2[5].split(", ")

for i in jiyin1:
    if i in jiyin2:
        print(i)

upup = []
downdown = []

for i in jiyin1:
    if zidian[i] > 0 and (i not in upup):
        upup.append(i)
    elif zidian[i] < 0 and (i not in downdown):
        downdown.append(i)
for i in jiyin2:
    if zidian[i] > 0 and (i not in upup):
        upup.append(i)
    elif zidian[i] < 0 and (i not in downdown):
        downdown.append(i)

with open("output4-up.txt", "w") as f:
    for i in upup:
        f.write(i + "\n")
with open("output4-down.txt", "w") as f:
    for i in downdown:
        f.write(i + "\n")

# ECM-receptor interaction
# Metabolic pathways
# Focal adhesion
# Cytokine-cytokine receptor interaction
# 101102089
