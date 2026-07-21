# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A17Q6.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-17\A17Q6.py
# Subject : 6. Write a program which accept one number and display below pattern
# Description : Input : 5
#Output : * * * * *
#         * * * *
#         * * *
#         * *
#         *
# =============================================================================

def main():
    print("Enter the number : ")
    Value = int(input())

    for i in range(Value,0,-1):
        print(" * " * i)

if __name__ == "__main__":
    main()