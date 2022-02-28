import numpy as np
import random 

# 定義區域
#region 

# 移動優先 右 > 下 > 左 > 上

# 移動方位定義數字
#   7 8 9
#   4 5 6
#   1 2 3 

#endregion 

# 移動 Function
#region

# 移動優先 右 > 下 > 左 > 上
def IsCanMove(Direction):
    global Key_X,Key_Y,Size
    if(Direction == 6):
        return Key_Y < Size-1
    if(Direction == 2):
        return Key_X < Size-1
    if(Direction == 4):
        return Key_Y > 0
    if(Direction == 8):
        return Key_X > 0
    else:
       return False

# 使用DoMoveNext前必須If IsCanMo
def DoMoveNext(Direction):
    global HuarongDao,Key_X,Key_Y,DirectionMoveTrace

    if(Direction == 6):
       HuarongDao[Key_X][Key_Y] = HuarongDao[Key_X][Key_Y+1]
       HuarongDao[Key_X][Key_Y+1] = 0
       Key_Y+=1
       
    if(Direction == 2):
       HuarongDao[Key_X][Key_Y] = HuarongDao[Key_X+1][Key_Y]
       HuarongDao[Key_X+1][Key_Y] = 0
       Key_X+=1

    if(Direction == 4):
       HuarongDao[Key_X][Key_Y] = HuarongDao[Key_X][Key_Y-1]
       HuarongDao[Key_X][Key_Y-1] = 0
       Key_Y-=1

    if(Direction == 8):
       HuarongDao[Key_X][Key_Y] = HuarongDao[Key_X-1][Key_Y]
       HuarongDao[Key_X-1][Key_Y] = 0
       Key_X-=1

    DirectionMoveTrace.append(Direction)

# DoMoveBack
def DoMoveBack(Direction):

    global HuarongDao,Key_X,Key_Y,DirectionMoveTrace
    Direction =  DirectionMoveTrace.pop()

    if(Direction == 6):
       HuarongDao[Key_X][Key_Y] = HuarongDao[Key_X][Key_Y-1]
       HuarongDao[Key_X][Key_Y-1] = 0
       Key_Y-=1
      
    if(Direction == 2):
       HuarongDao[Key_X][Key_Y] = HuarongDao[Key_X-1][Key_Y]
       HuarongDao[Key_X-1][Key_Y] = 0
       Key_X-=1

    if(Direction == 4):
       HuarongDao[Key_X][Key_Y] = HuarongDao[Key_X][Key_Y+1]
       HuarongDao[Key_X][Key_Y+1] = 0
       Key_Y+=1

    if(Direction == 8):
       HuarongDao[Key_X][Key_Y] = HuarongDao[Key_X+1][Key_Y]
       HuarongDao[Key_X+1][Key_Y] = 0
       Key_X+=1
    return

#endregion

# 設定 Function
#region

# 使用亂數方式產生華容道的初始數據
def SetHuarongDaoValue_Random(Size):
    HuarongDao = np.zeros([Size*Size], dtype=int)
    Key =""
    Count = 0
    while True:
        nonZeroCount = len(HuarongDao[np.nonzero(HuarongDao)])
        Value = random.randint(1,Size*Size)
        if(Value not in HuarongDao):
            HuarongDao[Count] = Value
            Count+= 1
            if(Value==Size*Size):
                Value = 0
            if(nonZeroCount==Size*Size-1):
                Key+=str(Value)
            else:
                Key+=str(Value)+','
        if(nonZeroCount==Size*Size):
            break
    
    return Key

# 根據使用者輸入的初始狀態，更新華容道數據
def SetHuarongDaoValue(Value,DoCheck):
    global Size,HuarongDao,Key_X,Key_Y

    listValue = Value.split(',')
    for i in range(Size):
        for j in range(Size):
            # 如果當前數字已超出華容道大小，則為非法輸入，Ex: Size = 3 ，輸入值卻含有 100
            if(int(listValue[j+i*Size]) not in range(0,Size*Size) and DoCheck ):
                return False
            # 如果當前數字為已存在華容道，即為重複數字，華容道禁止重複，固為非法輸入
            if(int(listValue[j+i*Size]) in HuarongDao and int(listValue[j+i*Size])!=0  and DoCheck ):
                return False
            # 將合法數字塞入華容道
            HuarongDao[i][j] = listValue[j+i*Size]
            # 將0的位置標記出來，以利開發者操作
            if(HuarongDao[i][j]==0):
                Key_X = i
                Key_Y = j
    return True

# 根據使用者輸入的Size 設定出一組華容道答案
def GetHuarongDaoSol(Size):
    Sol = ""
    for i in range(Size*Size):
        if(i==Size*Size -1 ):
            Sol+= str(0)
        else:
            Sol+= str(i+1) +","
    return Sol

#endregion

# 回傳情況 Function
#region

# 顯示當前華容到的情況
def PrintHuarongDao():
    global HuarongDao,Size

    def SingleLine(Line):
        strLine = ""
        for i in range(Size):
            strLine += str(Line[i]) + ' '
        return strLine
    print("-------Print-------")
    for i in range(Size):
        Line = np.zeros([Size], dtype=int)
        for j in range(Size):
            Line[j] = HuarongDao[i][j]
        print(SingleLine(Line))

# 回傳當前華容到的全部狀態
def GetHuarongDaoState():
    global HuarongDao,Size
    Line = ""
    for i in range(Size):
        for j in range(Size):
            Line += str(HuarongDao[i][j]) 
            if(not (i == Size-1 and j == Size-1)):
                Line += ","
    return Line

# 顯示尋訪紀錄的方位
def PrintSolDir(DirectionMoveTrace):
    strChinese=""
    for i in range(len(DirectionMoveTrace)):
        if(DirectionMoveTrace[i]==6):
            strChinese += "右"
        elif (DirectionMoveTrace[i]==2):
            strChinese += "下"
        elif (DirectionMoveTrace[i]==4):
            strChinese += "左"
        elif (DirectionMoveTrace[i]==8):
            strChinese += "上"
        strChinese+= " - "
    print(strChinese)

#endregion

# 深搜 Function 
#region

# 深搜入口
def DeepSearchSolve():
    global LocationMoveTrace,Correct,IsOver
    Status = GetHuarongDaoState()
    if(Correct == Status):
        return True

    LocationMoveTrace.append(Status)
    
    if(DeepSearch(6)):
        return True
    else:
        IsOver = False

    if(DeepSearch(2)):
        return True
    else:
        IsOver = False

    if(DeepSearch(4)):
        return True
    else:
        IsOver = False

    if(DeepSearch(8)):
        return True
    else:
        return False


# 深搜方位主程式
def DeepSearch(Direction):
    
    global LocationMoveTrace,Correct,DirectionMoveTrace,IsOver
    if(IsCanMove(Direction)==False):
        return False

    if(len(DirectionMoveTrace)>200):
        IsOver = True

    if(IsOver):
        return False
    
    DoMoveNext(Direction)
    if(GetHuarongDaoState() == Correct):
        return True
    if( GetHuarongDaoState() in LocationMoveTrace ):
        DoMoveBack(Direction)
        return False

    LocationMoveTrace.append(GetHuarongDaoState())

    if(DeepSearch(6) or DeepSearch(2) or DeepSearch(4) or DeepSearch(8)):
        return True
    else:
        DoMoveBack(Direction)
        return False

#endregion

# 廣搜 Function
#region

def BreadthSearchSolve():
    global LocationMoveTrace,Correct,SetBreadth

    Status = GetHuarongDaoState()
    if(Correct == Status):
        return True

    LocationMoveTrace.append(Status)

    temp = ClsBreadth(Status,None)
    SetBreadth.append(temp)

    return BreadthSearch()

def BreadthSearch():
    global SetBreadth,Correct,LocationMoveTrace,HuarongDaoValue

    while(len(SetBreadth)>0):

        temp = SetBreadth[0]
        SetBreadth.remove(temp)
        SetHuarongDaoValue(temp.State,False)
       
        if(GetHuarongDaoState()== Correct):
            PrintSolDir(temp.DirectionMoveTrace)  
            return True

        for i in range(4):
            Direction = 8
            if(i==0):
                Direction = 6
            elif(i==1):
                Direction = 2
            elif(i==2):
                Direction = 4
            if(IsCanMove(Direction)):
                SetHuarongDaoValue(temp.State,False)
                DoMoveNext(Direction)
                if( GetHuarongDaoState() in LocationMoveTrace ):
                    DoMoveBack(Direction)
                    continue
                LocationMoveTrace.append(GetHuarongDaoState())
                NewDirArray = temp.DirectionMoveTrace.copy()
                NewDirArray.append(Direction)
                SetBreadth.append(ClsBreadth(GetHuarongDaoState(),NewDirArray))
    return False

#endregion

# 廣搜 Class
#region

class ClsBreadth():
    def __init__(self, thisState,thisDirectionMoveTrace):   
        self.State = thisState
        if(thisDirectionMoveTrace== None ):
            self.DirectionMoveTrace = []
        else:
            self.DirectionMoveTrace = thisDirectionMoveTrace
   
#endregion


# --------------------------主程式--------------------------

# 初始函數宣告
#region

Key_X = 0 
Key_Y = 0 
DirectionMoveTrace =[]
LocationMoveTrace =[]
IsOver=False
SetBreadth =[]

#endregion

# 獲取華容道
#region 

while True :
    Size = int(input("請輸入華容道的Size："))
    if(input("是否要用亂數產生華容道初始數據 (Y/N)：") == "Y"):
        HuarongDaoValue = SetHuarongDaoValue_Random(Size)
    else:
        HuarongDaoValue = input("請輸入華容道的初始數值(Ex : 1,2,3,4,5,6,7,8,0)：")

      # 如果當前輸入的華容道初始數據，剛好符合華容道大小的話，才進行下一步合法判斷
    if(len(HuarongDaoValue.split(',')) == Size*Size ):
        HuarongDao = np.zeros([Size,Size], dtype=int)

        # 將當前初始數據塞入華容道，若無非法輸入則跳出此迴圈
        if(SetHuarongDaoValue(HuarongDaoValue,True)):
          #  PrintHuarongDao()
            break

    # 進行到此處皆為非法操作
    print("華容道數據設計錯誤，請重新輸入相對應的資料。")

#endregion

# 獲取華容道答案
Correct = GetHuarongDaoSol(Size)
PrintHuarongDao()

if(DeepSearchSolve()):
    PrintSolDir(DirectionMoveTrace)
else:
    print("當前設定無法在200步內完成，故設定為無解")


SetHuarongDaoValue(HuarongDaoValue,False)
DirectionMoveTrace =[]
LocationMoveTrace =[]
print("-------------")
PrintHuarongDao()

BreadthSearchSolve()
