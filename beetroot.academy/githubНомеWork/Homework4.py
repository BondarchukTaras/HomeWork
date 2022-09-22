# Task 1
string = 'helloworld'  # 'my' 'x'
if len(string) == 1:
    print('Empty String')
elif len(string) == 2:
    print(string + string)
elif len(string) > 2:
    print(string[:2] + string[-2:])

# Task 2
# print('Enter you phone number') #запит на введення номеру телефона
# phone_number = input() #створення перемфнної
# if phone_number.isdigit() and len(phone_number) == 10: # перевірка умов що при введенні вказані лише цифри та довжина 10 символів
#     print(phone_number) #вивід введеного користувачем
# elif phone_number.isdigit() and len(phone_number) != 10:
#     print('The number of characters must be 10') #вивід повідомлення
# else:
#     print('The phone number must contain only "0123456789" and must be 10 characters long.') #вивід повідомлення

# Task 3
# print('How much will be: 1 + 1 = ?')
# mathematical_expression = '2'
# print('Enter the answer')
# answer = input()
# if mathematical_expression == answer:  # перевірка що очікуваний результат відповідає відповіді користувача
#     print('Yes')
# else:
#     print('No')

# Task 4
# name1 = 'taras'  # змінна з ім'ям
# print('Enter you name')  # запрос на введення
# name2 = input()  # створення перемінної з веденого користувачем
# name2 = name2.lower()  # переведення до нижнього регістру
# if name1 == name2.lower():  # перевірка на валідність данних
#     print('True')
# else:
#     print('False')
