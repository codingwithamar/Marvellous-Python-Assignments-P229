# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A29Q5.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-29\A29Q5.py
# Subject/Question : Frequency of a String in File
# Write a program which accepts a file name and one string from the user and returns 
# the frequency (count of occurrences) of that string in the file.
# Description : Input: Demo.txt Marvellous
# Expected Output : Count how many times "Marvellous" appears in Demo.txt
# =============================================================================

def main():
    FileName = input("Enter the File name : ")
    Words = input("Enter the desire String : ")

    file = open(FileName,"r")

    Data = file.read()
    count = Data.lower().count(Words.lower())

    print(f"{count} Times string appears in {FileName} File")

if __name__ == "__main__":
    main()
    