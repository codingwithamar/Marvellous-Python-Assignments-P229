# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A29Q4.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-29\A29Q4.py
# Subject/Question : Compare Two Files (Command Line)
# Write a program which accepts two file names through command line arguments and 
# compares the contents of both files.
#   • If both files contain the same contents, display Success
#   • Otherwise display Failure
# Description : Input (Command Line): Demo.txt Hello.txt 
# Expected Output: Success OR Failure
# =============================================================================

import sys

def main():

    File1 = open(sys.argv[1],"r")
    File2 = open(sys.argv[2],"r")

    Data1 = File1.read()
    Data2 = File2.read()

    if Data1 == Data2:
        print("Success")
    else:
        print("Failure")

    File1.close()
    File2.close()

if __name__ == "__main__":
    main()
    