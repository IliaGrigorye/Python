# Реализуйте алгоритм перемешивания списка

import random 

list = list(map(int, input('Введите числа через пробел: ').split()))

def mix_list(list):
    for i in range(len(list)-1, 0, -1):
        j = random.randint(0, i + 1) 
        list[i], list[j] = list[j], list[i]
    return list      


print (list)  
print (mix_list(list))

