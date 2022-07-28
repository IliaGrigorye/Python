# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции вводить через пробел

position = list(map(int, input('Введите позиций элементов в промежутке [-10,10]: ').split()))

list_1 = []
list_2 = []

def list_n(list):
    N = 10
    k = -N
    while k < N + 1:
        list.append(k)
        k += 1
    return list

def sum_n(position, list_1):
    # summ = 0
    # for i in range(len(position)):
    #     summ += list_1[position[i]]
    summ = sum([list_1[position[i]] for i in range(len(position))])
    return summ

def list_k(list_1, list_2):
    # for i in range(len(position)):
    #     list_2.append(list_1[position[i]])
    [list_2.append(list_1[position[i]]) for i in range(len(position))]
    return list_2    

    
print(list_n(list_1))
print(list_k(list_1, list_2))
print(f'Сумма чисел на позициях {position} равна {sum_n(position, list_1)}')
