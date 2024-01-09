from tkinter import *
from random import randint

window=Tk()
window.title("Password Generator")
window.geometry("500x400")

my_password= chr(randint(33,126))

def new_rand():
    pw_entry.delete(0, END)
    pw_length=int(my_entry.get())
    my_password=''
    for x in range(pw_length):
        my_password+= chr(randint(33,126))
    pw_entry.insert(0, my_password)

def clipper():
    window.clipboard_clear()
    window.clipboard_append(pw_entry.get())
    

label_frame= LabelFrame(window, text="How Many Characters?")
label_frame.pack(pady=20)

my_entry=Entry(label_frame, font=("Helvetica",24))
my_entry.pack(pady=20, padx=20)

pw_entry = Entry(window, text='', font=("Helvetica",24),bd=0, bg="Systembuttonface")
pw_entry.pack(pady=20)

my_frame= Frame(window)
my_frame.pack(pady=20)

my_button=Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0,column=0,padx=10)

clip_button=Button(my_frame, text="Copy to clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

window.mainloop()