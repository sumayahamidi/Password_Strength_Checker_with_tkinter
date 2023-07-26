
# # Password_Strength_Checker
import string
from tkinter import *
import tkinter as tk #tkinter module for show windows 

window=Tk()  #make tkinter for gui password checker
window.title('Pass')
window.resizable(False,False)
window.grid_propagate(1)
window.geometry('250x200')

frame=Frame(window,width=650,height=500 )
frame.place(x=0,y=0)

password = StringVar() #Password variable
pass_lbl=Label(frame,text='enter your password' ,border=0 ,borderwidth=0, highlightthickness=0 )
pass_lbl.place(x=50,y=40,width=150)

pass_entry=Entry(frame , textvariable=password ,show="*" ,cursor="hand2")
pass_entry.place(x=60,y=70)

# characters list
special_characters = list(string.punctuation)

def delete_pass():
    password.set("")  # clear the password variable
    pass_entry.delete(0, END)  # delete the contents of the pass_entry widge

def toggle_password_visibility():
    if show_password.get():
        pass_entry.config(show="")
    else:
        pass_entry.config(show="*")

def show():
    p = password.get() #get password from entry
    if len(p)<8:
        pass_lbl.config(text = 'password is too short')
        delete_pass()

    elif not any(char.isdigit() for char in p):
        pass_lbl.config(text = "please add number!")
        delete_pass()

    elif not any(char in special_characters for char in p):
        pass_lbl.config(text = "please add special character!")
        delete_pass()

    elif not any(char.islower() for char in p):
        pass_lbl.config(text = "please add lowercase letter!")
        delete_pass()

    elif not any(char.isupper() for char in p):
        pass_lbl.config(text = "please add uppercase letter!")
        delete_pass()
        
    else:
        pass_lbl.config(text = 'password is strong')

show_password = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(frame, text="Show password", variable=show_password, command=toggle_password_visibility)
show_password_checkbox.place(x=60, y=90)

enter_btn=Button(frame,text='Enter',command=show)
enter_btn.place(x=100,y=130)

window.mainloop()
# #________________________________________
#__________________________________________

