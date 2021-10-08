""" Python Homework Assignment 7
Dictionaries and Sets
By: Mfon Okon Edet
'''

 Details:
 
 Return to your first homework assignments, when you described your favorite song. Refactor that code so all the variables are held as dictionary keys and value. Then refactor your print statements so that it's a single loop that passes through each item in the dictionary and prints out it's key and then it's value.


 Extra Credit:

 Create a function that allows someone to guess the value of any key in the dictionary, and find out if they were right or wrong. This function should accept two parameters: Key and Value. If the key exists in the dictionary and that value is the correct value, then the function should return true. In all other cases, it should return false. """

myFavSong = {"Artist":"Joeboy","Title":"Celebration","Album":"Baby","Genre":"Afrobeat","Year":"2020"}


for Key, Value in myFavSong.items():

    print(Key, ":", Value) # keyVal = Key and myFavSong[keyVal] = Value


def myDictionary(Key,Value):
    Key = input("Guess key:\n")
    Value = input("Guess Value:\n")
    if Key in myFavSong and myFavSong[Key] == Value:
        return True
    else:
        return False
        

print(myDictionary(Key, Value))




