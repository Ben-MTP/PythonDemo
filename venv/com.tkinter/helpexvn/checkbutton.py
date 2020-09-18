from tkinter import *
from tkinter.ttk import *

window = Tk();
window.title("Welcome to ManhKM app");
window.geometry('150x150');
chk_state = BooleanVar();
chk_state.set(True);
chk = Checkbutton(window, text='Men', var=chk_state);
chk.grid(column=0, row=0);
window.mainloop();