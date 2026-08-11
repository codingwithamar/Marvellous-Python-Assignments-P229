# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A27Q1.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-27\A27Q1.py
# Subject/Question : Write a Python program to implement a class named BookStore 
# with the following specifications:
# Description : 
#• The class should contain two instance variables:
#    ◦ Name (Book Name)
#    ◦ Author (Book Author)
#• The class should contain one class variable:
#    ◦ NoOfBooks (initialize it to 0)
#• Define a constructor (__init__) that accepts Name and Author and initializes instance variables.
#• Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is created.
#• Implement an instance method:
#    ◦ Display() – should display book details in the format:
#        <BookName> by <Author>. No of books: <NoOfBooks>
"""
Example usage:
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display() # Linux System Programming by Robert Love. No of
books: 1

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display() # C Programming by Dennis Ritchie. No of books: 2
"""
# =============================================================================

class BookStore:
    NoOfBooks = 0
    def __init__(self,Book_Name,Book_Author):
        self.Book_Name = Book_Name           #Instance Varibale
        self.Book_Author = Book_Author       #Instance Varibale

    NoOfBooks = NoOfBooks+1

    def Display(self):
        print(f"{self.Book_Name} by {self.Book_Author}. No of books: {BookStore.NoOfBooks}")


def main():
    print("--BOOK STORE DETAILS--")

    Obj1 = BookStore("Linux System Programming", "Robert Love")
    Obj1.Display() 

    Obj2 = BookStore("C Programming", "Dennis Ritchie")
    Obj2.Display()

if __name__ == "__main__":
    main()