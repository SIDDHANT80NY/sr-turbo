# admin home
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
from PIL import ImageTk, Image
import mysql.connector
import os, shutil
from tkinter import filedialog
import pymysql
import base64

class admin_home:
    def __init__(self, root):
     self.root = root
     self.root.title('SR_TURBO_')
     self.root.geometry("1000x300+0+0")
     self.root.resizable(False, False)

     self.bg = ImageTk.PhotoImage(Image.open(r"WhatsApp Image 2021-03-23 at 12.36.09 AM.jpg"))
     self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

     Frame_detail = Frame(self.root,bg="black")
     Frame_detail.place(x=50, y=0, height=300, width=900)

     lb1_carn = Label(Frame_detail, text="Car Name:-", font=("Goudy old style", 15, "bold"), fg="red",bg="black").grid(row=0,column=0)
     self.txt_carn = Entry(Frame_detail,width=20, font=("times new roman", 15), bg="white")
     self.txt_carn.grid(row=0,column=1)

     lb2_carb = Label(Frame_detail, text="Brand:-", font=("Goudy old style", 15, "bold"), fg="red",bg="black").grid(row=0,column=2)
     self.txt_carb = Entry(Frame_detail,width=20, font=("times new roman", 15), bg="white")
     self.txt_carb.grid(row=0,column=3)

     lb3_cost = Label(Frame_detail, text="starting ex-showroom cost:-", font=("Goudy old style", 15, "bold"), fg="red", bg="black").grid(row=1, column=0)
     self.txt_cost = Entry(Frame_detail, width=20, font=("times new roman", 15), bg="white")
     self.txt_cost.grid(row=1, column=1)

     lb4_mileage = Label(Frame_detail, text="mileage:-", font=("Goudy old style", 15, "bold"), fg="red",bg="black").grid(row=1, column=2)
     self.txt_mileage = Entry(Frame_detail, width=20, font=("times new roman", 15), bg="white")
     self.txt_mileage.grid(row=1, column=3)

     lb5_Engine = Label(Frame_detail, text="Engine Displ.:-", font=("Goudy old style", 15, "bold"), fg="red", bg="black").grid(row=2, column=0)
     self.txt_Engine = Entry(Frame_detail, width=20, font=("times new roman", 15), bg="white")
     self.txt_Engine.grid(row=2, column=1)

     lb6_speed = Label(Frame_detail, text="Top Speed:-", font=("Goudy old style", 15, "bold"), fg="red", bg="black").grid(row=2, column=2)
     self.txt_speed = Entry(Frame_detail, width=20, font=("times new roman", 15), bg="white")
     self.txt_speed.grid(row=2, column=3)

     lb7_safety = Label(Frame_detail, text="safety wrating:-", font=("Goudy old style", 15, "bold"), fg="red",bg="black").grid(row=3, column=0)
     self.txt_safety = Entry(Frame_detail, width=20, font=("times new roman", 15), bg="white")
     self.txt_safety.grid(row=3, column=1)

     lb8_type = Label(Frame_detail, text="Type:-", font=("Goudy old style", 15, "bold"), fg="red",bg="black").grid(row=3, column=2)
     self.txt_type  = Entry(Frame_detail, width=20, font=("times new roman", 15), bg="white")
     self.txt_type.grid(row=3, column=3)

     lb9_fuel = Label(Frame_detail, text="Fuel:-", font=("Goudy old style", 15, "bold"), fg="red",bg="black").grid(row=4, column=0)
     self.txt_fuel = Entry(Frame_detail, width=20, font=("times new roman", 15), bg="white")
     self.txt_fuel.grid(row=4, column=1)

     lb10_seat = Label(Frame_detail, text="seats:-", font=("Goudy old style", 15, "bold"), fg="red", bg="black").grid(row=4, column=2)
     self.txt_seat = Entry(Frame_detail, width=20, font=("times new roman", 15), bg="white")
     self.txt_seat.grid(row=4, column=3)

     lb11_space = Label(Frame_detail, text="Boot Space(IN LITERS):-", font=("Goudy old style", 15, "bold"), fg="red", bg="black").grid(row=5, column=0)
     self.txt_space = Entry(Frame_detail, width=20, font=("times new roman", 15), bg="white")
     self.txt_space.grid(row=5, column=1)

     lb12_image = Label(Frame_detail, text="image:-", font=("Goudy old style", 15, "bold"), fg="red", bg="black").grid(row=6, column=0)
     self.button = Button(Frame_detail,font=("Goudy old style", 15, "bold"),fg="red", bg="black", text="Browse A file", command=self.fileDailog)
     self.button.grid(column=1,row=6)

     UPDATE = Button(Frame_detail,command=self.UPDATEE_function, text="UPDATE", fg="blue", bg="black",
                     font=("times new roman", 15)).grid(row=7, column=3)

     back = Button(Frame_detail, command=self.back_function1, text="back to login", fg="yellow", bg="black",
                       font=("times new roman", 15)).grid(row=8,column=3)
                
     def btton(self):
      self.button = tkinter.Button(Frame_detail, text="Browse Afile", command=self.fileDailog)
      self.button.grid(column=3,row=6)

    def UPDATEE_function(self):
        if self.txt_space.get() == "" or self.txt_seat.get() == "" or self.txt_fuel.get() == "" or self.txt_type.get() == "" or self.txt_safety.get() == "" or self.txt_speed.get() == "" or self.txt_Engine.get() == "" or self.txt_mileage.get() == "" or self.txt_cost.get() == "" or self.txt_carb.get() == "" or self.txt_carn.get() == "":
            messagebox.showerror("error", "all fields are required", parent=self.root)
        else:
          con = mysql.connector.connect(host="localhost",user="root",passwd="root",database="roy")
          cur = con.cursor(buffered=True)
          st = "INSERT INTO detailss (name,brand,cost,mileage,engine,speed,safty,type,fuel,seat,space,image) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
          vals = (self.txt_carn.get(), self.txt_carb.get(),self.txt_cost.get(),self.txt_mileage.get(),self.txt_Engine.get(),self.txt_speed.get(),self.txt_safety.get(),self.txt_type.get(),self.txt_fuel.get(),self.txt_seat.get(),self.txt_space.get(),self.data)
          cur.execute(st,vals)
          con.commit()
          con.close()
          messagebox.showinfo("welcom", "UPLOAD SUCCESSFUL", parent=self.root)

        
    def back_function1(self):
        self.root.destroy()
        import roy

   

    def fileDailog(self):
     self.fileName = filedialog.askopenfilename(initialdir = "/", title="Select A File",filetype=(("jpeg",".jpg"),("png",".png")))
     print(self.fileName)
     with open(self.fileName, "rb") as image_file:
          self.data = base64.b64encode(image_file.read())
     

     

root = Tk()
obj = admin_home(root)
root.mainloop()
