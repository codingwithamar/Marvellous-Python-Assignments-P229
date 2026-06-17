"""
3. What does the id() function return?
Is the value returned by id() same for two variables holding the same value?
"""

#Declaration
age = 11     
marks = 21
no = 11

print("\n----Step 1 : See the variable and object id(memory address) and type----")
print("Age is :", age)
print("Type is : ", type(age))
print("Address is : ", id(age))

print("Marks is :", marks)
print("Type is : ", type(marks))
print("Address is : ", id(marks))

print("No is :", no)
print("Type is : ", type(no))
print("Address is : ", id(no))

print("\n-----------Step 2 : update no = 11 to 9.8 and see the changes-----------")
no = 9.8
print("Age is :", age)
print("Type is : ", type(age))
print("Address is : ", id(age))

print("Marks is :", marks)
print("Type is : ", type(marks))
print("Address is : ", id(marks))

print("No is :", no)
print("Type is : ", type(no))
print("Address is : ", id(no))

print('''\nNote : \nWe see After updation if object available in another then point to that location 
otherwise alloacte new memory and here dynamically variable type can change''')

print("\n-----------Step 3 : update age = 11 to 12 and see the changes-----------")
age = 12
print("Age is :", age)
print("Type is : ", type(age))
print("Address is : ", id(age))

print("Marks is :", marks)
print("Type is : ", type(marks))
print("Address is : ", id(marks))

print("No is :", no)
print("Type is : ", type(no))
print("Address is : ", id(no))

print('''Note : \nHere we see if we update objects value and no one point that memory addrees mean
referenece count is zero then memory was released and updated value store in new address place''')
