# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A29Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-29\A29Q3.py
# Subject/Question : Copy File Contents into a New File (Command Line) 
# Write a program which accepts an existing file name through command line arguments,
# creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt. 
# Description : Input (Command Line): ABC.txt 
# Expected Output: Create Demo.txt and copy contents of ABC.txt into Demo.txt
# =============================================================================

import os

def main():
    FileName = input("Enter Existing File Name : ")
    ExistingFile = open(FileName,"r")

    ExistingData = ExistingFile.read()

    DestinationFile = open("Demo.txt","w")

    DestinationFile.write(ExistingData)

    print("File data Create and Write Successfully")

if __name__ == "__main__":
    main()
    