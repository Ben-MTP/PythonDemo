from tkinter import *;
from tkinter.ttk import *;

window = Tk();
window.title("Welcome to ManhKM app");
window.geometry('150x150');
combo = Combobox(window)
combo['value'] = (1, 2, 3, 4, 5, "Text")
combo.current(5) #set data default:
combo.grid(column=0, row=0);

#developer: click choose value of input
#show result in screen

window.mainloop();