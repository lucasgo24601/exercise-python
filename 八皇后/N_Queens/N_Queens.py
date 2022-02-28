import numpy as np

# 主函數
def BackTrack(Column,Slash,BackSlash,Queens,i):
    global QueenSize
    if(i==QueenSize):
        QueenPrint(Queens)
    else:
        for j in range(QueenSize):
            if isVisitable(i, j, Column,Slash,BackSlash):
                Queens[i]=j
                # 先把當前位置設定為，佔據
                Column[j] = Slash[i + j] = BackSlash[i - j + QueenSize] = 1
                BackTrack(Column,Slash,BackSlash,Queens,i+1)
                # 會進行到此步則為，回朔上一個節點，以利陣列去造訪
                Column[j] = Slash[i + j] = BackSlash[i - j + QueenSize] = 0


# 判斷當前位置是否合法
def isVisitable( i, j, Column,Slash,BackSlash) :
    global QueenSize
    return not(Column[j] or Slash[i + j] or BackSlash[i - j + QueenSize])

# 顯示皇后的圖形
def QueenPrint(Queens) :
    global QueenSize
    for i in range(len(Queens)) :
        print( '. ' * (Queens[i]) + 'X ' + '. '*(QueenSize-Queens[i]-1))
    print("-----------------")


QueenSize =  int(input("請輸入Size："))

Queens=np.zeros([QueenSize], dtype=int)
Column =np.zeros([QueenSize], dtype=int)
BackSlash =np.zeros([QueenSize*2], dtype=int)
Slash= np.zeros([QueenSize*2], dtype=int)

BackTrack(Column,Slash,BackSlash,Queens,0)

input("Enter any key to exist\n")
