#Author : codingwithamar@gmail.com
#Description : 'Write a program which accepts one number and prints square of that number'

def sqr():
    print("Enter the value for square :")
    value = int(input())
    print(value ** 2)       #Way1
    print(pow(value,2))     #Way2

def main():
    sqr()

if __name__ == "__main__":
    main()
    