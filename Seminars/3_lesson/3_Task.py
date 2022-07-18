# Реализуйте алгоритм задания случайных чисел без использования встроенного
# генератора псевдо случайных чисел.

import time
def milli_time():
    return round(time.time())

x = milli_time() % 100
y = milli_time() % 10
xy = x * y

size = int(input('введите размер: '))
listt = []
t = size/2 * x

for i in range(size):
    listt.append(round(t * x * y * xy // 100, 3))
    t = t * (t * x * y * xy // 100) + 1 // 100

print(listt)

