from tkinter import *
from tkinter import messagebox,ttk
import pymysql.cursors
from PIL import Image , ImageTk
import forget
import management
class Login:
    def __init__(self):
        self.root=Tk()
        self.root.title("PROJECT")
        self.root.state("zoomed")
        self.root.config(background="#FFFFCC")

        self.l1=Label(self.root, text="LOGIN SECTION")
        self.l1.config(background="#FFFFCC",font=("Times New Roman",40,"underline"))
        self.l1.place(relx=0.35, rely=0.03)

        self.l2=Label(self.root, text="ADMIN ID:")
        self.l2.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l2.place(relx=0.3, rely=0.2)

        self.l3=Label(self.root, text="ADMIN PASSWORD:")
        self.l3.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l3.place(relx=0.2, rely=0.3)
        
        self.e1=Entry(self.root)
        self.e1.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e1.place(relx=0.5, rely=0.2)
        
        self.e2=Entry(self.root, show="*")
        self.e2.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e2.place(relx=0.5, rely=0.3)

        self.b1=Button(self.root,text="FORGOT PASSWORD", command=self.forgot)
        self.b1.config(background="white",font=("Times New Roman", 15,"bold"))
        self.b1.place(relx=0.3, rely=0.4)

        self.b2=Button(self.root,text="LOGIN",command=self.login)
        self.b2.config(background="white",font=("Times New Roman", 15,"bold"))
        self.b2.place(relx=0.5, rely=0.4)
        
        self.aa=self.e1.get()
        self.root.mainloop()
    def forgot(self):
        self.root.destroy()
        l1=forget.Forget()
            
    def login(self):
        self.aa=self.e1.get()
        self.ab=self.e2.get()
        conn=pymysql.connect(host="localhost", user="root", password="root",db="dbbank")
        cursor=conn.cursor()
        cursor.execute("select * from tbadmin where admid=%s",(self.aa))
        conn.commit()
        row=cursor.rowcount
        
        if (row>0):
            row=cursor.fetchone()
            if(self.ab==row[1]):
                self.root.destroy()
                o1=management.demo(self.aa)#object
        else:
            messagebox.showinfo("info","Invalid ID or Password")

        
