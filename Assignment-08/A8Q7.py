#Author : codingwithamar@gmail.com
#Description : 'How does modular programming improve code reusability, testing, and maintenance?'

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
    