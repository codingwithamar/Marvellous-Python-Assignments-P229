# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A17Q7.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-17\A17Q7.py
# Subject : 7. Write a program which accept one number and display below pattern.
# Description : Input : 5
#Output : 
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
# =============================================================================

def main():
    print("Enter the Value")
    Value = int(input())

    for i in range(Value):
        for j in range(1,Value+1,1):
            print(j, end =" ")
        print()

if __name__ == "__main__":
    main()
    