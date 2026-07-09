#Author : codingwithamar@gmail.com
#Description : 'Write a program which accepts one number and prints cube of that number'

def cube():
    print("Enter the value for square :")
    value = int(input())
    print(value ** 3)       #Way1
    print(pow(value,3))     #Way2

def main():
    cube()

if __name__ == "__main__":
    main()
    
    