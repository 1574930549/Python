def first():
    myFile1=open("input2.fa", "r")
    count = myFile1.readlines()
    data = []
    data2 = {}
    a = -1
    for i in count:
        if i.startswith(">"):
            num = i.split(" ")
            name = num[1] + " " + num[2]
            if name in data2:
                data2[name] += 1
            else:
                data2[name] = 1

            a += 1
            data.append("")
            continue
        data[a] += i.replace("\n", "")
    a = 0
    longlong = 0
    for i in range(len(data)):
        lenth = len(data[i])
        if lenth > longlong:
            a = i
            longlong = lenth

    print(data[a])
    return data2


def second(data2):
    for name, n in data2.items():
        print(name, (str(n) + "条"))


if __name__ == "__main__":
    data2=first()
    second(data2)
