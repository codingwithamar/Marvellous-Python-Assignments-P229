#Author : codingwithamar@gmail.com
#Description : '1. Write a program which accepts one number and prints multiplication table of that number.'

def multi(Num):
    for i in range(Num, Num * 10, Num):
        i = Num + i
        print(i)

def main():
    print("Enter Number for Table : ")
    num = int(input())
    multi(num)

if __name__ == "__main__":
    main()
    