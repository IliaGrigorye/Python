# Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input('Введите n: '))

def sequence(number: int):
    sequence = 1
    summ = 0
    i = 1
    list = []
    while i < number + 1:
        sequence = round((1 + 1/i)**i,2)
        summ += sequence
        list.append(summ)
        i += 1
    return list

print(sequence(number))