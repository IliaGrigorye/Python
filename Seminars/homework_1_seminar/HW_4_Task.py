# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).


quarter_number = int(input('введите номер четверти: '))
rangee = ""
k = 0

if quarter_number == 1:
    rangee = "x > 0, y > 0"
elif quarter_number == 2:
    rangee = "x > 0, y < 0"
elif quarter_number == 3:
    rangee = "x < 0, y < 0"
elif quarter_number == 4:
    rangee = "x < 0, y > 0"
else:
    print('Ошибка, введите число от 1 до 4')
    k =+ 1
    
if k == 0:
    print(f'для {quarter_number}-ой четверти диапозон {rangee}')