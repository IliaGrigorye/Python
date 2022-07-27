# lambda - анонимные функций
# list comprehension - генератор
# map - применяет функцию с выражением к элементам
# filter - применяет функцию с логическим выражением к элементам
# zip - комбинирует коллекций
# enimerate - номерует
# -----------------------------

# f = lambda x: x**2
# print(f(20))

# -----------------------------

# def f(x):
#     return x**2

# new_f = lambda x: True if (x > 10) else False
# new_f = lambda x: x**2
# my_list = [12, 24, 3564, 345, 4]

# for item in my_list:
#     print(f(item), end = ' ')

# res = list(map(new_f, my_list))
# print(res)

# -----------------------------

# что делать, с чем делать, условие
# my_list = [int(input('-> ')) for i in range(5)]
# print(my_list)
# listt = tuple([(i, i) for i in range(1, 21) if (i % 2 == 0)])
# print(listt)

# -----------------------------

# my_list = list(filter(lambda x: x > 10, [123, 12123, 4545, 32, 12, 1, 4]))
# print(my_list)
# my_list = list(filter(lambda x: type(x) == int, [123, 12123, 4545, 32, 12, 1, 4]))
# print(my_list)

# -----------------------------

# name = ['a', 'b', 'c']
# money = [123, 346, 1234]

# my_list = list(zip(name, money))

# print(my_list)

# -----------------------------

# name = ['a', 'b', 'c']

# my_list = list(enumerate(name))

# print(my_list)
