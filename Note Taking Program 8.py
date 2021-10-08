# Note-Taking Program 8

""" Details:
Create a note-taking program. When a user starts it up, it should prompt them for a filename.
If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file. After they enter the text, it should save the file and exit.
If they enter a file name that already exists, it should ask the user if they want:
A) Read the file
😎 Delete the file and start over
C) Append the file
If the user wants to read the file it should simply show the contents of the file on the screen. If the user wants to start over then the file should be deleted and another empty one made in its place. If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file. """

import os.path

NotePadList = ["James","John","Ken"]
NotePadFile = open("Notepad.txt","w")
for tempNotePad in NotePadList:
    NotePadFile.write(tempNotePad + "\n")
NotePadFile.close()

#For Existing Filename
Start = input("File Name: ")

if os.path.isfile(Start):
    Request = input("Please Choose:\n" + "A) Read the File\n" + "B) Delete File and Start Over\n" + "C) Append File\n" + "D) Replace a Single Line\n" + "Response: ")
    if Request == "A":
        NotePadFile = open("Notepad.txt","r")
        print(NotePadFile.read())
        NotePadFile.close
        print("\n******** DISPLAYED ALL FILE CONTENT ********")
    elif Request == "B":
        os.remove("Notepad.txt")
        print("\n******** FILE DELETED SUCCESSFULLY! ********")
        newFile = input("Please create a Filename: ")
        newFileName = open(newFile,"w")
        newFileName.write("")
        newFileName.close()
        print("\n******** NEW FILE SAVED! ********")
    elif Request == "C":
        AppendTxt = input("Append Text: ") 
        NotePadFile = open("Notepad.txt","a")
        NotePadFile.write(AppendTxt)
        NotePadFile.close()
        AppendFile = open("Notepad.txt","r")
        print(AppendFile.read())
        NotePadFile.close()
        print("\n******** ADDED THANK YOU! ********")
    elif Request == "D":
        LineNumb = int(input("Line number to update: "))
        counter = LineNumb
        if (True):
            counter -= 1
            with open("Notepad.txt","r") as NotePadFile:
                line = NotePadFile.readlines()
                line[counter]= input("Text to replace: ") + "\n" 
            with open("Notepad.txt","w") as File:
                for tempLine in line:
                    File.write(tempLine)
            with open("Notepad.txt","r") as File:
                for readFile in File:
                    ReadFile = readFile.strip("\n")
                    print(ReadFile)
        print("\n******** LINE REPLACED! ********")
            
#For Non-Existing Filename
else:
    WriteText = input("Enter Text: ")
    NewFile = open("NewFile.Txt","w")
    NewFile.write(WriteText)
    NewFile.close()
    NewFile = open("NewFile.txt","r")
    print(NewFile.read())
    NewFile.close()



    



