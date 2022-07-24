# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('введите X: '))
y = int(input('введите Y: '))
z = int(input('введите Z: '))

first_statement = not((x or y) or z)
second_statement = ((not x and not y) and not z)
if first_statement == second_statement:
    print('Истинно')
else:
    print('Ложно')