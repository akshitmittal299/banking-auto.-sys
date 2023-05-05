from tkinter import *
from tkinter import messagebox
import pymysql.cursors
from PIL import Image , ImageTk
import editpwd
class Forget:
    def __init__(self):
        self.root=Tk()
        self.root.title("PROJECT")
        self.root.state("zoomed")
        self.root.config(background="#FFFFCC")

        self.l4=Label(self.root, text="FORGOT PASSWORD")
        self.l4.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l4.place(relx=0.35, rely=0.03)

        self.f1=Frame(self.root,height=700, bd=5,width=1200, relief=RIDGE)
        self.f1.config(background="#FFFFCC")
        self.f1.place(relx=0.1,rely=0.1)

        
        self.l5=Label(self.f1, text="Enter Admin Id:")
        self.l5.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l5.place(relx=0.2, rely=0.13)
        
        self.e3=Entry(self.f1)
        self.e3.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e3.place(relx=0.5, rely=0.13)

        self.b3=Button(self.f1,text="Check", command=self.check)
        self.b3.config(background="white",font=("Times New Roman", 15,"bold"))
        self.b3.place(relx=0.6, rely=0.25)
        self.root.mainloop()
    def check(self):
        adid=self.e3.get()
        conn=pymysql.connect(host="localhost", user="root", password="root",db="dbbank")
        cursor=conn.cursor()
        cursor.execute("select admsecques, admsecans from tbadmin where admid =%s",(adid))
        conn.commit()
        row=cursor.rowcount
        if (row>0):
            row=cursor.fetchone()
            self.ans=row[1]
            self.f2=Frame(self.f1,height=400, bd=5,width=900, relief=RIDGE)
            self.f2.config(background="#FFFFCC")
            self.f2.place(relx=0.1,rely=0.38)

            self.l6=Label(self.f2, text="    Your Security Question is :")
            self.l6.config(background="#FFFFCC",font=("Times New Roman", 20,"bold"))
            self.l6.place(relx=0.1, rely=0.03)
            
            self.l7=Label(self.f2,text=row[0])
            self.l7.config(background="#FFFFCC",font=("Times New Roman", 20,"bold"))
            self.l7.place(relx=0.5, rely=0.03)
        
        
            self.e4=Entry(self.f2,width=40)
            self.e4.config(background="white",font=("Times New Roman", 25,"bold"))
            self.e4.place(relx=0.1, rely=0.23)

            self.b4=Button(self.f2,text="Verify", command=self.verify)
            self.b4.config(background="white",font=("Times New Roman", 15,"bold"))
            self.b4.place(relx=0.43, rely=0.55)

        else:
            messagebox.showerror("alert"," invalid id")
            self.e3.delete(0,END)
    def verify(self):
        adid=self.e3.get()
        if(self.e4.get()==self.ans):
            self.root.destroy()
            o1=editpwd.Editpwd(adid)
        else:
            messagebox.showerror("alert", "wrong answer try again!!")
            self.e4.delete(0,END)
    
    

