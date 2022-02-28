import numpy as np
import random 

def CreateRandom(Size):
    global ArrayMoney
    for i in range(Size):
        for j in range(Size):
              ArrayMoney[i][j] = random.randint(1,Size)

def PrintArrayMoney():
    global ArrayMoney,Size

    def SingleLine(Line):
        strLine = ""
        for i in range(Size):
            strLine += str(Line[i]) + ' '
        return strLine

    print("-------Print-------")
    for i in range(Size):
        Line = np.zeros([Size], dtype=int)
        for j in range(Size):
            Line[j] = ArrayMoney[i][j]
        print(SingleLine(Line))

def PrintDirTrace():
    global DirectionMoveTrace
    strAns = ""
    for i in range(len(DirectionMoveTrace)):
        if(DirectionMoveTrace[i] == 0):
            strAns+= "右 - "
        else:
             strAns+= "下 - "
    print(strAns)

def IsCanMove(Direction):
    global Key_X,Key_Y,Size

    if(Direction == 6 or Direction == 0):
        return Key_Y < Size-1
    if(Direction == 2  or Direction == 1):
        return Key_X < Size-1
    else:
       return False

def DoMoveNext(Direction):
    global ArrayMoney,Key_X,Key_Y,DirectionMoveTrace

    if(Direction == 6 or Direction == 0):
       Key_Y+=1
       
    if(Direction == 2  or Direction == 1):
       Key_X+=1

    DirectionMoveTrace.append(Direction)

def DeepSearch():
    global Key_X,Key_Y,Size,ArrayMoney,ArrayMoveTrace,DirectionMoveTrace

    if(Key_X==Size-1  and Key_Y == Size-1):
        Sum = 0
        for i in range(len(ArrayMoveTrace)):
            Sum+=ArrayMoveTrace[i]
        print("---"+str(Sum) + "---")
        PrintDirTrace()
        print()
        ArrayMoveTrace = []
        DirectionMoveTrace = []
    else:
        for j in range(2):
            if IsCanMove(j):
                DoMoveNext(j)
                Now_X = Key_X
                Now_Y = Key_Y
                Now_Dir = DirectionMoveTrace.copy()
                Now_Trace = ArrayMoveTrace.copy()
                ArrayMoveTrace.append(ArrayMoney[Key_X][Key_Y])
                DeepSearch()
                Key_X = Now_X
                Key_Y = Now_Y
                DirectionMoveTrace = Now_Dir.copy()
                ArrayMoveTrace = Now_Trace.copy()
    return

ArrayMoney = [] # 當前的薪水陣列
ArrayMoveTrace = [] # 存放當前累積的錢
DirectionMoveTrace=[] # 存放方向

Key_X=0
Key_Y=0

Size = int(input("請輸入Size："))
ArrayMoney = np.zeros([Size,Size], dtype=int)

CreateRandom(Size)
PrintArrayMoney();
DeepSearch()

