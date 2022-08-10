from tkinter import *
from tkinter import scrolledtext
from turtle import width

filename = "c:/Programming/programming/Working in Visual Studio Code/Python/Seminars/interface/myphonebook.txt"
myfile = open(filename, "a+")
myfile.close 


def viewing_contacts():
    myfile = open(filename, "r+") 
    filecontents = myfile.read() 
    if len(filecontents) == 0: 
        lbl = Label(window, text="В телефонной книге нет контактов", font = ("Arial Bold", 9))
        lbl.grid(column=1, row=1)
    else:
        txt = scrolledtext.ScrolledText(window, width=40, height=10, font = ("Arial Bold", 9))
        txt.grid(column=1, row=1)
        txt.insert(INSERT, filecontents)
    myfile.close

def add_contact():
    lbl = Label(window, text="Имя")  
    lbl.grid(column=1, row=1)
    txt_one = Entry(window, width=15, font = ("Arial Bold", 9))
    txt_one.grid(column=2, row=1)

    lbl = Label(window, text="Фамилия")  
    lbl.grid(column=1, row=2)
    txt_two = Entry(window, width=15, font = ("Arial Bold", 9))
    txt_two.grid(column=2, row=2)

    lbl = Label(window, text="Номер телефона")  
    lbl.grid(column=1, row=3)
    txt_three = Entry(window, width=15, font = ("Arial Bold", 9))
    txt_three.grid(column=2, row=3)

    lbl = Label(window, text="Электроная почта")  
    lbl.grid(column=1, row=4)
    txt_four = Entry(window, width=15, font = ("Arial Bold", 9))
    txt_four.grid(column=2, row=4)

    def input_firstname() -> str:
        first = "{}".format(txt_one.get())
        lbl.configure(text=first) 
        remfname = first[1:] 
        firstchar = first[0] 
        return firstchar.upper() + remfname
    def input_lastname() -> str: 
        last = "{}".format(txt_two.get())
        lbl.configure(text=last) 
        remlname = last[1:] 
        firstchar = last[0] 
        return firstchar.upper() + remlname 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = "{}".format(txt_three.get())
    lbl.configure(text=phoneNum) 
    emailID = "{}".format(txt_four.get())
    lbl.configure(text=emailID) 
    
    def click():
        contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  "]\n") 
        myfile = open(filename, "a") 
        myfile.write(contactDetails)
        # lbl = Label(window, text="Следующие контактные данные:\n " + contactDetails + "\nбыли успешно сохранены!", font = ("Arial Bold", 14))
        # lbl.grid(column=2, row=6) 
        # print( "Следующие контактные данные:\n " + contactDetails + "\nбыли успешно сохранены!")

    button = Button(window, text='Добавить', font = ("Arial Bold", 9), command=click)    
    button.grid(column=2, row=5)


window = Tk()
window.title("Телефонный справочник")
window.geometry('500x350')
lbl = Label(window, text="ГЛАВНОЕ МЕНЮ", font = ("Arial Bold", 14))
lbl.grid(column=0, row=0)
btn_one = Button(window, text="Посмотреть все контакты", font = ("Arial Bold", 9), command=viewing_contacts)
btn_one.grid(column=0, row=1)
btn_two = Button(window, text="Добавить контакт", font = ("Arial Bold", 9), command=add_contact)
btn_two.grid(column=0, row=2)

window.mainloop()