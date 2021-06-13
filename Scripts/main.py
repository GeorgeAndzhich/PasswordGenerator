import random
import tkinter as tk
from tkinter import *

def generatePass():
    print("Clicked")
    symbols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
               "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
               "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".","*","/","?"]
    passLen = length.get()
    if passLen == 0:
        print("No value detected")
    else:
        passLen = int(length.get())
    for i in range(passLen):
       char = random.randint(0,len(symbols))
       print(symbols[char],end= '')
       #TODO Change label or entry text


window = tk.Tk()
window.title("Password Generator")
window.geometry('400x300')
window.resizable(False, False)
length = tk.Entry(window,width = 2)
length.pack()
button = tk.Button(window, command=lambda: generatePass(), text="Generate")
button.pack(side=BOTTOM)
#TODO Make a text field where you will show your password
field = tk.Label(window,justify = BOTTOM)
field.pack()
#TODO Add labels
mainLabel = Label(window,anchor = CENTER,text = "Enter the number of charachters")
mainLabel.pack()
#TODO Reorganize elements on the window

window.mainloop()
