# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

listt = [2, 12, 50, 1, 0, 29, 11]
sum = 0

for i in range(len(listt)):
    if i % 2 != 0:
        sum += listt[i]

print(listt)
print(sum)