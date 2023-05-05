from tkinter import *
from tkinter import messagebox
import pymysql.cursors
from PIL import Image , ImageTk
import management
class View:
    def __init__(self):
        self.root=Tk()
        self.root.title("PROJECT")
        self.root.state("zoomed")
        self.root.config(background="#FFFFCC")

        self.l1=Label(self.root, text="View All Accounts")
        self.l1.config(background="#FFFFCC",font=("Times New Roman",40,"underline"))
        self.l1.place(relx=0.35, rely=0.01)

        self.l2=Label(self.root, text="Account No.:")
        self.l2.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l2.place(relx=0.2, rely=0.2)

        self.l3=Label(self.root, text="Customer Name:")
        self.l3.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l3.place(relx=0.2, rely=0.26)

        self.la=Label(self.root, text="Customer Gender:")
        self.la.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.la.place(relx=0.2, rely=0.38)

        self.l4=Label(self.root, text="Customer Address:")
        self.l4.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l4.place(relx=0.2, rely=0.32)

        self.l5=Label(self.root, text="Customer Email:")
        self.l5.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l5.place(relx=0.2, rely=0.44)
        
        self.l6=Label(self.root, text="Customer Contact:")
        self.l6.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l6.place(relx=0.2, rely=0.50)

        self.l7=Label(self.root, text="Customer Father's Name: ")
        self.l7.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l7.place(relx=0.2, rely=0.56)

        self.l8=Label(self.root, text="Customer Mother's Name:")
        self.l8.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l8.place(relx=0.2, rely=0.62)

        self.l9=Label(self.root, text="Opening Date:")
        self.l9.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l9.place(relx=0.2, rely=0.68)
        
        self.l0=Label(self.root, text="Opening Balance:")
        self.l0.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l0.place(relx=0.2, rely=0.74)
        
        self.e1=Entry(self.root)
        self.e1.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e1.place(relx=0.5, rely=0.2)
        
        self.e2=Entry(self.root)
        self.e2.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e2.place(relx=0.5, rely=0.26)
        
        self.e3=Entry(self.root)
        self.e3.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e3.place(relx=0.5, rely=0.32)

        self.k=StringVar()
        self.k.set('MALE')
##        self.r1=Radiobutton(self.root,text="Male",variable=self.k, value="MALE")
##        self.r2=Radiobutton(self.root,text="Female",variable=self.k, value="FEMALE")
##        self.r1.config(background="#FFFFCC",font=(25))
##        self.r2.config(background="#FFFFCC",font=(25))
##        
##        self.r1.place(relx=0.5, rely=0.38)
##        self.r2.place(relx=0.6, rely=0.38)
        self.e4=Entry(self.root)
        self.e4.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e4.place(relx=0.5, rely=0.38)
        
        self.e5=Entry(self.root)
        self.e5.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e5.place(relx=0.5, rely=0.44)
        
        self.e6=Entry(self.root)
        self.e6.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e6.place(relx=0.5, rely=0.50)
        
        self.e7=Entry(self.root)
        self.e7.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e7.place(relx=0.5, rely=0.56)
        
        self.e8=Entry(self.root)
        self.e8.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e8.place(relx=0.5, rely=0.62)
        
        self.e9=Entry(self.root)
        self.e9.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e9.place(relx=0.5, rely=0.68)
        
        
        self.e0=Entry(self.root)
        self.e0.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e0.place(relx=0.5, rely=0.74)

        self.a1=Listbox(self.root, selectmode =SINGLE)
        self.a1.config(height=60,width=50)
        self.a1.bind("<Double-Button-1>",self.show)
        self.conn=pymysql.connect(host="localhost", user="root", password="root", db= "dbbank")
        self.cursor=self.conn.cursor()
        self.cursor.execute("select * from tbaccount")
        row= self.cursor.rowcount
        for i in range (row):
            row=self.cursor.fetchone()
            self.a1.insert(i, row[0])
        self.a1.place (relx=0.8, rely=0.0)
        self.root.mainloop()
        obj=management.demo()
        
    def show(self,evt):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.e5.delete(0,END)
        self.e6.delete(0,END)
        self.e7.delete(0,END)
        self.e8.delete(0,END)
        self.e9.delete(0,END)
        self.e0.delete(0,END)
        self.rep=self.a1.curselection()
        self.ss=self.a1.get(self.rep)
        self.cursor.execute("select * from tbaccount where acno=%s",(self.ss))
        row=self.cursor.fetchone()
        self.e1.insert(0,row[0]) 
        self.e2.insert(0,row[1])    
        self.e3.insert(0,row[2])
        self.e4.insert(0,row[3])
        self.e5.insert(0,row[4])
        self.e6.insert(0,row[5])
        self.e7.insert(0,row[6])
        self.e8.insert(0,row[7])
        self.e9.insert(0,row[8])
        self.e0.insert(0,row[9])
