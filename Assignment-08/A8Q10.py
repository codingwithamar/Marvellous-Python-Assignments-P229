#Author : codingwithamar@gmail.com
#Description : '10. Explain why Python modules are considered the foundation of scalable software design'

import account
import loan
import customer
import database

def main():
    database.connect()
    balance = 5000
    balance = account.deposit(balance, 2000)
    print(balance)
    print(loan.calculate_emi(100000, 0.08))
    customer.customer_info()    

if __name__ == "__main__":
    main()
    