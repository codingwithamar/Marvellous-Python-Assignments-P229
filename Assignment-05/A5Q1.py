"""
1.What are bytes in Python?
Why are they immutable?
"""
data = bytes([65, 66, 67])     #Storage format
#converting the character
print(chr(data[0]))     #A
print(chr(data[1]))     #B
print(chr(data[2]))     #C
#data[0] = 69       #Error
# Once a bytes object is created, its contents cannot be modified.

#Iterating over Bytes
data = b"ABC"
for value in data:
    print(value)
#65
#66
#67

