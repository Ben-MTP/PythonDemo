from tkinter import *;
from tkinter import scrolledtext;
window = Tk();
window.title("Welcome to ManhKM app");
window.geometry('150x150');
txt = scrolledtext.ScrolledText(window,width=40,height=10);
txt.grid(column=0,row=0);
window.mainloop();