# Напишите программу, которая определит позицию второго вхождения строки
# в списке либо сообщит, что ее нет
# Пример:
# список:[qwe,asd,zxc,asd,fgd], ищем asd ответ 3
# список:[qwe,asd,zxc,фывф,fgd], ищем asd ответ -1


list = ['qwe', 'asd', 'zxc', 'fdgssdg', 'fgd']
find = 'asd'
index = -1
k = 0
for i in range(len(list)):
    if list[i] == find:
        k += 1
        if k == 2:
            index = i

print(index)
