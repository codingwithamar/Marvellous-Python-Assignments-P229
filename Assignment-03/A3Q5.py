"""
What is the difference between:
print() and return
Explain with function example.
"""

def madam(a, b):
    print(a + b)    #Display Output - madam ne board var value lihun dakhavali pan aplyala dili nahi

def sir(a, b):
    return a - b    #send value to caller - siranni ne value dakhavali nahi pan eka kagdavar lihun dili

MadamchiBook = madam(10, 20)    #madam ne value board var dakhavali pan aplyala lihun dili nahi tyamule aplya vahit kahich nahi ahe
SiranchiBook = sir(30, 10)     #siranni bookmadhe value lihun dili tyamule to kagad aplyakade aahe ani tyat value aahe

print("Madamchi Book : ", MadamchiBook)   #madam fakt dakhavali tyamule aplyakade kahich nahi - none 
print("Siranchi Book : ", SiranchiBook)   #siranni kagad dilaay tyat value aahe ti apan pahili - 

print("Siranchi Value + 1 : ", SiranchiBook + 1) #siranchi value reuse keli
print(MadamchiBook + 1) #madamachi valuech nahi tyamule usech nahi honar    #Error