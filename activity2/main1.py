from tkinter import *
from tkinter import messagebox
#create a window
window=Tk()
window.title("Event Handler")
window.geometry("500x500")

def msg():
    messagebox.showwarning("Alert","Stop! Virus Found.\n  User,\n   you should remove the virus")

#Adding button
button=Button(window,text="Scan For Virus",command=msg)
button.place(x=40,y=80)

window.mainloop()