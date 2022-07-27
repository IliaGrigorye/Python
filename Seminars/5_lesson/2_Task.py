# Дан список чисел. Создайте файл, в который поподают чисел,
# описываемые возростающую последовательность. Порядок элементов менять нельзя
# пример: [1, 4, 2, 6, 5, 7, 3] -> [1, 4, 6, 7]

import os
path = os.path.join('folder','file2Task.txt')

listt = [1, 4, 2, 6, 5, 7, 3]
new_listt =[listt[0]]
for i in range(1, len(listt)):
    if listt[i] - new_listt[-1] > 0:
        new_listt.append(listt[i])

print(new_listt)

with open(path, 'w') as data:
    data.write(f'{new_listt}')

