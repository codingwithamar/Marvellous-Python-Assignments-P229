# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A28Q5.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-28\A28Q5.py
# Subject/Question : Search a Word in File 
# Write a program which accepts a file name and a word from the user and 
# checks whether that word is present in the file or not. 
# Description : Input: Demo.txt Marvellous 
# Expected Output: Display whether the word Marvellous is found in Demo.txt or not.
# =============================================================================

def main():
    Filename = input("Enter the file name : ")
    Word = input("Enter the finding Word : ")

    file = open(Filename,"r")

    Data = file.read()
    count = Data.lower().count(Word.lower())

    if count > 0:
        print(f"{Word} word found in file {count} times")

    else:
        print(f"{Word} Word not found in file")

    file.close()

if __name__ == "__main__":
    main()
    