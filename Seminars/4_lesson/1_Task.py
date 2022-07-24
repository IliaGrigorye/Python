# Cчитать строку из файла. Задайте строку из набора чисел. Напишите программу, которая покажет большее
# и меньшее число. в качестве символа разделителя используйте пробел.

import os

def convert_int(str):
    return[int(x) for x in str.split()]

path = os.path.join('folder','file1Task.txt')

with open(path, 'r') as data:
    text = data.readline()

listt = convert_int(text)

print(listt)
print(max(listt))
print(min(listt))