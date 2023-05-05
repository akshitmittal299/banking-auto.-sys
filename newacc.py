from tkinter import *
from tkinter import messagebox
import pymysql.cursors
from PIL import Image , ImageTk
import datetime
import management
class New_acc:

    def __init__(self):
           
        self.date=datetime.date.today()
        self.root=Tk()
        self.root.title("PROJECT")
        self.root.state("zoomed")
        self.root.config(background="#FFFFCC")

        self.conn=pymysql.connect(host="localhost", user="root", password="root", db= "dbbank")
        self.cursor=self.conn.cursor()
        

        self.l1=Label(self.root, text="Open New Account")
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
        self.r1=Radiobutton(self.root,text="Male",variable=self.k, value="MALE")
        self.r2=Radiobutton(self.root,text="Female",variable=self.k, value="FEMALE")
        self.r1.config(background="#FFFFCC",font=(25))
        self.r2.config(background="#FFFFCC",font=(25))
        
        self.r1.place(relx=0.5, rely=0.38)
        self.r2.place(relx=0.6, rely=0.38)
##        self.e4=Entry(self.root)
##        self.e4.config(background="white",font=("Times New Roman", 25,"bold"))
##        self.e4.place(relx=0.5, rely=0.38)
##        
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
        self.e9.insert(0,self.date)
        self.e9.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e9.config(state="disabled")
        self.e9.place(relx=0.5, rely=0.68)
        
        
        self.e0=Entry(self.root)
        self.e0.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e0.place(relx=0.5, rely=0.74)

        self.b1=Button(self.root, text="Open Account", command=self.open)
        self.b1.config(background="black",foreground="white",font=("Times New Roman", 25,"bold"))
        self.b1.place(relx=0.4, rely=0.85)
        
        self.generate()
        self.root.mainloop()
        obj=management.demo()
    def open(self):
        if(self.e2.get()=="" or self.e3.get()=="" or  self.e1.get()=="" or self.e5.get()=="" or self.e6.get()=="" or self.e7.get()=="" or self.e8.get()=="" or self.e9.get()=="" or self.e0.get()==""):
            messagebox.showerror("alert","Enter all the Entry")

        else:
            self.ano=self.e1.get()
            self.nam=self.e2.get()
            self.add=self.e3.get()
            self.gen=self.k.get()
            self.mail=self.e5.get()
            self.con=self.e6.get()
            self.fat=self.e7.get()
            self.mot=self.e8.get()
            self.dat=self.e9.get()
            self.bal=self.e0.get()
            self.conn=pymysql.connect(host="localhost", user="root", password="root", db= "dbbank")
            self.cursor=self.conn.cursor()
            self.cursor.execute("insert into tbaccount values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.ano,self.nam,self.add,self.gen,self.mail,self.con,self.fat,self.mot,self.dat,self.bal))
            self.conn.commit()    
            messagebox.showinfo("info","inserted successfully")
            self.root.destroy()
            
    def generate(self):
        self.cursor.execute("select ifnull(max(acno),0) from tbaccount")
        self.conn.commit()
        row= self.cursor.fetchone()
        ano=row[0]
        ano=ano+1
        self.e1.configure(state="normal")
        self.e1.delete(0,END)
        self.e1.insert(0, ano)
        self.e1.configure(state="disabled")
        
        




