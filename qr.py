from tkinter import *
from tkinter import messagebox
import pyqrcode

tk=Tk()
tk.title("QrGenerator")
tk.config(bg="#99bbff")

def generateQr():
    pass
def displayCode():
    pass

Lbl=Label(tk,text="Enter text or URL",bg="#f25252",padx=30,pady=20,font=("Courier",30))
Lbl.pack()

userInput=StringVar()
entry=Entry(tk,textvariable=userInput,width=50,font=("Courier",30))
entry.pack(padx=50,pady=30)

button= Button(tk,text="Generate",width=20,command=generateQr,font=("ariel",15))
button.pack(padx=10,pady=10)

imglbl = Label(tk,bg="#e6e6e6")
imglbl.pack()

output = Label(tk,text="",bg="#f25252")
output.pack()

tk.mainloop()
