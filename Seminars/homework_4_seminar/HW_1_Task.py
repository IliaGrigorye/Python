# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

d = int(input('введите число цифр после запятой: '))

n = pi
print(n)

n = 20000000
mypi = 4 * (sum(1/x for x in range(1, n + 1, 4)) +
sum(-1/x for x in range(3, n + 1, 4)))

print(round(mypi, d))