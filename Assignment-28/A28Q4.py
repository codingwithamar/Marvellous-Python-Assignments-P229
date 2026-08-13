# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A28Q4.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-28\A28Q4.py
# Subject/Question : Copy File Contents into Another File 
# Write a program which accepts two file names from the user. 
#   • First file is an existing file 
#   • Second file is a new file 
# Copy all contents from the first file into the second file. 
# Description : Description
# =============================================================================

def main():
    Filename1 = input("Enter the Name of File1 : ")
    Filename2 = input("Enter the Name of File2 : ")

    file1 = open(Filename1,"r")
    Data1 = file1.read()

    file2 = open(Filename2,"w")
    Data2 = file2.write(Data1)

    print("Wrote data is String count is : ",Data2)

    file1.close()
    file2.close()

if __name__ == "__main__":
    main()
