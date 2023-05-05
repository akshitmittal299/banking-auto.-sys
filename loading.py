from tkinter import *
from tkinter.ttk import Progressbar
import pymysql.cursors
import threading
from PIL import Image , ImageTk
import time
import login
class Loading:
    def __init__(self):
        self.root=Tk()
        self.root.title("PROJECT")
        self.root.state("zoomed")
        self.root.config(background="#FFFFCC")

        self.l1=Label(self.root,text="LOADING SECTION")
        self.l1.config(background="#FFFFCC",font=("Times New Roman", 40,"bold", "italic","underline"))
        self.l1.place(relx=0.35 , rely=0.1)

        self.l2=Label(self.root)
        self.l2.config(background="#FFFFCC",font=("Times New Roman", 25,"bold"))
        self.l2.place(relx=0.2 , rely=0.7)
        
        self.a1=IntVar()
        self.pb=Progressbar(self.root, orient=HORIZONTAL, length=900)
        self.pb.config(mode ='determinate', maximum=100, variable=self.a1)
        self.pb.place(relx=0.2, rely=0.8)
        tup=(101,)
        self.t1=threading.Thread(target=self.move,args=tup,name="first")
        self.t1.start()
        self.root.after(500,self.check)
        self.root.mainloop()

    def move(self,a):
        for i in range(a):
            self.a1.set(i)
            self.l2.config(text="LOADING "+str(self.a1.get())+"%")
            time.sleep(0.01)
    def check(self):
        if self.a1.get()!=100:
            self.root.after(500,self.check)
        else:
            self.root.destroy()
            l1=login.Login()


