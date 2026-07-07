#Author : codingwithamar@gmail.com
#Description : 'What is the difference between local variables and global variables?'

value1 = 10         #Global variable

def demo1():
    value2 = 11     #Local variable

    print("inside function demo1 is : ", value1)    #10
    print("inside function demo1 is : ", value2)    #22

def demo2():
    print("inside function demo2 is : ", value1)    #10
#    print("inside function demo2 is : ", value2)    #Error

demo1()
demo2()