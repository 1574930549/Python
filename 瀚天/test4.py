def first():
    myFile1 = open("kegg.txt", "r")
    count = myFile1.readlines()
    del count[0]
    Data1 = []
    for i in count:
        Data1.append(i.split("\t"))
    for i in Data1:
        if int(i[2]) > 20:
            print(i[1])
    return Data1


def second(Data2):
    for i in Data2:
        if str(i[1]) == "Ovarian steroidogenesis":
            Ovarian = i
            Ovarian = Ovarian[5].split(", ")
        elif str(i[1]) == "Estrogen signaling pathway":
            Estrogen = i
            Estrogen = Estrogen[5].split(", ")
    for i in Ovarian:
        if i in Estrogen:
            print(i)
    return Ovarian, Estrogen


def third(Ovarian, Estrogen):
    myFile2 = open("gene_log2fc.txt", "r")
    data = myFile2.readlines()
    del data[0]
    data2 = []
    for i in data:
        data2.append(i.replace("\n", "").split("\t"))
    dictionary = {}
    for i in data2:
        dictionary[i[0]] = float(i[1])
    Up = []
    Down = []
    for i in Ovarian:
        if dictionary[i] > 0 and (i not in Up):
            Up.append(i)
        elif dictionary[i] < 0 and (i not in Down):
            Down.append(i)
    for i in Estrogen:
        if dictionary[i] > 0 and (i not in Up):
            Up.append(i)
        elif dictionary[i] < 0 and (i not in Down):
            Down.append(i)
    myFile3 = open("output4-up.txt", "w")
    for i in Up:
        myFile3.write(i + "\n")
    myFile4 = open("output4-down.txt", "w")
    for i in Down:
        myFile4.write(i + "\n")


if __name__ == "__main__":
    Data = first()
    Ovarian, Estrogen = second(Data)
    third(Ovarian, Estrogen)
