import random
from itertools import groupby

# Task 1
# a = []
# i = 0
# range(10)
# while i < 10: # кількість ітерацій
#     i = i + 1
#     x = random.randint(1, 10) # генерація випадкового числа від 1 до 10
#     a.append(x) # додати число в список
# print(a) # вивід першого списку з 10 випадкових цифр від 1 до 10
# print(max(a)) # вивід максимального числа зі списку

# Task 2
# a = []
# b = []
# i = 0
# range(10)
# while i < 10:
#     i = i + 1
#     x = random.randint(1, 10)  # генерація випадкового числа від 1 до 10
#     y = random.randint(1, 10)
#     a.append(x)  # додати число в список
#     b.append(y)  # додати число в список
# print(a)  # вивід першого списку з 10 випадкових цифр від 1 до 10
# print(b)  # вивід першого списку з 10 випадкових цифр від 1 до 10
# print(list(set(a + b)))  # створення та третього списко з першого та другого без дублів

# Task 3
a = list(range(1,101))
b=[]
print(a)
i = 0
range(101)
while i < 100:
    i = i + 1
    if (i % 7 == 0) and not (i % 5 == 0): # числа, які діляться на 7, але не кратні 5,
        b.append(str(i))
print('  '.join(b))
