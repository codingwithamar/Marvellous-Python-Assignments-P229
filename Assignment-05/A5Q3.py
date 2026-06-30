data1 = bytes([65, 66, 67])
data2 = bytearray([65, 66, 67])

print(data1)
print(data2)

print(type(data1))
print(type(data2))

#try to Modify
data1[0] = 68   #Error
data2[0] = 68

#bytes → Immutable (cannot be modified after creation) 
#bytearray → Mutable (can be modified after creation)

