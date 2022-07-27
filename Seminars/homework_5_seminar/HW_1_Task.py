# Напишите программу, удаляющую из текста все слова, содержащие "абв".

def read_from_file(f_name: str) -> str:
    with open(f_name, 'r') as f:
        return f.readline()

a = read_from_file('folder/file1Task.txt').split()

b = ' '.join(filter(lambda x: not 'abc' in x, a))

print(b)