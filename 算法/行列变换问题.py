


class graph:
    sour=0
    dest=0
    def __int__(self):
        ans = [1 << 16]
        m = 4
        n = 4
        x = 0
        row = [1] * 4
        col = [1] * 4
    def rowx(self):
        for i in range(0,n):
            y = 1
            self.row[i] = 0
            for j in range(0, self.n):
                if (self.x and 1) != 0:
                    self.row[i] != y
                y <<= 1
                self.x >>= 1
    def colx(self):
        for j in range(0,self.n):
            self.col[j]=0
        y=1
        for i in range(0,self.m):
            for j in range(0,self.n):
                if(self.x and 1)!=0:
                    self.col[j]=y
                self.x>>=1
            y<<=1
    def rowy(self):
        z=1
        x=0
        for i in range(0,self.m):
            y=self.row[i]
            for j in range(0,self.n):
                if(y and 1)!=0:
                    x|=z
                z<<=1
                y>>=1
        self.x=x
    def coly(self):
        z = 1
        x = 0
        for i in range(0, self.m):
            for j in range(0, self.n):
                if (self.col[j] and 1) != 0:
                    x |= z
                z <<= 1
                self.col[j]>>= 1
        self.x = x
    def Swaprow(self,i,j):#将二进数进行行互换
        o=self.row[i]
        self.row[i]=self.row[j]
        self.row[j]=o

    def Swapcol(self, i,  j):#将二进数进行列互换
        o=self.col[i]
        self.col[i]=self.col[j]
        self.col[j]=o
    def reveR(self,k):
        y=0
        z=1<<(4-1)
        for j in range(0,4):
            if(self.row[k]and 1)!=0:
                y|=z
            z>>=1
            self.row[k]>>=1
        self.roe[k]=y
    def reveC(self,k):
        y=0
        z=1<<(4-1)
        for j in range(0,4):
            if(self.col[k]and 1)!=0:
                y|=z
            z>>=1
            self.col[k]>>=1
        self.col[k]=y
    def rowswap(self,x,i,j):
        self.x=x
        graph.rowx()
        graph.Swaprow(i,j)
        graph.rowy()
        return self.x
    def colswap(self,x,i,j):
        self.x = x
        graph.colx()
        graph.Swapcol(i, j)
        graph.coly()
        return self.x
    def revrow(self,x,k):
        self.x = x
        graph.rowx()
        graph.reveR(k)
        graph.rowy()
        return self.x
    def revcol(self,x,k):
        self.x = x
        graph.colx()
        graph.reveC(k)
        graph.coly()
        return self.x

if __name__=="__main__":
    Maxsize = 1 << 16
    hash=[1]*Maxsize
    E=0
    N=0
    h=0
    #ss=input()
    ss='1010010000101010'
    chArrs=list(ss)
    graph=graph()
    for i in range(0,16):
        c=chArrs[i]
        graph.sour=graph.sour and (int)(c - '0') << i
    #sd=input()
    sd='1010000001100101'
    chArrd=list(sd)
    for i in range(0,16):
        c=chArrd[i]
        graph.dest=graph.dest and (int)(c - '0') << i
    queue=[None]*100
    for k in range(0,Maxsize):
        hash[k] = -1
    graph.x=graph.sour
    hash[graph.x] = 0
    #queue.append(graph.x)
    while len(queue)!=0:
        e=queue[0]
        for i in range(0,4-1):
            for j in range(i+1,4):
                graph.x=graph.rowswap(E,i,j)
                N=graph.x
                if hash[N]==-1:
                    hash[N] = hash[E] + 1
                    graph.ans[N] = E
                    queue.add(N)
        for i in range(0,4-1):
            for j in range(i+1,4):
                graph.x = graph.colswap(E, i, j)
                N = graph.x
                if hash[N] == -1:
                    hash[N] = hash[E] + 1
                    graph.ans[N] = E
                    queue.add(N)
        for i in range(0,4):
            graph.x = graph.revrow(E, i)
            N=graph.x
            if hash[N]==-1:
                hash[N] = hash[E] + 1
                graph.ans[N] = E
                queue.add(N)
        for i in range(0, 4):
            graph.x = graph.revcol(E, i)
            N = graph.x
            if hash[N] == -1:
                hash[N] = hash[E] + 1
                graph.ans[N] = E
                queue.add(N)
        if hash[graph.dest]!=-1:
            print("ok")
            break

    def outb(x):
        for i in range(0,4):
            for j in range(0,4):
                if (x and 1)!=0:
                    print(1)
                else:
                    print(0)
                x/=2
            print()
    def output(N):
        if N==graph.sour:
            print()
            outb(N)
            return
        output(graph.ans[N])
        print()
        outb(N)

# 1010010000101010
# 1010000001100101