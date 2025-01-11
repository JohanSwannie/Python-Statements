
# * WHILE STATEMENT - EXAMPLE 1

list1 = [5, 20, 18, 36, 22, 7, 13, 28, 34, 16]

def whileOne(num):
    while num < 20:
        if num in list1:
            print(f"Number {num} is present in list1")
        num += 1

whileOne(1)

# * WHILE STATEMENT - EXAMPLE 2

def whileTwo(num2):
    while True:
        if num2 < 4:
            break
        if num2 % 2 == 0:
            print(f"Number {num2} left with no remainder")
        num2 -= 3

whileTwo(18)

# * WHILE STATEMENT - EXAMPLE 3

import random

def whileThree():
    while True:
        nbr = int(input("Please enter a number between 5 and 10 "))
        rnum = random.randint(5, 10)
        if nbr == rnum:
            print("You have hit the Jackpot!")
            break
        else:
            tryAgain = input("You have missed it - Enter 'y' to try again or anything else to quit ")
            if tryAgain != 'y':
                break
            
whileThree()
                
            
        




        