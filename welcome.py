from tkinter import *
#from tkinter import messagebox
import pymysql.cursors
from PIL import Image , ImageTk
import loading
class welcome:
    def __init__(self):
        self.root=Tk()
        self.root.title("PROJECT")
        self.root.state("zoomed")
        self.root.config(background="#FFFFCC")

        self.l1=Label(self.root, text="WELCOME TO BANK AUTOMATION SYSTEM")
        self.l1.config(background="#FFFFCC",font=("Times New Roman", 40,"bold", "italic","underline"))
        self.l1.place(relx=0.15,rely=0)

        self.la=Label(self.root)
        self.la.place(relx=0.0, rely=0.08)
        img=Image.open("images\\aa.jpg")
        img1=img.resize((1600,550), Image.Resampling.LANCZOS)
        self.i1=ImageTk.PhotoImage(img1)
        self.la.config(image=self.i1)

        self.b1=Button(self.root, text="GET STARTED", command=self.loading,relief=RAISED)
        self.b1.config(background="black",foreground="white",height=2,width=30,font=(30))
        self.b1.place(relx=0.4,rely=0.8)
        self.root.mainloop()

    def loading(self):
        self.root.destroy()
        l1=loading.Loading()
obj=welcome()
