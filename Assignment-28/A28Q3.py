# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A28Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-28\A28Q3.py
# Subject/Question : Display File Line by Line 
# Write a program which accepts a file name from the user and displays the contents 
# of the file line by line on the screen.
# Description : 
# Input: Demo.txt 
# Expected Output: Display each line of Demo.txt one by one.
# =============================================================================

def main():
    Filename = input("Enter the Name of File : ")

    File = open(Filename,"r")

    Data = File.read()

    print("File Content : \n",Data)

    File.close()

if __name__ == "__main__":
    main()
