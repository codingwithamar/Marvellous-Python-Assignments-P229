# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A28Q1.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-28\A28Q1.py
# Subject/Question : Count Lines in a File
# Write a program which accepts a file name from the user and counts how many lines are present in the file. 
# Description : 
# Input: Demo.txt 
# Expected Output: Total number of lines in Demo.txt.
# =============================================================================

def main():
    Lines = []
    Filename = input("Enter the File Name : ")

    File = open(Filename,"r")

    for Line in File:       # radlines() predefine function is Available
        Lines.append(Line)

    print("Line Of file is : ",len(Lines))

    File.close()

if __name__ == "__main__":
    main()
    