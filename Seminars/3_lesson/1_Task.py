# Задайте список. Напишите программу, которая определит, присутствует
# ли в заданом списке строк некое число


str_list = ['1213', 'efs', '234', 'adfa12', '332']

number = input('введите число: ')
a = False

for item in str_list:
    print(item)
    if item.__contains__(number):
        a = True
        break

print(a)





