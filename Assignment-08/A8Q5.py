#Author : codingwithamar@gmail.com
#Description : 'How does Python internally identify the start and end of a code block using indentation?'

def main():
    x = 10

    if x > 0:
        print("Positive")

        if x > 5:
            print("Greater than 5")

        print("Done")

    print("End")

if __name__ == "__main__":
    main()
    