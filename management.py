from tkinter import *
from tkinter import messagebox
import pymysql.cursors
from PIL import Image , ImageTk
import delete
import deposite
import editpwd
import edtprf
import aboutus
import ministat
import modify
import newacc
import search
import secupd
import transfer
import view
import withdraw
import update
import login
class demo:
    def __init__(self, aid):
        self.root=Tk()
        self.adminid = aid
        self.root.title("PROJECT")
        self.root.state("zoomed")
        self.root.config(background="#FFFFCC")
        self.l1=Label(self.root)
        self.l1.place(relx=0,rely=0)

        
        img=Image.open("images\\mm.jpg")
        img1=img.resize((1600,780), Image.ANTIALIAS)
        self.i1=ImageTk.PhotoImage(img1)
        self.l1.config(image=self.i1,compound="bottom")

        self.root.option_add('*tearOff', False)
        self.mb=Menu(self.root)
        self.root.config(menu=self.mb)
        self.ac1=Menu(self.mb)
        self.t1=Menu(self.mb)
        self.a1=Menu(self.mb)
        self.h1=Menu(self.mb)
        self.mb.add_cascade(menu=self.ac1,label='Account')
        self.mb.add_cascade(menu=self.t1,label='Transaction')
        self.mb.add_cascade(menu=self.a1, label='Admin')
        self.mb.add_cascade(menu=self.h1, label='Help')
        self.ac1.add_command(label='Open New Account',comman=self.open)
        #self.f1.add_separator()
        self.ac1.add_command(label='Modify Account', command=self.modify)
        self.ac1.add_command(label='Delete Account', command=self.dlt)
        self.ac1.add_command(label='View All Account', command=self.view)
        self.ac1.add_command(label='Search', command=self.search)
        self.t1.add_command(label='Withdraw', command=self.withdraw)
        self.t1.add_command(label='Deposit', command=self.deposit)
        self.t1.add_command(label='Transfer', command=self.transfer)
        self.t1.add_command(label='Ministatement', command=self.mini)
        self.a1.add_command(label='Edit Profile', command=self.profile)
        self.a1.add_command(label='Edit Password',command=self.pwd)
        self.a1.add_command(label='Edit Security Settings',command= self.security)
        self.a1.add_command(label='Logout', command=self.logout)
        self.h1.add_command(label='About Us', command=self.about)
        self.root.mainloop()
    def open(self):
        
        obj=newacc.New_acc()
    def modify(self):
        
        obj=modify.Modify()
    def dlt(self):
        
        obj=delete.Delete()
    def view(self):
        
        obj=view.View()
    def search(self):
        
        obj=search.Search()
    def withdraw(self):
        
        obj=withdraw.Withdraw()
    def deposit(self):
        
        obj=deposite.Deposit()
    def transfer(self):
        
        obj=transfer.Transfer()
    def mini(self):
        
        obj=ministat.Mini()
    def profile(self):
        
        obj=edtprf.Edit(self.adminid)
    def pwd(self):
        
        obj=editpwd.Editpwd(self.adminid)
    def security(self):
        
        obj=secupd.secupd(self.adminid)
    def logout(self):
        
        obj=login.Login()
    def about(self):
        
        obj=aboutus.help1()





