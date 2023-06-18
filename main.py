
import os
from functions import *




def main():
    balance = deposit()
    while True:
        print(f"Your balance is ${balance}")
        ans = input("Would you like to spin? (y/n) ")
        if ans == "y":
            balance += spin(balance)
        else:
            break

if __name__ == '__main__':
    main()




    