import math


def first(txt, belong, chain):
    myFile = open(txt, 'r')
    cout = myFile.readlines()
    result = []
    for i in cout:
        i = i.replace("\n", "")
        result.append(i)
    dna = []
    for i in result:
        length = []
        if i in chain:
            length.append(chain.find(i))
            length.append(chain.find(i) + len(i))
            dna.append(length)
    dna.sort()

    while not dna[0][0]:
        connection = []
        length = dna[0][1]
        connection.append(dna[0])
        for i in dna:
            if i[0] == length:
                length = i[1]
                connection.append(i)
                if length == len(chain):
                    dictionary[belong] += 1
                    for k in connection:
                        dna.remove(k)
                    connection.clear()
                    length = 0
                    break
                elif length > len(chain):
                    length = 0
                    break
        if len(dna) and len(connection):
            dna.remove(connection.pop())
        if not len(dna):
            break
    return dictionary[belong]


def second():
    A = math.log(dictionary['a1'] / dictionary['a2'], 2)
    B = math.log(dictionary['b1'] / dictionary['b2'], 2)

    if B < A:
        print("基因A", A)
    else:
        print("基因B", B)


if __name__ == "__main__":
    DNA1 = 'ACATCTCAAACTGGCAAAACTCAGTCTTAGCAGATTCAGTGTGGAAGCAGCTATCAAAAAGGCCATAAGGATTTTGTCCCCAAATTTCACATGAGCTACCTTGCTTCAAACTACTGAGATGAAGGGGGCAAGATTATTTGTCCTTCTTTCTAGTTTATGGAGTGGGGGCATTGGGCTTAACAACAGTAAGCATTCTTGGACTATACCTGA'
    DNA2 = 'ATTTCATTTCCACGCCAACCATCGTGCGCCGCGGTCTGAACGCTCCTGCCACAGAAAAAGAAAATAAAAGCAAGGAAAATTCTAATCGAATACCAAATATCGTGCTTGTGTGCTCTTTCCGCAATTGATTTTTTTTAAGTAGTGCATGACAATAACCGTTGAGTTGACTCCAACCGAAGTAACCATAAC'
    dictionary = {"a1": 0, "b1": 0, "a2": 0, "b2": 0}
    dictionary['a1'] = first("input5-1.fa", 'a1', DNA1)
    dictionary['b1'] = first("input5-1.fa", 'b1', DNA2)
    dictionary['a2'] = first("input5-2.fa", 'a2', DNA1)
    dictionary['b2'] = first("input5-2.fa", 'b2', DNA2)
    print(dictionary['a1'], dictionary['b1'], dictionary['a2'], dictionary['b2'])
    second()
