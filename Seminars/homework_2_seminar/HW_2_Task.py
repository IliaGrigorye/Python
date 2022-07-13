# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите N: '))

def product_numbers(number: int):
    c = 1
    i = 1
    list = []
    while i < number + 1:
        c = c * i
        list.append(c)
        i += 1
    return list

print(product_numbers(number))
