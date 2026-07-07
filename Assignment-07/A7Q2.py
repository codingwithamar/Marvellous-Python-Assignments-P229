#Author : codingwithamar@gmail.com
#Description : Why should excessive use of global variables be avoided in large programs?

value = 10

def increment():
    global value
    value = value + 10  # except 20

def decrement():
    global value
    value = value - 5   #except 5

increment()
decrement()

print(value)    #but answer is 15