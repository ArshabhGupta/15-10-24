from tkinter import *
from datetime import date

root = Tk()
root.title("Getting started with widgets")
root.geometry('400x300')

lb1 = Label(text = "Hey there!", fg = "red", bg = "aqua", height = 1, width = 300)

label1 = Label(text = "Full Name", bg = "white")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to the application! "
    greet = "Hello"+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height = 3)
btn = Button(text = "Begin", command = display, height = 1, bg = "aqua", fg = "blue")

lb1.pack()
label1.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()