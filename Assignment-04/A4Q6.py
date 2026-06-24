"""
What is a dictionary in Python?
Explain:
• Key value pair
• Why keys must be immutable
• Why duplicate keys are not allowed
"""

student ={"name" : "Amar Bhandare",     #str -> str
        "age" : 29,                     #str -> int
        "birth_date" : "10-02-1996",    #str -> str
        "marks" : [80,70,40,20]} 
print(student)   # {'name': ‘Amar Bhandare', 'age': 29} 
print(type(student))            # <class 'dict'>
print(type(student.values()))   # <class 'dict_values'>
student

print('''
Property              Rule                    Reason
Keys            Must be immutable       Hashing requires a stable, unchanging value
Keys            Must be unique          Hash table maps one key → one memory slot
Values          Can be any type         No hashing needed; just stored data
Values          Can be duplicated       Two keys can point to the same value — no conflict
    ''')

