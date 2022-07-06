
# ----типы данных и переменная
# ----int, float, boolean, str, list, None

# value = None
# print(type(value))

# a = 123
# b = 1.23
# print(type(a))
# print(type(b))

# value = 12334
# print(type(value))

# s = 'hello world'
# print(s) #вывод строки

# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# r = False
# print(f)
# print(r)

# list = ['1', '2', '3']
# col = ['hello', 1,2,4.5,True]
# print(list)
# print(col)

# --------------------------------------------------------------------------------

# ----Ввод и вывод данных
# ----print, input

# print('Введите a:');
# a = int(input()) # можно float
# print('Введите b:');
# b = int(input())
# print(a, '+', b, '=', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# ----------------------------------------------------------------------------------------

# ----Арифметические операций
# ----+, -, *, /, %, //, **
# ----(), Сокращенные операции

# a = 10
# b = 5
# c = a + b # сложение
# print(c)
# c = a - b # вычитание
# print(c)
# c = a / b # деление float
# print(c)
# c = a * b # умножение
# print(c)
# c = a // b # деление int
# print(c)
# c = a % b # остаток от деления
# print(c)
# c = a ** b # a в степени b
# print(c)

# a = 1.3
# b = 3
# c = a * b
# print(c)
# c = round(a * b, 3)
# print(c)

# a = 3
# a += 5
# print(a)

# --------------------------------------------------------------------------

# Логические операций
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

# a = 1 < 4 
# print(a)
# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 > 4 and 5 < 2
# print(a)
# a = 1 > 4 and 5 > 2
# print(a)
# a = 1 == 4
# print(a)
# a = 1 != 4
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)
# a = [1,2]
# b = [1,2]
# print(a == b)

# a = 3 < 5 < 8 < 10
# print(a)
# func = 1
# T = 4
# x = 2
# print(func < T > x)

# f = 1 > 2 or 4 < 6 # хотя бы одно истина
# print(f)

# f = [1,2,3,4] # есть ли число в f
# print(f)
# print(2 in f)
# print(not 2 in f)

# is_odd = f[0] % 2 == 0
# print(is_odd)
# is_odd = not f[0] % 2
# print(is_odd)

# ---------------------------------------------------------------------------------

# Управляющий конструкций
# if, if-else, while, for

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a, 'больше', b)
# else:
#     print(b, 'больше', a)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждал Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ :3')
# else:
#     print('Привет, ', username)

# orig = 23
# inver = 0
# while orig != 0:
#     inver = inver * 10 + (orig % 10)
#     orig //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inver)

# for i in 1,2,3,4,5:
#     print(i**2)
# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i)
# list = range(10)
# for i in list:
#     print(i)
# for i in range(10):
#     print(i)
# for i in range(1, 6):
#     print(i)
# for i in range(1, 17, 2):
#     print(i)
# for i in 'q we - rt y':
#     print(i)

# help(int) # Помощь

# text = 'съешь еще этих мягких французcких булок'
# print(len(text))                    # длина
# print('еще' in text)                # поиск в тексте
# print(text.isdigit())               # проверка все ли символы числа
# print(text.islower())               # проверка все ли символы нижнего регистра
# print(text.replace('еще','ЕЩЕ'))    # замена

# text = 'съешь еще этих мягких французcких булок'
# print(text[0])                  # первая буква в тексте
# print(text[1])                  # вторая буква
# print(text[len(text)-1])        # Последняя буква
# print(text[-5])                 # пятая буква с конца
# print(text[:])                  # печать текста от начало и до конца
# print(text[0:6])                # печать от одного до другого 
# print(text[6:-17])              # печать от одного до другого 

# ---------------------------------------------------------------------------------

# Списки: введение
## list = list

# numbers = [1, 2, 3, 4, 5]
# print(numbers)                  # печать всего списка
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)             # замена типа range на list
# print(type(numbers))

# print(numbers)                  # 1 2 3 4 5
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)                  # 10 2 3 4 5

# for i in numbers:
#     i *= 2
#     print(i)                    # 20 4 6 8 10
# print(numbers)                  # 10 2 3 4 5

# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)                                        # red green blue

# for e in colors:
#     print(e*2)                                      # redred greengreen blueblue

# colors.append('gray')                               # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'])   # true
# colors.remove('red') #del colors [0]                # удаление элемента

# -----------------------------------------------------------------------------

# Функций
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))
print(type(f(arg)))

arg = 2.3
print(f(arg))
print(type(f(arg)))

arg = 2
print(f(arg))
print(type(f(arg)))