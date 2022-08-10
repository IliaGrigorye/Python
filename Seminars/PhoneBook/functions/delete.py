
filename = "c:/Programming/programming/Working in Visual Studio Code/Python/Seminars/PhoneBook/myphonebook.txt"  

def delet():
    firstname = input( "Введите Имя и Фамилию: ")
    c = 0
    k = 0

    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for line in lines:
            if firstname == "":
                f.write(line)
                c += 1
            if firstname not in line:
                f.write(line)
                k += 1
        
        if k == len(lines):
            print('Контакт не найден')
        if c > 0:
            print('Контакт не найден')