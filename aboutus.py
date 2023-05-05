from tkinter import *
from tkinter import messagebox
import pymysql.cursors
from PIL import Image , ImageTk
import management
class help1:
    def __init__(self):
        self.root=Tk()
        self.root.title("PROJECT")
        self.root.state("zoomed")
        self.root.config(background="#FFFFCC")
        self.l1=Label(self.root)
        self.l1.place(relx=0.34,rely=0.0)
        img=Image.open("images\\ab.jpg")
        img1=img.resize((400,200), Image.Resampling.LANCZOS)
        self.i1=ImageTk.PhotoImage(img1)
        self.l1.config(image=self.i1)        
        


##        self.l3=Label(self.root, text="About Us:")
##        self.l3.config(background="#FFFFCC",font=("Times New Roman", 40,"bold", "underline"))
##        self.l3.place(relx=0.25, rely=0.03)

        self.t1=Text(self.root,width=80, height=13, wrap='word')
        self.t1.place(relx=0.05, rely=0.25)
        self.t1.config(background="white",font=("Times New Roman", 25,"bold"))
        self.t1.insert('1.0','''This project has been developed by Mr.Akshit Mittal under the supreme guidance of Er. PUNEET AGGARWAL.\nIn recent years, the banking industry has been undergoing drastic changes, reflecting a number of underlying developments. Core Banking Solution (CBS) is networking of branches, which enables Customers to operate their accounts, and avail banking services from any branch of the Bank on CBS network, regardless of where he maintains his account. The customer is no more the customer of a Branch. He becomes the Bank's Customer. Thus CBS is a step towards enhancing customer convenience through anywhere and anytime Banking.\nMinimum Software Requirements.\n1. Operation System: Windows\n2. Language: PYTHON\n3. Front End: Eclipse IDE\n4. Back End: MySQL Server 5.0''')
        self.t1.config(state='disabled')
        self.root.mainloop()
        l=management.demo()

