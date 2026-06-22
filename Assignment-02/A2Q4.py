"""
4. What is the purpose of getsizeof()? 
Why is memory size different for different data types?
"""

import sys

x = 10
y = 3.14
name = "Python"
print("----Memory Size with Variable----")
print("Size of X(10) :", sys.getsizeof(x),"bytes")
print("Size of Y(3.14) :", sys.getsizeof(y),"bytes")
print("Size of Python(Str) : ", sys.getsizeof(name), "bytes")

print("\n----Memory Size without Variable(direct value)----")
print("Size of 10 :", sys.getsizeof(10), "bytes")
print("Size of 3.14 :", sys.getsizeof(3.14), "bytes")
print("Size of Boolean -True :", sys.getsizeof(True), "bytes")
print("Size of Python : ", sys.getsizeof("Python"),"bytes")
print("Size of List - 10,20,30 : ", sys.getsizeof([10,20,30]), "bytes")