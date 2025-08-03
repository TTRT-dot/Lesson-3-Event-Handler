from tkinter import *
import random
#create a window
window=Tk()
window.title("Event Handler")
window.geometry("500x500")

#Event handler for keypress
def handle_keypress(event):
    """Print the charecter associated to the key pressed"""
    print(event.char)

#Bind keypress to event to handle_keypress()
window.bind("<Key>",handle_keypress)

    #event handler for butten click
def handle_click(event):
    print("\n Button was clicked! \n  Greetings User \n   How are you")

button = Button(text="Click Me!")
button.pack()

#Bind click event to handle_click()
button.bind("<Button-1>",handle_click)

window.mainloop()