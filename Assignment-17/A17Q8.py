# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A17Q8.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-17\A17Q8.py
# Subject : 8. Write a program which accept one number and display below pattern.
# Description : Input : 5   Output : 
#   1
#   1 2
#   1 2 3
#   1 2 3 4
#   1 2 3 4 5
# =============================================================================

def main():
    print("Enter the value")
    Value = int(input())

    for i in range(1,Value+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    main()
    