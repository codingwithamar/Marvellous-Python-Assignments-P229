"""What is the range data type in Python?
How is it different from a list of numbers?
"""

import sys

a = range(5)          
b = range(2, 8)       
c = range(0, 10, 2)   
d = range(10, 0, -1)  

print("\nlist of A :",list(a))    # 0, 1, 2, 3, 4
print("list of B :",list(b))    # 2, 3, 4, 5, 6, 7
print("list of C :",list(c))    # 0, 2, 4, 6, 8
print("list of D :",list(d))    # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

print("\n",type(a))  #<class 'range'>
print(type(b))  #<class 'range'>
print(type(c))  #<class 'range'>
print(type(d))  #<class 'range'>

r = range(1_000_000)
l = list(range(1_000_000))

print("\nmemory size of r : ",sys.getsizeof(r),"Bytes")
l_size = print("memory size of l : ",sys.getsizeof(l),"Bytes")
in_MB = sys.getsizeof(l)
print(in_MB/(1024*1024),"MB")
