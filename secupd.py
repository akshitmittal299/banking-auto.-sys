from tkinter import *
from tkinter import messagebox
import pymysql.cursors
from PIL import Image , ImageTk
class secupd:
    def __init__(self):
        self.root=Tk()
        self.root.title("PROJECT")
        self.root.state("zoomed")
        self.root.config(background="#FFFFCC")

        self.l1=Label(self.root, text="Enter new security question:")
        self.l1.config(background="#FFFFCC",font=("Times New Roman",25,"bold"))
        self.l1.place(relx=0.2, rely=0.2)

        self.l2=Label(self.root, text="enter security answer :")
        self.l2.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l2.place(relx=0.2, rely=0.3)

        self.e1=Entry(self.root)
        self.e1.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e1.place(relx=0.5, rely=0.2)
        
        self.e2=Entry(self.root)
        self.e2.config(background="white",font=("Times New Roman", 25,"bold"))
        self.e2.place(relx=0.5, rely=0.3)

        
        self.l3=Label(self.root, text="Update Your Security question")
        self.l3.config(background="#FFFFCC",font=("Times New Roman", 40,"bold", "underline"))
        self.l3.place(relx=0.25, rely=0.03)

        self.b1=Button(self.root, text="Update",command=self.update)
        self.b1.config(background="white",font=(30))
        self.b1.place(relx=0.45, rely=0.4)


        self.root.mainloop()
    def update(self):
        m= messagebox.askyesno("VALIDATE", "Do you want to continue:")
        if(m):
            conn=pymysql.connect(host="localhost", user="root",password="root", db="dbbank")
            cursor=conn.cursor()
            cursor.execute("update tbadmin set admsecques=%s , admsecans=%s where admid= 'aa'",(self.e1.get(), self.e2.get()))
            conn.commit()
            messagebox.showinfo("validation", "password updated successfully")
            self.root.destroy()
        else:
            messagebox.showerror("alert", "password and confirm password does not match")
            self.e1.delete(0,END)
            self.e2.delete(0,END)

        
    
