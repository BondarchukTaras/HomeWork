from packege.foo import foo
print(foo('David'))

# varivant 1 без інформації в packege
# from packege.foo import foo
# from packege.baz.operation import minus, division
# from packege.bar.info import log
# print(foo('David'))
# print(minus(35, 5))
# print(division(44, 11))
# log('Hi friend')

# variant 2 з інформацією в packege
# from packege import foo, minus, division, log
# print(foo('David'))
# print(minus(35, 5))
# print(division(44, 11))
# log('Hi friend')

# variant 3 з інформацією в packege і зміною назви
# import packege as my_import
# print((my_import.foo('Devid')))
# print(my_import.minus(35, 5))
# print(my_import.division(44, 11))
# my_import.log('Hi friend')
# print(my_import.another_foo())

# from packege import *
# def division(x):
#     return x / 3
# if __name__ == '__main__':
#     print(foo('David'))
#     print(minus(35, 5))
#     print(division(44, 11))
#     log('Hi friend')
#     print(another_foo())
#     print((division_second(30)))
