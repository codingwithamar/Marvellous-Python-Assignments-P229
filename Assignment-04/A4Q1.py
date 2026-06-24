"""What is the difference between List and Tuple in Python? 
Explain in terms of:
• Mutability
• Memory
• Performance
• Use cases
"""
import sys, timeit
print("-------------------------------------List------------------------------------------")
print('''A list is an ordered collection used to store multiple values in a single variable,
and it allows modification after creation.\n''')

lst = [10,20.50,True,"Amar"]        #mixed data type allowed
print("Our List :", lst)                                #Ordered collection
print("Data type of list :", type(lst))                 #type is list
print("Memory size of list :", sys.getsizeof(lst))      #Use more memory 
lst[0] = 100                                            #Mutable(can Modified)
lst.append(40)                                          #Use case - modification is allowed
lst.remove("Amar")                                      #Deletion is Allowed
lst_time = timeit.timeit("[10,20.50]", number=1000000)  #Measure execution time
print("Execution time is :", lst_time)                  #Slower 

print("\n-------------------------------------Tuple------------------------------------------")
print("A tuple is similar to a list but is used when the data should not be changed after creation.\n")
tpl = (10,20.50,True,"Amar")
print("Our Tuple : ", tpl)
print("Data Type of tuple : ", type(tpl))
print("Memory Size of tuple : ", sys.getsizeof(tpl))
#tpl[0] = 100                                            #Unmutable (cannot Modified)
#tpl.append(40)                                          #Use case - modification is not allowed
#tpl.remove = ("Amar")                                   #Deletion also not allowed
tpl_time = timeit.timeit("[10,20.50]", number = 1000000) #Measure Execution Time
print("Execution Time is : ", tpl_time)                  #Faster

"""Note : timeit() is used to measure the execution time of a small piece of Python code.
It helps compare the performance of different code snippets."""