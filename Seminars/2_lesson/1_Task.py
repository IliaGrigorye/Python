# Напишите программу, которая принимает на вход число N и выдает последовательность из N членов
# Пример: N = 5: 1, -3, 9, -27, 81


number = int(input('Введите N: '))

def list_form(number: int):
    list_n = []
    for i in range (0, number):
        list_n.append((-3)**i)
    return list_n
print(list_form(number))