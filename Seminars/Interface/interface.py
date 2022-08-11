from pdb import Restart
from tkinter import *
from tkinter import scrolledtext
from turtle import clear


filename = "c:/Programming/programming/Working in Visual Studio Code/Python/Seminars/interface/myphonebook.txt"
myfile = open(filename, "a+")
myfile.close 

def phonebook():
    def viewing_contacts():
        myfile = open(filename, "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            lbl = Label(win, text="В телефонной книге нет контактов", font = ("Arial", 9))
            lbl.grid(column=1, row=1)
        else:
            txt = scrolledtext.ScrolledText(win, width=60, height=10, font = ("Arial", 9))
            txt.grid(column=1, row=1)
            txt.insert(INSERT, filecontents)
        myfile.close

    def add_contact(): 
        lbl = Label(win, text="Имя", font = ("Arial", 9))  
        lbl.grid(column=1, row=1)
        txt_one = Entry(win, width=15, font = ("Arial", 9))
        txt_one.grid(column=2, row=1, stick='wens', padx=5, pady=5)

        lbl = Label(win, text="Фамилия", font = ("Arial", 9))  
        lbl.grid(column=1, row=2)
        txt_two = Entry(win, width=15, font = ("Arial", 9))
        txt_two.grid(column=2, row=2, stick='wens', padx=5, pady=5)

        lbl = Label(win, text="Номер телефона", font = ("Arial", 9))  
        lbl.grid(column=1, row=3)
        txt_three = Entry(win, width=15, font = ("Arial", 9))
        txt_three.grid(column=2, row=3, stick='wens', padx=5, pady=5)

        lbl = Label(win, text="Email", font = ("Arial", 9))  
        lbl.grid(column=1, row=4)
        txt_four = Entry(win, width=15, font = ("Arial", 9))
        txt_four.grid(column=2, row=4, stick='wens', padx=5, pady=5)
    
        def write_txt(data):
            with open(filename, 'a') as file:
                file.write(data)
        
        def click():
            firstname = txt_one.get()
            lastname = txt_two.get()
            phoneNum = txt_three.get()
            emailID = txt_four.get()

            contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  "]\n") 
            write_txt(contactDetails)
            lbl = Label(win, text="Следующие контактные данные:\n " + contactDetails + "\nбыли успешно сохранены!", font = ("Arial Bold", 7))
            lbl.grid(column=2, row=6) 
            

        button = Button(win, text='Добавить', font = ("Arial", 9), command=click)    
        button.grid(column=2, row=5)

    def searchcontact():
        lbl = Label(win, text="Введите Имя и Фамилию", font = ("Arial", 9))  
        lbl.grid(column=1, row=3)
        txt = Entry(win, width=15, font = ("Arial", 9))
        txt.grid(column=1, row=4, stick='wens', padx=5, pady=5)

        def click():
            searchname = txt.get() 
            myfile = open(filename, "r+") 
            filecontents = myfile.readlines()
            found = False 
            for line in filecontents: 
                if searchname in line: 
                    lbl_one = Label(win, text="По ващему запросу найдено:", font = ("Arial", 9))
                    lbl_one.grid(column=1, row=5)
                    lbl_two = Label(win, text=line, font = ("Arial", 9))
                    lbl_two.grid(column=1, row=6)
                    found = True 
            if found == False: 
                lbl = Label(win, text="По ващему запросу ни чего не найдено", font = ("Arial", 9))
                lbl.grid(column=1, row=5)

        button = Button(win, text='Поиск', font = ("Arial", 9), command=click)    
        button.grid(column=2, row=4)

    def delet():
        lbl = Label(win, text="Введите Имя и Фамилию", font = ("Arial", 9))  
        lbl.grid(column=1, row=4)
        txt = Entry(win, width=15, font = ("Arial", 9))
        txt.grid(column=1, row=5, stick='wens', padx=5, pady=5)

        def click():
            firstname = txt.get()
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
                    lbl = Label(win, text="По ващему запросу ни чего не найдено", font = ("Arial", 9))
                    lbl.grid(column=1, row=6)
                if c > 0:
                    lbl = Label(win, text="По ващему запросу ни чего не найдено", font = ("Arial", 9))
                    lbl.grid(column=1, row=6)
                else:
                    lbl = Label(win, text=f"Контактный данный {firstname} удалены", font = ("Arial", 9))
                    lbl.grid(column=1, row=6)

        button = Button(win, text='Удалить', font = ("Arial", 9), command=click)    
        button.grid(column=2, row=5)

    win = Tk()
    win.title("Телефонный справочник")
    win.geometry('630x400')

    lbl = Label(win, text="Главное меню", font = ("Arial", 12))
    lbl.grid(column=0, row=0, stick='we', padx=5)

    btn_one = Button(win, text="Посмотреть все контакты", font = ("Arial", 9), command=viewing_contacts)
    btn_one.grid(column=0, row=1, stick='wens', padx=5, pady=5)
    btn_two = Button(win, text="Добавить контакт", font = ("Arial", 9), command=add_contact)
    btn_two.grid(column=0, row=2, stick='wens', padx=5, pady=5)
    btn_three = Button(win, text="Поиск по контакта", font = ("Arial", 9), command=searchcontact)
    btn_three.grid(column=0, row=3, stick='wens', padx=5, pady=5)
    btn_four = Button(win, text="Удаление контакта", font = ("Arial", 9), command=delet)
    btn_four.grid(column=0, row=4, stick='wens', padx=5, pady=5)


    def restart():
        win.destroy()
        phonebook()   

    btn_five = Button(win, text="Перезапуск", font = ("Arial", 9), command=restart)
    btn_five.grid(column=0, row=5, stick='wens', padx=5, pady=5)



    win.grid_columnconfigure(0, minsize=60)
    win.grid_columnconfigure(1, minsize=60)
    win.grid_columnconfigure(2, minsize=60)

    win.grid_rowconfigure(0, minsize=30)
    win.grid_rowconfigure(1, minsize=30)
    win.grid_rowconfigure(2, minsize=30)
    win.grid_rowconfigure(3, minsize=30)
    win.grid_rowconfigure(4, minsize=30)
    win.grid_rowconfigure(5, minsize=30)
    win.grid_rowconfigure(6, minsize=30)

    win.mainloop()

phonebook()