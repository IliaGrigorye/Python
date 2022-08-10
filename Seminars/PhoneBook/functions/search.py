filename = "c:/Programming/programming/Working in Visual Studio Code/Python/Seminars/PhoneBook/myphonebook.txt"  

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