# В файле находиться N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнить условие A[i] - 1 = A[i - 1]. найдите это число


import os

def convert_int(str):
    return[int(x) for x in str.split()]

path = os.path.join('folder','file1Task.txt')

with open(path, 'r') as data:
    text = data.readline()

listt = convert_int(text)

print(listt)

# for i in range(1, len(listt)):
#     if listt[i] - 1 != listt[i - 1]:
#         print(f"не хватает {listt[i] - 1}")

# def f(listt: list):
#     for i in range(1, len(listt)):
#         if listt[i] - 1 != listt[i - 1]:
#             return listt[i] - 1

f = lambda i: listt[i] - listt[i - 1] != 1
x = tuple(filter(f, range(1, len(listt))))
print(x[0] + 1)

