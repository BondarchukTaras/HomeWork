from datetime import datetime
import random

# Task 1
# import random
#
# print('Try to guess the number from 1 to 10')
# numeric = int(input())
# a = random.randint(1, 2)  # випадкове число в діапазоні 1-10
# print(a)
# if numeric == a:
#     print("You guessed it")
# else:
#     print("You didn't guess")

# Task 2
# print('Hello what is you name?')
# name = input()
# print('How old are you?')
# age = int(input())
# age = age + 1
# print("Hello", name, "on your next birthday you’ll be", age, "years")

# print('Hello what is you name?')
# name = input()
# print('Enter your year of birth')
# year = input()
# print('Enter your birth month')
# month = input()
# print('Enter your birthday')
# day = input()
# age = year + "." + month + "." + day
# birthday = datetime.strptime(age, '%Y.%m.%d')
# f = ("2023" + "." + month + "." + day)
# f = datetime.strptime(f, '%Y.%m.%d')
# print("Hello", name, "on your next birthday you’ll be", f.year - birthday.year, "years")

# Task 3

def WithoutRepeat(length):
    letters = 'hello'
    result = ''.join((random.sample(letters, length)))
    print("Randomly generated string is: ", result)
WithoutRepeat(5) # define the length
WithoutRepeat(5)
WithoutRepeat(5)
WithoutRepeat(5)
WithoutRepeat(5)