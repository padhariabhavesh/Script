# Programmer : Bhavesh Padharia

# Question ask using tkinter in Python

from tkinter import *
from tkinter import messagebox

# Object of Tk()

main = Tk()

#function to use the ask question

def Submit():
    messagebox.askquestion("From", "Do you want to submit")

#setting geometry of window instance

main.geometry("100x100")
#creating window

B1 = Button(main, text="Submit", command=Submit)

#Button positioning

B1.pack()

#infinite loop till close

main.mainloop()



# Follow Us : www.padharia.in

