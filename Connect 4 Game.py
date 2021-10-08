# PROJECT 1
# CONNECT 4 GAME

#Project: Project #1 (Connect 4)

#Task: Create the 'Connect 4' Game (a two-player game)
#Useful Link: https://youtu.be/utXzIFEVPjA (Connect 4 Rules)




# | | | | | | 1
#-------------2
# | | | | | | 3
#-------------4
# | | | | | | 5
#-------------6
# | | | | | | 7
#-------------8
# | | | | | | 9
#-------------10
# | | | | | | 11 ->row
#1234567890123 ->column

#creating the blocks
def blocks(list):
    for row in range(1,12): # 1,2,3,4,5,6,7,8,9,10,11
                            # 1,.,3,.,5,.,7,.,9,.,11
        if row%2 == 1: # if row is odd = 1,3,5,7,9,11
            Row = int(row/2) #--> 0.5,1.5,2.5,3.5,4.5,5.5 using int() gives 0,1,2,3,4,5
            for column in range(1,14): # 1,2,3,4,5,6,7,8,9,10,11,12,13
                                       # 1,.,3,.,5,.,7,.,9,.,11,.,13
                if column%2 == 1:  # if column is odd = 1,3,5,7,9,11,13
                    Column = int(column/2) #--> 0.5,1.5,2.5,3.5,4.5,5.5,6.5 using int() gives 0,1,2,3,4,5,6
                    if column != 13:
                        print(list[Column][Row],end="")
                    else:
                        print(list[Column][Row])
                else:
                    print("|",end="")
        else:
            print("-------------")



#Creating Players and their moves
Player = "Player1"
columnRowList = [[" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "]]
#               [[Row0,Row1,Row2,Row3,Row4,Row5],[Row0,Row1,Row2,Row3,Row4,Row5],[Row0,Row1,Row2,Row3,Row4,Row5],[Row0,Row1,Row2,Row3,Row4,Row5],[Row0,Row1,Row2,Row3,Row4,Row5],[Row0,Row1,Row2,Row3,Row4,Row5],[Row0,Row1,Row2,Row3,Row4,Row5]]
#                  Column0           Column1         Column2          Column3          Column4         Column5           Column6        
ROW = 6
COLUMN = 7 

def AscendPlay1(columnRowList,chooseRow):
    if columnRowList[chooseColumn][5] == " " and chooseRow == 5:
        columnRowList[chooseColumn][chooseRow] = "X"

    elif columnRowList[chooseColumn][5] != " " and chooseRow == 4:
        columnRowList[chooseColumn][chooseRow] = "X"

    elif columnRowList[chooseColumn][4] != " " and chooseRow == 3:
        columnRowList[chooseColumn][chooseRow] = "X"

    elif columnRowList[chooseColumn][3] != " " and chooseRow == 2:
        columnRowList[chooseColumn][chooseRow] = "X"

    elif columnRowList[chooseColumn][2] != " " and chooseRow == 1:
        columnRowList[chooseColumn][chooseRow] = "X"

    elif columnRowList[chooseColumn][1] != " " and chooseRow == 0:
        columnRowList[chooseColumn][chooseRow] = "X"

    else:
        print("Oops!! Your Loss!", Player)


def AscendPlay2(columnRowList,chooseRow):
    if columnRowList[chooseColumn][5] == " " and chooseRow == 5:
        columnRowList[chooseColumn][chooseRow] = "O"

    elif columnRowList[chooseColumn][5] != " " and chooseRow == 4:
        columnRowList[chooseColumn][chooseRow] = "O"

    elif columnRowList[chooseColumn][4] != " " and chooseRow == 3:
        columnRowList[chooseColumn][chooseRow] = "O"

    elif columnRowList[chooseColumn][3] != " " and chooseRow == 2:
        columnRowList[chooseColumn][chooseRow] = "O"

    elif columnRowList[chooseColumn][2] != " " and chooseRow == 1:
        columnRowList[chooseColumn][chooseRow] = "O"

    elif columnRowList[chooseColumn][1] != " " and chooseRow == 0:
        columnRowList[chooseColumn][chooseRow] = "O"
    
    else:
        print("Oops!! Your Loss!", Player)

def winMoves1(columnRowList):
    #Horizantal win
    for cl in range(COLUMN-3):
        for rw in range(ROW):
            if columnRowList[cl][rw] == "X" and columnRowList[cl+1][rw] == "X" and columnRowList[cl+2][rw] == "X" and columnRowList[cl+3][rw] == "X":
                print("PLAYER 1 WINS!!!!")
                blocks(columnRowList)
                return True

    #Vertical win
    for cl in range(COLUMN):
        for rw in range(ROW-3):
            if columnRowList[cl][rw] == "X" and columnRowList[cl][rw+1] == "X" and columnRowList[cl][rw+2] == "X" and columnRowList[cl][rw+3] == "X":
                print("PLAYER 1 WINS!!!!")
                blocks(columnRowList)
                return True

    #Ascending diagonal win
    for cl in range(COLUMN-3):
        for rw in range(ROW-3):
            if columnRowList[cl][rw] == "X" and columnRowList[cl+1][rw+1] == "X" and columnRowList[cl+2][rw+2] == "X" and columnRowList[cl+3][rw+3] == "X":
                print("PLAYER 1 WINS!!!!")
                blocks(columnRowList)
                return True

    #Descending diagonal win
    for cl in range(COLUMN-3):
        for rw in range(3, ROW):
            if columnRowList[cl][rw] == "X" and columnRowList[cl+1][rw-1] == "X" and columnRowList[cl+2][rw-2] == "X" and columnRowList[cl+3][rw-3] == "X":
                print("PLAYER 1 WINS!!!!")
                blocks(columnRowList)
                return True    

def winMoves2(columnRowList):
    #Horizantal win
    for cl in range(COLUMN-3):
        for rw in range(ROW):
            if columnRowList[cl][rw] == "O" and columnRowList[cl+1][rw] == "O" and columnRowList[cl+2][rw] == "O" and columnRowList[cl+3][chooseRow] == "O":
                print("PLAYER 2 WINS!!!!")
                blocks(columnRowList)
                return True

    #Vertical win
    for cl in range(COLUMN):
        for rw in range(ROW-3):
            if columnRowList[cl][rw] == "O" and columnRowList[cl][rw+1] == "O" and columnRowList[cl][rw+2] == "O" and columnRowList[cl][rw+3] == "O":
                print("PLAYER 2 WINS!!!!")
                blocks(columnRowList)
                return True

    #Ascending diagonal win
    for cl in range(COLUMN-3):
        for rw in range(ROW-3):
            if columnRowList[cl][rw] == "O" and columnRowList[cl+1][rw+1] == "O" and columnRowList[cl+2][rw+2] == "O" and columnRowList[cl+3][rw+3] == "O":
                print("PLAYER 2 WINS!!!!")
                blocks(columnRowList)
                return True

    #Descending diagonal win
    for cl in range(COLUMN-3):
        for rw in range(3, ROW):
            if columnRowList[cl][rw] == "O" and columnRowList[cl+1][rw-1] == "O" and columnRowList[cl+2][rw-2] == "O" and columnRowList[cl+3][rw-3] == "O":
                print("PLAYER 2 WINS!!!!")
                blocks(columnRowList)
                return True

blocks(columnRowList)

while(True):
    print("Your Turn: ",Player)
    chooseRow = int(input("Pick Row: "))
    chooseColumn = int(input("Pick Column: "))
       
    if Player == "Player1":
        if columnRowList[chooseColumn][chooseRow] == " ":
            AscendPlay1(columnRowList,chooseRow)
            if winMoves1(columnRowList) == True:
                break
            Player = "Player2" 
               
    else:
        if columnRowList[chooseColumn][chooseRow] == " ":
            AscendPlay2(columnRowList,chooseRow)
            if winMoves2(columnRowList) == True:
                break
            Player = "Player1"
         
    blocks(columnRowList)
