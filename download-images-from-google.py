# @Bhavesh Padharia
# Download images from google using python

import requests
import shutil
import tkinter as tk
import tkinter.tkk as tkk
from tkinter.messagebox import showinfo

win = tk.TK()
win.title("Image downloader...")

def download():
    url = entry.get()
    img = requests.get(url,stream=True)
    saveImg = open(r'big data',wb)
    shutil.copyfileobj(img.raw,saveImg)
    showinfo("done","image download successfully")

label = tk.Label(win,text='Enter the url here: ')
label.grid(row=0,column=0,padx=5,pady=5)

entry = tk.Entry(win,width=30)
entry.grid(row=0,column=1,padx=5,pady=5)

button = ttk.Button(win,text="Download",command=download)
button.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

win.mainloop()


