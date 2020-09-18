# Lam quen voi kiem gia dien trong python
# Lam mot poppu hien thi du lieu:
# Thu vien tkinter import:
#
#
from tkinter import *;
from tkinter import messagebox;
def hello():
    messagebox.showinfo('Hello everyone', 'How are you?')
tk = Tk();
btn = Button(tk, text = 'click me', command = hello);
btn.pack();
mainloop();