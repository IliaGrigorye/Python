filename = "myphonebook.txt"
myfile = open(filename, "a+")
myfile.close 

# главное меню 
def main_menu(): 
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
        main_menu() 
    elif choice == "2": 
        newcontact() 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
    elif choice == "3": 
        searchcontact() 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
    elif choice == "4": 
        delet() 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
    elif choice == "5": 
        print("Благодарим вас за использование телефонной книги!") 
    else: 
        print( "Пожалуйста, предоставьте действительные входные данные!\n") 
        enter = input( "Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
 
# функция поиска         
def searchcontact(): 
    searchname = input( "Введите имя и фамилию для поиска контактной записи: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print( "По вашему запросу найдено:", end = " ") 
            print( line) 
            found = True 
            break 
    if found == False: 
        print( "По вашему запросу ни чего не найдено", searchname) 
 
# ввод имени 
def input_firstname(): 
    first = input( "Введите Имя: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 
# ввод фамилий 
def input_lastname(): 
    last = input( "Введите Фамилию: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 
 
# сохранение новых контактных данных
def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input( "Введите номер телефона: ") 
    emailID = input( "Введите адрес электронной почты: ") 
    contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  "]\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print( "Следующие контактные данные:\n " + contactDetails + "\nбыли успешно сохранены!") 

# удаление
def delet():
    firstname = input( "Введите Имя: ")
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for line in lines:
            if firstname == "":
                f.write(line)
            elif firstname not in line:
                f.write(line)


main_menu()
