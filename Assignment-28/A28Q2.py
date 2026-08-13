# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A28Q2.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-28\A28Q2.py
# Subject/Question : ) Count Words in a File 
# Write a program which accepts a file name from the user and counts the total number of words in that file. 
# Description : Input: Demo.txt 
# Expected Output: Total number of words in Demo.txt.
# =============================================================================

def main():
    Filename = input("Enter the File name : ")

    FileObject = open(Filename,"r")

    Data = FileObject.read()
    Words = Data.split()
    print("Total Number Of Strings : ",len(Words))

    FileObject.close()

if __name__ == "__main__":
    main()