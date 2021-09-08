import math


def Travel(firstX,firstY,board):
    movex=[-2, -1, 1, 2,  2,  1, -1, -2]
    movey=[1,  2, 2, 1, -1, -2, -2, -1]
    nextStepX=[1]*len(board)
    nextStepY=[1]*len(board)
    exitS=[1]*len(board)
    nextX = firstX
    nextY = firstY
    board[nextX][nextY] = 1
    for m in range(2,int(math.pow(len(board), 2)+1)):
        for i in range(0,len(board)):
            exitS[i] = 0
        count = 0
        for i in range(0,8):
            temI = nextX + movex[i]
            temJ = nextY + movey[i]
            if temI < 0 or temI > 7 or temJ < 0 or temJ > 7:
                continue
            if 0 == board[temI][temJ]:
                nextStepX[count] = temI
                nextStepY[count] = temJ
                count =count+1
        min=-1
        if count==0:
            return False
        if 1==count:
            min=0
        else:
            for i in range(0,count):
                for j in range(0,8):
                    temI = nextStepX[i] + movex[j]
                    temJ = nextStepY[i] + movey[j]
                    if temI < 0 or temI > 7 or temJ < 0 or temJ > 7:
                        continue
                    if 0 == board[temI][temJ]:
                        exitS[i] =exitS[i]+1
        tem = exitS[0]
        min = 0
        for  i in range(1,count):
            if tem>exitS[i]:
                tem = exitS[i]
                min = i
        nextX = nextStepX[min]
        nextY = nextStepY[min]
        board[nextX][nextY] = m
    return True


if __name__=='__main__':
    #firstX=input("输入起始点(0-7)：")
    firstX=1
    #firstY=input("输入起始点(0-7)：")
    firstY=1
    board=[[0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0]]
    if Travel(firstX, firstY, board):
        print("游历完成：")
    else:
        print("游历失败！")
    for i in range(0, len(board)):
        for j in range(0,len(board[0])):
            if board[i][j] < 10:
                print(board[i][j],end=' ')
            else:
                print(board[i][j],end=' ')
            print(" ",end=' ')
        print()
