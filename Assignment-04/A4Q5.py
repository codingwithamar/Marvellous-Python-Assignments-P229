"""
Predict the output:
s = "Python"
print(id(s))
s = s + "3"
print(id(s))
Explain the reason for change / no change in id().
"""

s = "Python"
print(id(s))
s = s + "3"
print(id(s))

#in python if variables value update then python PVM allocate new memory space while
#address changed old address memory get pointless and garbage collector release memory space