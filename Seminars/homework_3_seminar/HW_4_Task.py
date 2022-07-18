# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('введите число: '))

def binar_n (number: int):
    binary_number = []
    while number != 0:
        binary_number.append(number % 2)
        number //= 2

    revers = []
    for i in reversed(binary_number):
        revers.append(i)
    
    return revers

print(number, '->', int(''.join(map(str, binar_n(number)))))