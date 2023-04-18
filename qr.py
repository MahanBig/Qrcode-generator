from tkinter import *
from tkinter import messagebox
import pyqrcode

tk=Tk()
tk.title("QrGenerator")

def generateQr():
    if len(userInput.get()) > 0:
        global qr,img
        qr=pyqrcode.create(userInput.get())
        img = BitmapImage(data=qr.xbm(scale=10))
    else:
        messagebox.showwarning('warning',"Didnt write anything")
    try:
        displayCode()
    except:
        pass

def displayCode():
    imglbl.config(image=img)
    output.config(text="Qr Code : "+userInput.get())

Lbl=Label(tk,text="Enter text or URL")
Lbl.pack()

userInput=StringVar()
entry=Entry(tk,textvariable=userInput,width=50)
entry.pack(padx=50,pady=30)

button= Button(tk,text="Generate",command=generateQr)
button.pack(padx=10,pady=10)

imglbl = Label(tk)
imglbl.pack()

output = Label(tk,text="")
output.pack()

tk.mainloop()
