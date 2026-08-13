# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A29Q2.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-29\A29Q2.py
# Subject/Question : Display File Contents
# Write a program which accepts a file name from the user, opens that file, and 
# displays the entire contents on the console.
# Description : Input: Demo.txt 
# Expected Output: Display contents of Demo.txt on console.
# =============================================================================

def main():
    FileName = input("Enter the file Name : ")

    File = open(FileName,"r")

    FileData = File.read()

    print(FileData)

    File.close()

if __name__ == "__main__":
    main()
    