from tkinter import *
from tkinter.font import Font



window=Tk()
window.title("To-Do-List")
window.geometry("500x500")

my_font=Font (
    family="Brush Script MT",
    size=30,
    weight="bold")

my_frame = Frame(window)
my_frame.pack(pady=10)

my_list=Listbox(my_frame,
                font = my_font,
                width = 25,
                height = 5,
                bg = "SystemButtonFace",
                bd = 0,
                fg ="#464646",
                highlightthickness = 0,
                selectbackground =  "#a6a6a6",
                activestyle="none")
my_list.pack()

stuff=["Walk the dog", "Buy Groceries","Learn tkinter", "complete task"]
for item in stuff:
    my_list.insert(END, item)

my_scrollbar=Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

my_list.config(yscrollcommand = my_scrollbar)
my_scrollbar.config(command = my_list.yview)

my_entry = Entry(window, font=("Helvetica", 24))
my_entry.pack(pady=20)

button_frame = Frame(window)
button_frame.pack(pady=20)

def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)


delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)


window.mainloop()