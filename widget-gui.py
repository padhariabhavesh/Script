#Programmer Bhavesh Padharia

#Adding widges in GUI

import tkinter as tk

win = tk.Tk()
win.title("First GUI")
l1 = tk.Label(win, text= " This is Label",)
b1 = tk.Button(win, text = " Click Me")
b1.pack()
l1.pack()

win.mainloop()
