import random
import tkinter as tk
from tkinter import *

def generatePass():
    print("Clicked")
    symbols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
               "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
               "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".","*","/","?"]
    passLen = int(length.get())
    for i in range(passLen):
       char = random.randint(0,len(symbols))
       print(symbols[char])

#TODO Make a text field where you will show your password
#TODO Add labels
#TODO Reorganize elements on the window
window = tk.Tk()
window.title("Password Generator")
window.geometry('400x300')
window.resizable(False, False)
length = tk.Entry(window,width = 2)
length.pack(side=LEFT)
button = tk.Button(window, command=lambda: generatePass(), text="Generate")
button.pack(side=BOTTOM)


window.mainloop()
