from tkinter import *
from tkinter.ttk import *

window = Tk();
window.title("Welcome to ManhKM app");
window.geometry('150x150');
selected = IntVar();
#something
rad1 = Radiobutton(window, text='First', value=1, variable=selected);
rad2 = Radiobutton(window, text='Second', value=2, variable=selected);
rad3 = Radiobutton(window, text='Third', value=3, variable=selected);

#developer: after click on radio button ->
#insert value in label -
def clicked():
    print(selected.get());

btn = Button(window, text="Click me", command=clicked);
rad1.grid(column=0, row=0);
rad2.grid(column=1, row=0);
rad3.grid(column=2, row=0);
btn.grid(column=0, row=1);

window.mainloop();