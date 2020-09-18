from tkinter import *;
from tkinter.ttk import *;


window = Tk();      #<class 'tkinter.Tk'>
window.title("Wellcom to Tkinter");

# set size window:
window.geometry('150x150');

#print(window);
print(type(window));
#create label: - gan gia tri cho Label
lbl1 = Label(window, text="Copyright's ManhKM", font=("Arial Bold", 10));

#create input value:
txt = Entry(window, width=10);

#gan vi tri cua label:
lbl1.grid(column=0, row=1);
lbl2 = Label(window, text="Gameshow Random Value");
lbl2.grid(column=0, row=2);
txt.grid(column=0, row=3);


#handle event button:
def clicked():
    val_response = "Wellcom to " + txt.get();
    lbl1.configure(text=val_response);
# create new function before use in btn:
btn = Button(window, text="Click me", bg="orange", fg="red", command=clicked);
btn.grid(column=0, row=4);





window.mainloop();     #handle action by user