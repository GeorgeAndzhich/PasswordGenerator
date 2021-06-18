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
        print("No value detected")
    else:
        passLen = int(length.get())
        passwordGenerated = lower+upper+numbers+symbol
        temp = random.sample(passwordGenerated,passLen)
        final = "".join(temp)

        label1['text'] = final
       #TODO Change label or entry text


window = tk.Tk()
window.title("Password Generator")
window.geometry('400x200')
window.resizable(True, False)
length = tk.Entry(window,width = 2)
length.pack()
button = tk.Button(window, command=lambda: generatePass(), text="Generate")
button.pack(side=BOTTOM)
#TODO Make a text field where you will show your password
field = tk.Label(window)
field.pack()
#TODO Add labels
mainLabel = Label(window,anchor = N,text = "Enter the number of charachters")
mainLabel.place(x = 20,y=200)
mainLabel.pack()

label1 = Label(window,anchor = N)
label1.pack()
window.mainloop()
