from tkinter import *
from tkinter.messagebox import *

#win
Windowl=Tk()
Windowl.title("Спорт")
Windowl.geometry("1000x800")
#win

#canvas
canvas=Canvas(Windowl)
canvas.place(x=100,y=100,width=900,height=780)

def b1_click(event):
    global img
    tennis_img = PhotoImage(file="image-1.jpg")
    canvas.create_image(0,0,anchor=E,image=img)

def b2_click(event):
    global img
    tennis_img = PhotoImage(file="image-2.jpg")
    canvas.create_image(0,0,anchor=E,image=img)

def b3_click(event):
    global img
    tennis_img = PhotoImage(file="image-3.jpg")
    canvas.create_image(0,0,anchor=E,image=img)
#canvas

#Var
itVar = IntVar()
#Var

#lab
lab = Label(text="Виберіть ваш улюблений спорт")
lab.pack()
#lab

#кнопочки
b1 = Radiobutton(text="теніс", variable=itVar, value=1)
b1.place(x=20, y=30)
b1.bind("<Button-1>",b1_click)

b2 = Radiobutton(text="Футбол", variable=itVar, value=2)
b2.place(x=20, y=60)
b2.bind("<Button-1>",b2_click)

b3 = Radiobutton(text="фігурне катання", variable=itVar, value=3)
b3.place(x=20, y=90)
b3.bind("<Button-1>",b3_click)
#кнопочки

mainloop()