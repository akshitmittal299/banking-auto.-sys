from tkinter import *
from tkinter import messagebox,ttk
import pymysql.cursors
from PIL import Image , ImageTk
import management
class Modify:
    def __init__(self):
        self.root=Tk()
        self.root.title("PROJECT")
        self.root.state("zoomed")
        self.root.config(background="#FFFFCC")

        self.l1=Label(self.root, text="Modify Account Details")
        self.l1.config(background="#FFFFCC",font=("Times New Roman",40,"underline"))
        self.l1.place(relx=0.35, rely=0.03)

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
        obj=management.demo()
    def search(self):
        ano=self.e2.get()
        conn=pymysql.connect(host="localhost", user="root", password="root", db= "dbbank")
        cursor=conn.cursor()
        cursor.execute("select * from tbaccount where acno=%s",(ano))
        row=cursor.rowcount
        if(row>0):
            self.display()
        else:
            messagebox.showerror("Alert","You do not have a account here!!!")
    def display(self):
        self.f1=Frame(self.root,height=500, bd=5,width=1200, relief=RIDGE)
        self.f1.config(background="#FFFFCC")
        self.f1.place(relx=0.1,rely=0.35)

        self.l5=Label(self.f1, text="Customer Name:")
        self.l5.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l5.place(relx=0.1, rely=0.03)
        
        self.l6=Label(self.f1, text="Customer Address:")
        self.l6.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l6.place(relx=0.1, rely=0.13)

        self.l7=Label(self.f1, text="Customer Email:")
        self.l7.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l7.place(relx=0.1, rely=0.23)
        
        
        self.l8=Label(self.f1, text="Customer Contact:")
        self.l8.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l8.place(relx=0.1, rely=0.33)

        self.l9=Label(self.f1, text="Customer Father's Name:")
        self.l9.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l9.place(relx=0.1, rely=0.43)

        self.l0=Label(self.f1, text="Customer Mother's Name:")
        self.l0.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l0.place(relx=0.1, rely=0.53)

        self.e3=Entry(self.f1)
        self.e3.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e3.place(relx=0.5, rely=0.03)

        self.e4=Entry(self.f1)
        self.e4.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e4.place(relx=0.5, rely=0.13)

        self.e5=Entry(self.f1)
        self.e5.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e5.place(relx=0.5, rely=0.23)

        self.e6=Entry(self.f1)
        self.e6.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e6.place(relx=0.5, rely=0.33)

        self.e7=Entry(self.f1)
        self.e7.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e7.place(relx=0.5, rely=0.43)

        self.e8=Entry(self.f1)
        self.e8.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e8.place(relx=0.5, rely=0.53)

        self.b2=Button(self.f1,text="Modify", command=self.modify)
        self.b2.config(background="white",font=("Times New Roman", 20,"bold"))
        self.b2.place(relx=0.4, rely=0.65)

        self.conn=pymysql.connect(host="localhost", user="root", password="root",db="dbbank")
        self.cursor=self.conn.cursor()
        self.cursor.execute("select cname,cadd,cemail, cmob, cfname,cmname from tbaccount where acno=%s",(self.e2.get()) )
        row=self.cursor.fetchone()
        nam=row[0]
        add=row[1]
        mail=row[2]
        mob=row[3]
        fat=row[4]
        mot=row[5]
        self.e3.insert(0,nam)
        self.e4.insert(0,add)
        self.e5.insert(0,mail)
        self.e6.insert(0,mob)
        self.e7.insert(0,fat)
        self.e8.insert(0,mot)
        
    def modify(self):
        self.ano=self.e2.get()
        self.nam=self.e3.get()
        self.add=self.e4.get()
        self.mail=self.e5.get()
        self.mob=self.e6.get()
        self.fat=self.e7.get()
        self.mot=self.e8.get()
        a=messagebox.askyesno("Alert", "Do you want to modify")
        if(a):
            conn=pymysql.connect(host="localhost", user="root", password="root",db="dbbank")
            cursor=conn.cursor()
            cursor.execute("update tbaccount set cname=%s,cadd=%s,cemail=%s, cmob=%s, cfname=%s,cmname=%s where acno=%s",(self.nam,self.add,self.mail,self.mob,self.fat,self.mot,self.ano) )
            conn.commit()
            self.root.destroy()
            
        
            

        
    


