# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них
# Пример: 1, 4, 5, 6, 10 -> 10

a = []
for i in range(5):
    x = int(input('введите число '))
    a.append(x)

maxx = a[0]

for i in range(1, len(a)):
    if a[i] > maxx:
        maxx = a[i]
print(a,'->', maxx)