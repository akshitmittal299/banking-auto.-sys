from tkinter import *
from tkinter import messagebox
import pymysql.cursors
from PIL import Image , ImageTk
import management
class Mini:
    def __init__(self):
        self.root=Tk()
        self.root.title("PROJECT")
        self.root.state("zoomed")
        self.root.config(background="#FFFFCC")
        self.l1=Label(self.root, text="MiniStatement")
        self.l1.config(background="#FFFFCC",font=("Times New Roman",40,"underline"))
        self.l1.place(relx=0.35, rely=0.03)

        self.conn=pymysql.connect(host="localhost", user="root", password="root", db= "dbbank")
        self.cursor=self.conn.cursor()

        self.l2=Label(self.root, text="Enter Account No. :")
        self.l2.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l2.place(relx=0.2, rely=0.15)

        self.e2=Entry(self.root)
        self.e2.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e2.place(relx=0.5, rely=0.15)

        self.b1=Button(self.root,text="Search", command=self.search)
        self.b1.config(background="white",font=("Times New Roman", 20,"bold"))
        self.b1.place(relx=0.43, rely=0.25)
        
        self.root.mainloop()
        l=management.demo()
    def search(self):
        self.ano=self.e2.get()
        
        self.cursor.execute("select * from tbaccount where acno=%s",(self.ano))
        row=self.cursor.rowcount
        if(row>0):
            row=self.cursor.fetchone()
            self.bal=row[9]
            self.display()
        else:
            messagebox.showerror("Alert","You do not have a account here!!!")
    def display(self):
        self.la=Label(self.root, text="Transaction Id:")
        self.la.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.la.place(relx=0.2, rely=0.35)

        self.l4=Label(self.root, text="Source Account No. :")
        self.l4.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l4.place(relx=0.2, rely=0.43)

        self.l5=Label(self.root, text="Destination Account No. :")
        self.l5.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l5.place(relx=0.2, rely=0.51)
        
        self.l6=Label(self.root, text="Transaction Type:")
        self.l6.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l6.place(relx=0.2, rely=0.59)

        self.l7=Label(self.root, text="Transaction Amount: ")
        self.l7.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l7.place(relx=0.2, rely=0.67)

        self.l8=Label(self.root, text="Transaction Date:")
        self.l8.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l8.place(relx=0.2, rely=0.75)

        self.l9=Label(self.root, text="Transaction Time:")
        self.l9.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l9.place(relx=0.2, rely=0.83)

        self.e5=Entry(self.root)
        self.e5.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e5.place(relx=0.5, rely=0.35)
        
        self.e6=Entry(self.root)
        self.e6.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e6.place(relx=0.5, rely=0.43)
        
        self.e7=Entry(self.root)
        self.e7.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e7.place(relx=0.5, rely=0.51)
        
        self.e8=Entry(self.root)
        self.e8.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e8.place(relx=0.5, rely=0.59)
        
        self.e9=Entry(self.root)
        self.e9.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e9.place(relx=0.5, rely=0.67)
        
        
        self.e0=Entry(self.root)
        self.e0.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e0.place(relx=0.5, rely=0.75)

        self.e1=Entry(self.root)
        self.e1.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e1.place(relx=0.5, rely=0.83)

        self.a1=Listbox(self.root, selectmode =SINGLE)
        self.a1.config(height=60,width=50)
        self.a1.bind("<Double-Button-1>",self.fetchsingle)
        self.a1.place(relx=0.8,rely=0.0)
        
        self.cursor.execute("select transid from tbtransaction where transscraccno=%s or transdestaccno = %s",(self.ano, self.ano))
        self.a1.delete(0,END)
        index=0
        for row in self.cursor:
            self.a1.insert(index, row)
            index=index+1
    def fetchsingle(self,evt):
        ind= self.a1.curselection()
        val=self.a1.get(ind)
        self.e1.delete(0,END)
        self.e5.delete(0,END)
        self.e6.delete(0,END)
        self.e7.delete(0,END)
        self.e8.delete(0,END)
        self.e9.delete(0,END)
        self.e0.delete(0,END)
        self.cursor.execute("select * from tbtransaction where transid=%s",(val))
        row=self.cursor.fetchone()
        self.e1.insert(0, row[0])
        self.e5.insert(0, row[1])
        self.e6.insert(0, row[2])
        self.e7.insert(0, row[3])
        self.e8.insert(0, row[4])
        self.e9.insert(0, row[5])
        self.e0.insert(0, row[6])
        

        
