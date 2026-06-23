def fun():      #function define, Allocate but not execute in first
    x = 10      #local variable
    print(x)    #print 10 and scope ended and function control return

fun()           #now called function goto control line no - 1
print(x)        #now try to print but "x" not found because x define inside local function due to scope ended he show error

"""
Code Flow - line 5 > 1 > 2(assign) > 3(print value of x) > 5(functuon return) > 6(try to print but cannot) > then show error
OUTPUT :
10
Traceback (most recent call last):
  File "C:\Users\Sumaney\Desktop\GitHub\Marvellous-Python-Assignments-P229\Assignment-03\A3Q3.py", line 6, in <module>
    print(x)
          ^
NameError: name 'x' is not defined
"""

"""
Explanation :
Local variables can be accessed only inside the function in which they are created.

code correction - 
def fun():
    x = 10
    return x

x = fun()

print(x)
"""