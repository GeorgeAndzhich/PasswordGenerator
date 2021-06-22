import random
import string
import tkinter as tk
from tkinter import *

def generatePass():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbol = string.punctuation
    passLen = length.get()
    if passLen == "":
        label1['text'] = "No input detected"
    else:
        try:
            passLen = int(length.get())
        except ValueError:
            label1['text'] = "Please enter a number"
        else:
            passwordGenerated = lower+upper+numbers+symbol
            temp = random.sample(passwordGenerated,passLen)
            final = "".join(temp)
            label1['text'] = final


window = tk.Tk()
window.title("Password Generator")
window.geometry('400x200')
window.resizable(True, False)
length = tk.Entry(window,width = 2)
length.pack()
button = tk.Button(window, command=lambda: generatePass(), text="Generate")
button.pack(side=BOTTOM)
field = tk.Label(window)
field.pack()
mainLabel = Label(window,anchor = N,text = "Enter the number of charachters")
mainLabel.place(x = 20,y=200)
mainLabel.pack()

label1 = Label(window,anchor = N)
label1.pack()
window.mainloop()
