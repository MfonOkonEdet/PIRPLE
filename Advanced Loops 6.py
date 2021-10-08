""" Python Homework Assignment 6: Advanced Loops
Details:
Create a function that takes in two parameters: rows, and columns, both of which are integers.
The function should then proceed to draw a playing board (as in the examples from the lectures)
the same number of rows and columns as specified. After drawing the board, your function should return True.
Extra Credit:
Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping.
If someone passes a value greater than either maximum, your function should return False """


# | | 0
#-----1
# | | 2
#-----3
# | | 4
#12345

def myGame(row, columns):
    maxHeight = 5
    maxWidth = 6 
    for row in range(5):
        if row % 2 == 0:
            for columns in range(1, 6):
                if columns % 2 == 1:
                    if columns != 5:
                        print(" ", end="")
                    else:
                        print(" ")
                else:
                    print("|", end="")
        else:
            print("-----")
    if row <= maxHeight and columns <= maxWidth:
        return True
    else:
        return False
 
print(myGame(5, 6))