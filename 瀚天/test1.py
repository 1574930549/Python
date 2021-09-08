from numpy.core.defchararray import lower


def indexstr(str1, str2):
    lenth2 = len(str2)
    lenth1 = len(str1)
    indexstr2 = []
    i = 0
    while str2 in str1[i:]:
        indextmp = str1.index(str2, i, lenth1)
        indexstr2=indextmp
        i = (indextmp + lenth2)
    return indexstr2


def complement(seq):
    return seq.translate(str.maketrans('ACGTacgtRYMKrymkVBHDvbhd', 'TGCAtgcaYRKMyrkmBVDHbvdh'))


def first(seq1):
    seq2 = complement(seq1)
    n = seq1.count('A')
    m = seq1.count('C')
    print(seq1)
    print(seq2)
    print('双链氢键个数:', (2 * n) + (3 * m))
    print('互补成双链:')


def second(seq1):
    seq2 = complement(seq1)
    seq1exon1 = seq1[0:24]
    seq1introns = lower(seq1[24:50])
    seq1exon2 = seq1[50:65]
    seq3 = str(seq1exon1) + str(seq1introns) + str(seq1exon2)
    # print(exon1,introns,exon2)
    print('外显子总长度', len(seq1exon1) + len(seq1exon2))
    seq2exon1 = seq2[0:24]
    seq2introns = lower(seq2[24:50])
    seq2exon2 = seq2[50:65]
    seq4 = str(seq2exon1) + str(seq2introns) + str(seq2exon2)
    print(seq3)
    print(seq4)


def third(seq1):
    a=int(indexstr(str(seq1),'AATTC'))
    seq5=seq1[0:a]
    seq6=seq1[a:65]
    # print(seq1)
    print(seq5)
    print(seq6)


if __name__ == "__main__":
    seq1 = "ATGCTTCCGGCTGTTCCCTGAGACCTCAAGTGTGAGGAATTCTGTACTATTGATGCTTCACACCT"
    first(seq1)
    second(seq1)
    third(seq1)
