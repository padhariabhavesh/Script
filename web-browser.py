# Programmer Bhavesh Padharia
# Make your own web browser

import tkinter as tk
import webbrowser

win = tk.Tk()

def wb():
    url = e1.get()
    webbrowser.open(url)

l1 = tk.Label(win, text = "Enter URL = ")
l1.grid(row=0, column=0, padx=5,pady=5)

e1 = tk.Entry(win, width=50, bg='#ff9ca6')
e1.grid(row=0, column=1, padx=5,pady=5)

b1 = tk.Button(win, text = "Search", command=wb)
b1.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

win.mainloop()

