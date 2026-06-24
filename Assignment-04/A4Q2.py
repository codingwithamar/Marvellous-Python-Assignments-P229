"""Why are tuples faster than lists?
In which real-world scenario would you prefer a tuple over a list?
"""

print("\nBoth tuple and list store multiple values, but tuples are" \
"generally faster because tuples are immutable,fixed size compare to list has"
"Append,update,insert, delete operation and that operation dynamically increased memory.\n")

print("Real life scenario use in below case")
location = (18.5204, 73.8567)       #logitude and lattitude are fixed value
dob = (15, 8, 1995)                 #Date of Birth is fixed not changed dynamically
employee = (101, "Amar", "Pune")    #employee name and id is fixed not change dunamically

print("Location : ",location)
print("DOB : ", dob)
print("Employee Primary Details : ", employee)

