# Напишите программу, удаляющую из текста все слова содержащий "абв".

def read_from_file(f_name: str) -> str:
    with open(f_name, 'r') as f:
        return f.readline()

a = read_from_file('folder/file3Task.txt').split()

b = ' '.join(filter(lambda x: not 'abc' in x, a))

print(b)