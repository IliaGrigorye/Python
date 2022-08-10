from .importt import newcontact
from .search import searchcontact
from .delete import delet

filename = "c:/Programming/programming/Working in Visual Studio Code/Python/Seminars/PhoneBook/myphonebook.txt"  

def main_menuu(): 
    print( "\nГЛАВНОЕ МЕНЮ\n") 
    print( "1. Показать все существующие контакты") 
    print( "2. Добавить новый контакт") 
    print( "3. Поиск по существующему контакту")
    print( "4. Удаление контакта") 
    print( "5. Выход") 
    choice = input("Введите нужную цифру: ") 
    if choice == "1": 
        myfile = open(filename, "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "В телефонной книге нет контактов.") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menuu() 
    elif choice == "2": 
        newcontact() 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menuu() 
    elif choice == "3": 
        searchcontact() 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menuu() 
    elif choice == "4": 
        delet() 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menuu() 
    elif choice == "5": 
        print("Благодарим вас за использование телефонной книги!") 
    else: 
        print( "Пожалуйста, предоставьте действительные входные данные!\n") 
        enter = input( "Нажмите Enter, чтобы продолжить ...") 
        main_menuu()