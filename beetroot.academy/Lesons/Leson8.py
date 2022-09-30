# функція
# def is_valie(value):
#     if value is None:
#         print("None")
#     elif value:
#         print("True")
#     else:
#         print("False")
# print(None)
# print(True)
# print(False)
# is_valie(0)
# is_valie(0.0)
# is_valie([])
# is_valie({})
# is_valie(0)
# is_valie(())
# is_valie(set())
# is_valie(3)
# is_valie(-3)
# is_valie("")
# is_valie("+")
# is_valie(" ")

# a=1
# b=2
# c=3
# def temp(a, b, c):
#     print(f'a: {a}')
#     print(f'b: {b}')
#     print(f'c: {c}')
#     #return None
# temp(a, b, c) # print неивикористовувати щоб не виводилось None

# def temp(a, b, c, *args):
#     print(f'a: {a}')
#     print(f'b: {b}')
#     print(f'c: {c}')
#     print(args)
# temp('sdfdsfsd', False, 12, 45, 21, 8, 4, 'fd', True) # переводе в дуплекс

# def temp(a, b, c, **kwargs):
#     print(f'a: {a}')
#     print(f'b: {b}')
#     print(f'c: {c}')
#     print(kwargs)
# temp('sdfdsfsd', False, 12, test_1=45, test_2='aaa', test_3=21, test_4=8, test_5=4, test_6='fd',
#      test_7=True)  # переводе в словник

# lambda - Aнонімні функції
# print((lambda x, y: x + y)(4, 5))
# def add (x, y):
#     return  x+y
# print(add(4,5))

# months = [(1, "January"), (5, 'May'), (4, "April")]
# print(sorted(months, key=lambda x: x[0]))

# {'h': ASCII}
# def convert(string):
#     codes = {}
#     for ch in string:
#         if not ch in codes:
#             codes[ch]=ord(ch)
#     return  codes
# s= input("Please enter str: ")
# print(convert(s))

# чи число є просте
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# def main():
#     value = int(input('Plase enter the number: '))
#     if is_prime(value):
#         print(f'{value} - is prime number')
#     else:
#         print(f'{value} - is not prime number')
# main()

# func(minutes=50, days=1)) => задачка кількість секунд в задоних параметрах
# def to_seconds(seconds=0, minutes=0, hours=0, days=0, weeks=0):
#     seconds_in_minutes = 60
#     seconds_in_hours = 60 * seconds_in_minutes
#     seconds_in_days = 24 * seconds_in_hours
#     seconds_in_weeks = 7 * seconds_in_days
#
#     return seconds + minutes * seconds_in_minutes + \
#            hours * seconds_in_hours + \
#            days * seconds_in_days + \
#            weeks * seconds_in_weeks
#
#
# print((to_seconds(minutes=50, days=1)))

import  random
number =['i', 'j']
print(number)
i = random.randint(1,10)
j = i * i
print(i)
print(j)
# del number[0]
number.append(0, i)
# del number [0]
number.append(0, j)
print(list.number)


