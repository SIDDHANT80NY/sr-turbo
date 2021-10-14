# register
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import pymysql

class User_Register:
    def __init__(self, root):
        self.root = root
        self.root.title('SR_TURBO_registerPage')
        self.root.geometry("1200x700+0+0")
        self.root.resizable(False, False)

        self.bg = ImageTk.PhotoImage(Image.open(r"WhatsApp Image 2021-03-23 at 12.36.09 AM.jpg"))
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.icon = ImageTk.PhotoImage(Image.open(r"LOGO (1).jpg"))
        self.icon_photo = Label(self.root, image=self.icon).grid(row=0,column=1)

        Frame_login = Frame(self.root, bg="black")
        Frame_login.place(x=100, y=150, height=480, width=950)
        title = Label(Frame_login, text="                                                              Register Here:-", font=("Impact", 20, "bold"), fg="blue",bg="black").place(x=10, y=00)

        lb1_user = Label(Frame_login, text="User name:-", font=("Goudy old style", 15, "bold"), fg="red",bg="black").place(x=10, y=40)
        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_user.place(x=10, y=70 , width=800, height=35)

        lb2_userp = Label(Frame_login, text="Set Password:-", font=("Goudy old style", 15, "bold"), fg="red",bg="black").place(x=10, y=110)
        self.txt_userp = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_userp.place(x=10, y=140 , width=800, height=35)

        lb3_userp1 = Label(Frame_login, text="Re-entre Password:-", font=("Goudy old style", 15, "bold"), fg="red",bg="black").place(x=10, y=180)
        self.txt_userp1 = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_userp1.place(x=10, y=210 , width=800, height=35)

        lb4_phoneno = Label(Frame_login, text="Enter Your Phone Number:-", font=("Goudy old style", 15, "bold"), fg="red",bg="black").place(x=10, y=250)
        self.txt_phoneno = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_phoneno.place(x=10, y=280 , width=800, height=35)

        lb5_age = Label(Frame_login, text="Enter Your age:-", font=("Goudy old style", 15, "bold"), fg="red",bg="black").place(x=10, y=320)
        self.txt_age = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_age.place(x=10, y=350 , width=800, height=35)

        register = Button(Frame_login, command=self.Register_function, text="          Register          ", fg="green", bg="black", font=("times new roman", 15)).place( x=10, y=390)
        back = Button(Frame_login, command=self.back_function1, text="back", fg="yellow", bg="black",
                       font=("times new roman", 15)).place(x=10, y=430)

    def Register_function(self):
        if self.txt_user.get() == "" or self.txt_userp.get() == "" or self.txt_userp1.get() == "" or self.txt_phoneno.get() == "" or self.txt_age.get() == "":
            messagebox.showerror("error", "all fields are required", parent=self.root)
        elif self.txt_userp.get() != self.txt_userp1.get():
             messagebox.showerror("Error","Password does not match",parent = self.root)
        elif int(self.txt_age.get())>100:
                messagebox.showerror("Error","madarchod mar aab",parent = self.root)
        elif int(self.txt_phoneno.get())<1000000000:
                messagebox.showerror("Error","Invalid contact number!",parent = self.root)
        else:
            con = mysql.connector.connect(host="localhost",user="root",passwd="root",database="roy")
            cur = con.cursor(buffered=True)
            st = "INSERT INTO userss (username,password,phoneno,age) VALUES (%s, %s, %s, %s)"
            vals = (self.txt_user.get(), self.txt_userp.get(),self.txt_phoneno.get(),self.txt_age.get())
            cur.execute(st,vals)
            con.commit()
            con.close()
            messagebox.showinfo("welcom", "registered SUCCESSFULLY", parent=self.root)

    def back_function1(self):
        self.root.destroy()
        import roy

root = Tk()
obj = User_Register(root)
root.mainloop()
