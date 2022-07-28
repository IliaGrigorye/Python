# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

listt = [2, 3, 4, 5, 6, 7]
listt_comp = []

# for i in range((len(listt) + 1) // 2):
#     listt_comp.append(listt[i] * listt[len(listt) - 1 - i])

[listt_comp.append(listt[i] * listt[len(listt) - 1 - i]) for i in range((len(listt) + 1) // 2)]

print(listt_comp)