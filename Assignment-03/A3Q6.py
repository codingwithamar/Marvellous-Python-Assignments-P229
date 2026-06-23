"""
Write a program to display:
• Data type
• Memory address
• Size in bytes
of a variable entered by the user.
"""
import sys
var = eval(input("enter the variable : "))
print("User Entered Variable is  : ", var)
print("User Entered Variable Data Type is : ", type(var))
print("User Entered Variable memory address is : ", id(var))
print("User Entered Variables Size is : ", sys.getsizeof(var))
