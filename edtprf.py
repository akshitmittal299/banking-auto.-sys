from tkinter import *
from tkinter import messagebox,ttk
import pymysql.cursors
from PIL import Image , ImageTk
import management

class Edit:
    def __init__(self,aid):
        self.adminid=aid
        self.root=Tk()
        self.root.title("PROJECT")
        self.root.state("zoomed")
        self.root.config(background="#FFFFCC")

        self.conn=pymysql.connect(host="localhost", user="root", password="root", db= "dbbank")
        self.cursor=self.conn.cursor()
        

        self.l1=Label(self.root, text="Admin's Profile")
        self.l1.config(background="#FFFFCC",font=("Times New Roman",40,"underline"))
        self.l1.place(relx=0.35, rely=0.1)

        self.l2=Label(self.root, text="Name:")
        self.l2.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l2.place(relx=0.2, rely=0.3)

        self.l3=Label(self.root, text="Address:")
        self.l3.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l3.place(relx=0.2, rely=0.4)

        self.la=Label(self.root, text="Mobile no.:")
        self.la.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.la.place(relx=0.2, rely=0.5)

        self.l4=Label(self.root, text="E.mail Id:")
        self.l4.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l4.place(relx=0.2, rely=0.6)

        self.e1=Entry(self.root)
        self.e1.config(background="white",font=("Times New Roman", 25,"bold"), width=30)
        self.e1.place(relx=0.5, rely=0.3)
        
        self.e2=Entry(self.root)
        self.e2.config(background="white",font=("Times New Roman", 25,"bold"), width=30)
        self.e2.place(relx=0.5, rely=0.4)
        
        self.e3=Entry(self.root)
        self.e3.config(background="white",font=("Times New Roman", 25,"bold"), width=30)
        self.e3.place(relx=0.5, rely=0.5)

        self.e5=Entry(self.root)
        self.e5.config(background="white",font=("Times New Roman", 25,"bold"), width=30)
        self.e5.place(relx=0.5, rely=0.6)

        self.b1=Button(self.root, text="modify", command=self.edit)
        self.b1.config(background="black",foreground="white",font=("Times New Roman", 25,"bold"))
        self.b1.place(relx=0.4, rely=0.7)
        
        

        self.cursor.execute("select * from tbadmin where admid=%s",self.adminid)
        row=self.cursor.fetchone()
        self.e1.insert(0,row[4])#name
        self.e2.insert(0,row[5])#add
        self.e3.insert(0,row[7])#pho
        self.e5.insert(0,row[6])#id
        self.root.mainloop()
    def edit(self):
        nam=self.e1.get()
        add=self.e2.get()
        pho=self.e3.get()
        eid=self.e5.get()
        if (nam=="" or self.e2.get()=="" or self.e3.get()=="" or self.e5.get()==""):
            messagebox.showerror("ALERT","fields can not be empty")
        else:
            try:
                mob=int(pho)
            except ValueError as e:
                messagebox.showerror("ALERT", "Enter mobile no in integer form")
            if(len(pho)!=10):
                messagebox.showerror("ALERT", "mobile no should contain 10 integers")
            elif ("@gmail.com" or "@yahoo.com"  in eid):
                m=messagebox.askyesno("VALIDATE", " Do you want to continue:")
                if(m):
                    self.cursor.execute("update tbadmin set admname=%s, admadd=%s, admemail=%s, admphno=%s where admid=%s", (nam,add,eid,pho,self.adminid))
                    self.conn.commit()
                    messagebox.showinfo("validate", "updated successfully")
                    self.root.destroy()
                    obj=management.demo()
                else:
                    pass
    
        
