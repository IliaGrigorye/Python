# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать 
# в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def write_file(st):
    with open('fileTask4.txt', 'w') as data:
        data.write(st)


def rand():
    return random.randint(0,101)


def create_coeff(k):
    listt = [rand() for i in range(k+1)]
    return listt
    

def create_polinom(sp):
    listt = sp[::-1]
    polinom = ''
    if len(listt) < 1:
        polinom = 'x = 0'
    else:
        for i in range(len(listt)):
            if i != len(listt) -  1 and listt[i] != 0 and i != len(listt) - 2:
                polinom += f'{listt[i]}x^{len(listt)-i-1}'
                if listt[i+1] != 0:
                    polinom += ' + '
            elif i == len(listt) -  2 and listt[i] != 0:
                polinom += f'{listt[i]}x'
                if listt[i+1] != 0:
                    polinom += ' + '
            elif i == len(listt) -  1 and listt[i] != 0:
                polinom += f'{listt[i]} = 0'
            elif i == len(listt) -  1 and listt[i] == 0:
                polinom += ' = 0'
    return polinom

k = int(input("Введите натуральную степень k = "))
coeff = create_coeff(k)
write_file(create_polinom(coeff))
