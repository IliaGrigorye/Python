# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
import os
path1 = os.path.join('folder','file2-1Task.txt')
path2 = os.path.join('folder','file2-2Task.txt')

with open(path1, 'r') as data:
    text1 = data.readline()

def coding(txt):
    count  =  1
    res = ''
    for i in range (len(txt) -1):
        if txt [i] == txt[i+1]:
            count  += 1
        else:
            res += str(count) + txt[i]
            count  =  1
    if  1 > 1 or (txt[len(txt)-2] != txt[-1]):
        res += str(count) + txt[-1]
    return res

def decoding(txt):
    number  = ''
    res = ''
    for i in range (len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

with open(path2, 'w') as data:
    data.write(f'{coding(text1)}')

print(f"Текст после кодировки: {coding(text1)}")
print(f"Текст после дешифровки: {decoding(coding(text1))}")