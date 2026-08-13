# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A29Q1.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-29\A29Q1.py
# Subject/Question : Check File Exists in Current Directory
# Write a program which accepts a file name from the user and checks whether that 
# file exists in the current directory or not.
# Description : Input: Demo.txt
# Expected Output: Display whether Demo.txt exists or not.
# =============================================================================

import os

def main():
    FileName = input("Enter the File Name : ")
    File = os.path.exists(FileName)

    if (File == True):
        print("File is Exist")
    else:
        print("File Not Exist")


if __name__ == "__main__":
    main()
    