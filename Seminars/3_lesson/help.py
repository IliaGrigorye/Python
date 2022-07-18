# list() - список: изменяемый, индексируемый
# tuple() - кортеж: неизменяемый, индексируемый
# set() - множество: изменяемый, неиндексируемый
# dict() - словарь: изменяемый, индексируемый по ключу

# a = [12, 3, 5]
# my_tuple = tuple([1, 2, 3])
# my_tuple = tuple([a])
# my_tuple = (1, 2, 3)
# my_tuple = 10,

# my_set = set()
# my_set = {4, 2, 7}
# a = [1, 2, 2, 3, 3]
# print(set(a)) --> (1, 2, 3)

my_dict = dict()
my_dict = {
    543: 'Стул',
    753: 'Стол'
}

for key, val in my_dict.items():
    print(f"{key} - {val}")


