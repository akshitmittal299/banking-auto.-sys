from tkinter import *
from tkinter import messagebox
import pymysql.cursors
from PIL import Image , ImageTk
import datetime
import time
import management
class Transfer:
    def __init__(self):
        self.root=Tk()
        self.root.title("PROJECT")
        self.root.state("zoomed")
        self.root.config(background="#FFFFCC")
        self.l1=Label(self.root, text="Transfer")
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
        
        self.l6=Label(self.f1, text="Destination Account No. :")
        self.l6.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l6.place(relx=0.1, rely=0.23)

        self.e3=Entry(self.f1)
        self.e3.insert(0,self.bal)
        self.e3.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e3.place(relx=0.5, rely=0.13)

        self.e4=Entry(self.f1)
        self.e4.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e4.place(relx=0.5, rely=0.23)

        self.b2=Button(self.f1,text="check",command=self.check)
        self.b2.config(background="white",font=("Times New Roman", 20,"bold"))
        self.b2.place(relx=0.4, rely=0.33)
    def check(self):
        ano=self.e4.get()
        self.cursor.execute("select * from tbaccount where acno =%s",(ano))
        row= self.cursor.rowcount
        if (row>0):
            self.col=self.cursor.fetchone()
            self.display2()
        else:
            messagebox.showerror("ALERT","The recieving account does not exist")
    def display2(self):
        
        self.l7=Label(self.f1, text="Amount to be Transfered:")
        self.l7.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l7.place(relx=0.1, rely=0.46)

        self.e5=Entry(self.f1)
        self.e5.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e5.place(relx=0.5, rely=0.46)

        self.b2=Button(self.f1,text="transfer",command=self.transfer)
        self.b2.config(background="white",font=("Times New Roman", 20,"bold"))
        self.b2.place(relx=0.4,rely=0.55)
    def transfer(self):
        amo=self.e5.get()
        if(int(amo)>=0):
            
            if(self.bal>int(amo)):
                m=messagebox.askyesno("ALERT", "Do you want to continue:")
                if (m):
                    n=self.generateid()
                    (s,t)=self.datetime()
                
                    ano=self.e2.get()
                    send=self.e4.get()
                    self.bal=self.bal- int(amo)
                    rbal=self.col[9]
                    rbal=rbal+ int(amo)
                    self.cursor.execute("update tbaccount set balance=%s where acno=%s",(str(self.bal),ano))
                    self.cursor.execute("update tbaccount set balance =%s where acno=%s",(str(rbal), send))
                    self.conn.commit()
                    self.cursor.execute("insert into tbtransaction values(%s,%s,%s,'Transfer',%s,%s,%s)",(n,ano,send,str(amo),s,t))
                    self.conn.commit()
                    messagebox.showinfo("VALIDATE","Amount "+amo+"transfered from"+str(ano) +"to" +str(send))
                else :
                      pass
            else:
                print("9")
        else:
            messagebox.showerror("ALERT","enter amount in postive")
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
           

        
    

    
