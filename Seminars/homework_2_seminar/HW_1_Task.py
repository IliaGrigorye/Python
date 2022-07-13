# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input('Введите число: ')

def sum_number(number):
    number = list(number)
    
    if ',' in number:
        number.remove(',')
    if '-' in number:
        number.remove('-')

    print(sum(map(int, number)))

sum_number(number)

