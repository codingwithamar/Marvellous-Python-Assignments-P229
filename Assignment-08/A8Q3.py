#Author : codingwithamar@gmail.com
#Description : 'What is an IndentationError? When does Python raise this error?'

def main():
    age = 20

    if age >= 18:
        print("Eligible")      # Tab
        print("Can vote")     # Spaces
        print("Eligible to vote")

if __name__ == "__main__":
    main()


#TabError:inconsistent use of tabs and spaces in indentation