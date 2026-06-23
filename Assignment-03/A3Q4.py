"""
Write a function that does not return anything but prints a message.
Explain the default return value of such a function.
"""

def display():
    print("Inside Display Function")

result = display()

print("Return Value is : ", result)
print(type(result))

"""
OUTPUT :
Inside Display Function
Return Value is :  None
<class 'NoneType'>
"""