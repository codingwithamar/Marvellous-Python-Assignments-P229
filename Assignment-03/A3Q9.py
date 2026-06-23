"""What is the difference between:
x = 10
x = “Ten"
Is this allowed? Why?"""


x = 10 
print("In case of int : ", x)
print(id(x))
print(type(x))

x = "Ten"
print("In case of str : ", x)
print(x)
print(id(x))
print(type(x))
