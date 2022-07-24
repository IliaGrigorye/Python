# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

listt = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {listt}")

new_listt = []
for i in listt: 
    if i not in new_listt:
        new_listt.append(i) 

print(f"Список из неповторяющихся элементов: {new_listt}")