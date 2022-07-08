# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# Пример: x=34; y=-30 -> 4; x=2; y=4-> 1; x=-34; y=-30 -> 3;

x = int(input('введите кординату X: '))
y = int(input('введите кординату Y: '))

quarter_number = 0

if x == 0 and y == 0:
    print('x и y не должны ровняться 0')
elif x == 0 and y != 0:
    print('кордината находиться на оси Y')
elif x != 0 and y == 0:
    print('кордината находиться на оси X')
elif x > 0 and y > 0:
    quarter_number = 1
elif x < 0 and y > 0:
    quarter_number = 2
elif x < 0 and y < 0:
    quarter_number = 3
else:
    quarter_number = 4

if quarter_number > 0:
    print(f'точка с кординтами ({x}, {y}) находиться в {quarter_number} плоскости')