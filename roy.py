# login
print("hello")
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import pymysql

''' mainly used pithon libraries for GUI are:-1)kivy 2)Qt 3)wxPython 4)Tkinter

Tkinter:- its an inbuilt pithon module used to create simple GUI apps:(most commonly used) '''


class login:
    def __init__(self, root):
        # _init_ is a special_method just like special_variable eg _name_
        self.root = root
        self.root.title('SR MOTO_WORLD')
        self.root.geometry("700x420+0+0")
        self.root.resizable(False, False)

        # now for baground image ->
        self.bg = ImageTk.PhotoImage(Image.open(r".vscode\WhatsApp Image 2021-03-23 at 12.36.09 AM.jpeg"))
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # now for login frame ->
        Frame_login = Frame(self.root, bg="black")
        Frame_login.place(x=50, y=50, height=320, width=600)

        self.icon = ImageTk.PhotoImage(Image.open(r"LOGO (1).jpg"))
        self.icon_photo = Label(Frame_login, image=self.icon).grid(row=9,column=1)

        title = Label(Frame_login, text="Login Here:-", font=("Impact", 20, "bold"),fg="blue",bg="black").grid(row=0,column=1)
        desc = Label(Frame_login, text="Login here to get best car details comparison in India",
                     font=("Goudy old style", 11, "bold"),fg="blue",bg="black").grid(row=1,column=1)

        lb1_user = Label(Frame_login, text="User Name:-", font=("Goudy old style", 15, "bold"), fg="red",
                         bg="black").grid(row=3,column=0)
        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_user.grid(row=3,column=1)

        lb2_userp = Label(Frame_login, text="Password:-", font=("Goudy old style", 15, "bold"), fg="red",
                          bg="black").grid(row=5,column=0)
        self.txt_userp = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_userp.grid(row=5,column=1)

        # For adding button ->
        Login = Button(Frame_login, command=self.login_function, text="Login", fg="blue", bg="black",
                       font=("times new roman", 15)).grid(row=7,column=0)
        Register = Button(Frame_login,command=self.Register_function1,text="Register", fg="green", bg="black", font=("times new roman", 15)).grid(row=7,column=1)
        admin = Button(Frame_login, command=self.admin_function2, text="ADMIN", fg="dark orange", bg="black",
                          font=("times new roman", 15)).grid(row=7,column=2)

        # for logo icon->
        lb3_IGNORE = Label(Frame_login, text="IGNORE", font=("Goudy old style", 15, "bold"), fg="black",bg="black").grid(row=8,column=1)
        self.icon = ImageTk.PhotoImage(Image.open(r"LOGO (1).jpg"))
        self.icon_photo = Label(Frame_login, image=self.icon).grid(row=9,column=1)

        # DEFINING FUNCTIONS ->

    def login_function(self):
        if self.txt_userp.get() == "" or self.txt_user.get() == "":
            messagebox.showerror("error", "all fields are required", parent=self.root)
        else:
            con = mysql.connector.connect(host="localhost",user="root",passwd="root",database="roy")
            cur = con.cursor(buffered=True)
            st = "select * from userss where username=%s and password=%s"
            vals = (self.txt_user.get(), self.txt_userp.get())
            cur.execute(st,vals)
            rows = cur.fetchone()
            if rows == None:
             messagebox.showerror("error", "INVALID USER NAME/PASSWORD", parent=self.root)
            else:
             messagebox.showinfo("welcom", "WELCOM TO SR MOTOR WORLD", parent=self.root)
             self.root.destroy()
             import roy4    
            con.commit()
            con.close()

    def Register_function1(self):
        self.root.destroy()
        import roy1

    def admin_function2(self):
        self.root.destroy()
        import roy3


root = Tk()
obj = login(root)
root.mainloop()
