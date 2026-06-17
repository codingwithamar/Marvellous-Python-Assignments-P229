"""
2. What is the difference between: 
a = 10 
b = 10 
and 
a = [10] 
b = [10] 
Explain using id().
"""
print("-------------case 1----------------")
a = 10      
b = 10      
print(type(a), type(b))
print("a = ", a,"id = ",id(a))      
print("b = ", b,"id = ",id(b))
print("a and b refer to same object:", id(a) == id(b))      #if id match return bool True value

print("\n-------------case 2----------------")
a = [10]
b = [10]
print(type(a), type(b))
print("a = ", a,"id = ",id(a))
print("b = ", b,"id = ",id(b))
print("a and b refer to different object:", id(a) == id(b)) 


