# Найдите корни квадратного уравнения Ax^2 + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождние квадратного уравнения
# 2) с помощью дополнительных библиотек Python
# import math
# D=b^2-4ac
# Dk = math.sqrt(D) или D**0.5
# x = (((-b(+-)(c^0.5))/(2*a))

import os
path = os.path.join('folder','file2Task.txt')

def convert_int(str):
    return[int(x) for x in str.split()]

with open(path, 'r+') as data:
    # text = data.read()
    a = int(data.readline())
    b = int(data.readline())
    c = int(data.readline())

# number = convert_int(text)

# D = number[1]**2 - 4 * number[0] * number[2]
D = b**2 - 4 * a * c
# X1 = (-number[1] + D**0.5)/(2 * number[0])
X1 = (-b + D**0.5)/(2 * a)
# X2 = (-number[1] - D**0.5)/(2 * number[0])
X2 = (-b - D**0.5)/(2 * a)

print(X1, X2)

# with open(path, 'a') as data:
#     data.write(f'\nКорень 1: {X1}')
#     data.write(f'\nКорень 1: {X2}')