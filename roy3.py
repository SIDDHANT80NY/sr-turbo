# admin login
print("hello")
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image


''' mainly used pithon libraries for GUI are:-1)kivy 2)Qt 3)wxPython 4)Tkinter

Tkinter:- its an inbuilt pithon module used to create simple GUI apps:(most commonly used) '''


class login:
    def __init__(self, root):
        # _init_ is a special_method just like special_variable eg _name_
        self.root = root
        self.root.title('SR MOTO_WORLD')
        self.root.geometry("640x350+0+0")
        self.root.resizable(False, False)

        # now for baground image ->
        self.bg = ImageTk.PhotoImage(Image.open(r".vscode\WhatsApp Image 2021-03-23 at 12.36.09 AM.jpeg"))
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.icon = ImageTk.PhotoImage(Image.open(r"LOGO (1).jpg"))
        self.icon_photo = Label(self.root, image=self.icon).grid(row=9,column=1)

        # now for login frame ->
        Frame_login = Frame(self.root, bg="black")
        Frame_login.place(x=100, y=100, height=179, width=440)


        lb1_user = Label(Frame_login, text="User name:-", font=("Goudy old style", 18, "bold"), fg="red",
                         bg="black").grid(row=0,column=0)
        self.txt_user = Entry(Frame_login, font=("times new roman", 20), bg="lightgray")
        self.txt_user.grid(row=0,column=1)

        lb2_userp = Label(Frame_login, text="password:-", font=("Goudy old style", 18, "bold"), fg="red",
                          bg="black").grid(row=1,column=0)
        self.txt_userp = Entry(Frame_login, font=("times new roman", 20), bg="lightgray")
        self.txt_userp.grid(row=1,column=1)

        # For adding button ->
        Login = Button(Frame_login, command=self.login2_function, text="Login", fg="blue", bg="black",
                       font=("times new roman", 20)).grid(row=2,column=1)
        back = Button(Frame_login, command=self.back_function1, text="back", fg="yellow", bg="black",
                      font=("times new roman",20)).grid(row=3,column=1)


    def login2_function(self):
        if self.txt_userp.get() == "" or self.txt_user.get() == "":
            messagebox.showerror("error", "all fields are required", parent=self.root)
        elif self.txt_userp.get() != "maths" or self.txt_user.get() != "at9422":
            messagebox.showerror("error", "INVALID USER NAME/PASSWORD", parent=self.root)

        else:
            messagebox.showinfo("welcome", "WELCOME MASTER", parent=self.root)
            self.root.destroy()
            import roy2

    def back_function1(self):
        self.root.destroy()
        import roy


root = Tk()
obj = login(root)
root.mainloop()
