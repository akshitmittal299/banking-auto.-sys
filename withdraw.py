from tkinter import *
from tkinter import messagebox
import pymysql.cursors
from PIL import Image , ImageTk
import datetime
import time
import management
class Withdraw:
    def __init__(self):
        self.root=Tk()
        self.root.title("PROJECT")
        self.root.state("zoomed")
        self.root.config(background="#FFFFCC")
        self.l1=Label(self.root, text="Withdraw")
        self.l1.config(background="#FFFFCC",font=("Times New Roman",40,"underline"))
        self.l1.place(relx=0.35, rely=0.03)

        self.conn=pymysql.connect(host="localhost", user="root", password="root", db= "dbbank")
        self.cursor=self.conn.cursor()

        self.l2=Label(self.root, text="Enter Account No. :")
        self.l2.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l2.place(relx=0.25, rely=0.15)

        self.e2=Entry(self.root)
        self.e2.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e2.place(relx=0.5, rely=0.15)

        self.b1=Button(self.root,text="Search", command=self.search)
        self.b1.config(background="white",font=("Times New Roman", 20,"bold"))
        self.b1.place(relx=0.43, rely=0.25)
        
        self.root.mainloop()
        l=management.demo()
    def search(self):
        ano=self.e2.get()
        
        self.cursor.execute("select * from tbaccount where acno=%s",(ano))
        self.conn.commit()
        row=self.cursor.rowcount
        if(row>0):
            row=self.cursor.fetchone()
            self.bal=row[9]
            self.display()
        else:
            messagebox.showerror("Alert","You do not have a account here!!!")
    def display(self):
        self.f1=Frame(self.root,height=500, bd=5,width=1200, relief=RIDGE)
        self.f1.config(background="#FFFFCC")
        self.f1.place(relx=0.1,rely=0.35)

        self.l5=Label(self.f1, text="Your Balance :")
        self.l5.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l5.place(relx=0.1, rely=0.13)
        
        self.l6=Label(self.f1, text="Withdrawl Amount:")
        self.l6.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l6.place(relx=0.1, rely=0.23)

        self.e3=Entry(self.f1)
        self.e3.insert(0,self.bal)
        self.e3.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e3.place(relx=0.5, rely=0.13)

        self.e4=Entry(self.f1)
        self.e4.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e4.place(relx=0.5, rely=0.23)

        self.b2=Button(self.f1,text="Withdraw",command=self.draw)
        self.b2.config(background="white",font=("Times New Roman", 20,"bold"))
        self.b2.place(relx=0.4, rely=0.65)
    def draw(self):
        ano=self.e2.get()
        bal=int(self.e3.get())
        amt=int(self.e4.get())
        if(amt<bal):
            upbal=bal-amt
            if(upbal<bal):
        
                m=messagebox.askyesno("VALIDATE"," Do you want to withdraw?")
                if (m):
                    n=self.generateid()
                    (s,t)=self.datetime()
                    self.cursor.execute("update tbaccount set balance=%s where acno=%s",(upbal,ano))
                    self.conn.commit()
                    self.e3.delete(0,END)
                    self.e4.delete(0,END)
                    self.e3.insert(0,upbal)
                    self.cursor.execute("insert into tbtransaction values(%s,%s,%s,'Withdraw',%s,%s,%s)",(n,ano,ano,str(amt),s,t))
                    self.conn.commit()
                    messagebox.showinfo("VALIDATE","YOUR UPDATED BALANCE IS "+str(upbal))
            else:
                messagebox.showerror("ALERT","ENTER AMOUNT IN POSTIVE ")

        else:
            messagebox.showerror("Alert", "Insufficient Balance!!")

    def generateid(self):
        self.cursor.execute("select ifnull(max(transid),0) from tbtransaction")
        row=self.cursor.fetchone()
        n=int(row[0])
        n=n+1
        return n
    def datetime(self):
        s=datetime.date.today()
        t=time.localtime()
        t=time.strftime("%H:%M:%S",t)
        return s,t
        
