filename = "c:/Programming/programming/Working in Visual Studio Code/Python/Seminars/PhoneBook/myphonebook.txt"

def input_firstname(): 
    first = input( "Введите Имя: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 

def input_lastname(): 
    last = input( "Введите Фамилию: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 

def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input( "Введите номер телефона: ") 
    emailID = input( "Введите адрес электронной почты: ") 
    contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  "]\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print( "Следующие контактные данные:\n " + contactDetails + "\nбыли успешно сохранены!") 