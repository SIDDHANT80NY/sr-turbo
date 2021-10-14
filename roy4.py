# user home
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import os, shutil
from tkinter import filedialog
import pymysql
import base64


class User_home:
    def __init__(self, root):
        self.root = root
        self.root.title('SR_TURBO_')
        self.root.geometry("1520x610+0+0")
        self.root.resizable(False, False)

        self.bg = ImageTk.PhotoImage(Image.open(r"WhatsApp Image 2021-03-23 at 12.36.09 AM.jpg"))
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # frame 1
        Frame_one1 = Frame(self.root, bg="black")
        Frame_one1.place(x=0, y=0, height=650, width=400)

        lb1_carn0 = Label(Frame_one1, text="Brand Name:-", font=("Goudy old style", 15, "bold"), fg="red",
                          bg="black").grid(row=0, column=0)
        self.txt_carn0 = Entry(Frame_one1, width=20, font=("times new roman", 15), bg="white")
        self.txt_carn0.grid(row=0, column=1)

        lb2_carb0 = Label(Frame_one1, text="Car Name:-", font=("Goudy old style", 15, "bold"), fg="red",
                          bg="black").grid(row=1, column=0)
        self.txt_carb0 = Entry(Frame_one1, width=20, font=("times new roman", 15), bg="white")
        self.txt_carb0.grid(row=1, column=1)

        SEARCHbutton1 = Button(Frame_one1, command=self.fetchone1_function1, text="Search", fg="blue", bg="black",
                               font=("times new roman", 13)).grid(row=2, column=2)

        self.carname = StringVar()
        self.brandname = StringVar()
        self.cost = StringVar()
        self.milage = StringVar()
        self.engine = StringVar()
        self.speed = StringVar()
        self.safty = StringVar()
        self.type = StringVar()
        self.fuel = StringVar()
        self.seat = StringVar()
        self.space = StringVar()

        lbA_carn0 = Label(Frame_one1, text="Car Name:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=3, column=0)
        self.txt_one = Entry(Frame_one1, textvariable=self.carname, width=20, font=("times new roman", 15), bg="white")
        self.txt_one.grid(row=3, column=1)

        lbB_carn0 = Label(Frame_one1, text="Brand Name:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=4, column=0)
        self.txt_two = Entry(Frame_one1, textvariable=self.brandname, width=20, font=("times new roman", 15),
                             bg="white")
        self.txt_two.grid(row=4, column=1)

        lbC_carn0 = Label(Frame_one1, text="Ex.S-Cost:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=5, column=0)
        self.txt_three = Entry(Frame_one1, textvariable=self.cost, width=20, font=("times new roman", 15), bg="white")
        self.txt_three.grid(row=5, column=1)

        lbD_carn0 = Label(Frame_one1, text="Milage:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=6, column=0)
        self.txt_four = Entry(Frame_one1, textvariable=self.milage, width=20, font=("times new roman", 15), bg="white")
        self.txt_four.grid(row=6, column=1)

        lbE_carn0 = Label(Frame_one1, text="Engine:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=7, column=0)
        self.txt_five = Entry(Frame_one1, textvariable=self.engine, width=20, font=("times new roman", 15), bg="white")
        self.txt_five.grid(row=7, column=1)

        lbF_carn0 = Label(Frame_one1, text="Speed:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=8, column=0)
        self.txt_six = Entry(Frame_one1, textvariable=self.speed, width=20, font=("times new roman", 15), bg="white")
        self.txt_six.grid(row=8, column=1)

        lbG_carn0 = Label(Frame_one1, text="Safty:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=9, column=0)
        self.txt_seven = Entry(Frame_one1, textvariable=self.safty, width=20, font=("times new roman", 15), bg="white")
        self.txt_seven.grid(row=9, column=1)

        lbH_carn0 = Label(Frame_one1, text="Type:-", font=("Goudy old style", 13, "bold"), fg="green", bg="black").grid(
            row=10, column=0)
        self.txt_eight = Entry(Frame_one1, textvariable=self.type, width=20, font=("times new roman", 15), bg="white")
        self.txt_eight.grid(row=10, column=1)

        lbI_carn0 = Label(Frame_one1, text="Fuel:-", font=("Goudy old style", 13, "bold"), fg="green", bg="black").grid(
            row=11, column=0)
        self.txt_nine = Entry(Frame_one1, textvariable=self.fuel, width=20, font=("times new roman", 15), bg="white")
        self.txt_nine.grid(row=11, column=1)

        lbJ_carn0 = Label(Frame_one1, text="Seats:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=12, column=0)
        self.txt_ten = Entry(Frame_one1, textvariable=self.seat, width=20, font=("times new roman", 15), bg="white")
        self.txt_ten.grid(row=12, column=1)

        lbK_carn0 = Label(Frame_one1, text="Boot Space:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=13, column=0)
        self.txt_eleven = Entry(Frame_one1, textvariable=self.space, width=20, font=("times new roman", 15), bg="white")
        self.txt_eleven.grid(row=13, column=1)

        # frame2
        Frame_two2 = Frame(self.root, bg="black")
        Frame_two2.place(x=410, y=0, height=650, width=400)

        lb1_carn1 = Label(Frame_two2, text="Brand Name:-", font=("Goudy old style", 15, "bold"), fg="red",
                          bg="black").grid(row=0, column=0)
        self.txt_carn1 = Entry(Frame_two2, width=20, font=("times new roman", 15), bg="white")
        self.txt_carn1.grid(row=0, column=1)
        lb2_carb1 = Label(Frame_two2, text="Car Name:-", font=("Goudy old style", 15, "bold"), fg="red",
                          bg="black").grid(
            row=1, column=0)
        self.txt_carb1 = Entry(Frame_two2, width=20, font=("times new roman", 15), bg="white")
        self.txt_carb1.grid(row=1, column=1)

        SEARCHbutton2 = Button(Frame_two2, command=self.fetchone2_function2, text="Search", fg="blue", bg="black",
                               font=("times new roman", 13)).grid(row=2, column=2)

        self.carname1 = StringVar()
        self.brandname1 = StringVar()
        self.cost1 = StringVar()
        self.milage1 = StringVar()
        self.engine1 = StringVar()
        self.speed1 = StringVar()
        self.safty1 = StringVar()
        self.type1 = StringVar()
        self.fuel1 = StringVar()
        self.seat1 = StringVar()
        self.space1 = StringVar()

        lbL_carn0 = Label(Frame_two2, text="Car Name:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=3, column=0)
        self.txt_one = Entry(Frame_two2, textvariable=self.carname1, width=20, font=("times new roman", 15), bg="white")
        self.txt_one.grid(row=3, column=1)

        lbM_carn0 = Label(Frame_two2, text="Brand Name:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=4, column=0)
        self.txt_two = Entry(Frame_two2, textvariable=self.brandname1, width=20, font=("times new roman", 15),
                             bg="white")
        self.txt_two.grid(row=4, column=1)

        lbN_carn0 = Label(Frame_two2, text="Ex.S-Cost:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=5, column=0)
        self.txt_three = Entry(Frame_two2, textvariable=self.cost1, width=20, font=("times new roman", 15), bg="white")
        self.txt_three.grid(row=5, column=1)

        lbO_carn0 = Label(Frame_two2, text="Milage:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=6, column=0)
        self.txt_four = Entry(Frame_two2, textvariable=self.milage1, width=20, font=("times new roman", 15), bg="white")
        self.txt_four.grid(row=6, column=1)

        lbP_carn0 = Label(Frame_two2, text="Engine:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=7, column=0)
        self.txt_five = Entry(Frame_two2, textvariable=self.engine1, width=20, font=("times new roman", 15), bg="white")
        self.txt_five.grid(row=7, column=1)

        lbQ_carn0 = Label(Frame_two2, text="Speed:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=8, column=0)
        self.txt_six = Entry(Frame_two2, textvariable=self.speed1, width=20, font=("times new roman", 15), bg="white")
        self.txt_six.grid(row=8, column=1)

        lbR_carn0 = Label(Frame_two2, text="Safty:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=9, column=0)
        self.txt_seven = Entry(Frame_two2, textvariable=self.safty1, width=20, font=("times new roman", 15), bg="white")
        self.txt_seven.grid(row=9, column=1)

        lbT_carn0 = Label(Frame_two2, text="Type:-", font=("Goudy old style", 13, "bold"), fg="green", bg="black").grid(
            row=10, column=0)
        self.txt_eight = Entry(Frame_two2, textvariable=self.type1, width=20, font=("times new roman", 15), bg="white")
        self.txt_eight.grid(row=10, column=1)

        lbU_carn0 = Label(Frame_two2, text="Fuel:-", font=("Goudy old style", 13, "bold"), fg="green", bg="black").grid(
            row=11, column=0)
        self.txt_nine = Entry(Frame_two2, textvariable=self.fuel1, width=20, font=("times new roman", 15), bg="white")
        self.txt_nine.grid(row=11, column=1)

        lbV_carn0 = Label(Frame_two2, text="Seats:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=12, column=0)
        self.txt_ten = Entry(Frame_two2, textvariable=self.seat1, width=20, font=("times new roman", 15), bg="white")
        self.txt_ten.grid(row=12, column=1)

        lbW_carn0 = Label(Frame_two2, text="Boot Space:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=13, column=0)
        self.txt_eleven = Entry(Frame_two2, textvariable=self.space1, width=20, font=("times new roman", 15),
                                bg="white")
        self.txt_eleven.grid(row=13, column=1)

        # frame3
        Frame_three3 = Frame(self.root, bg="black")
        Frame_three3.place(x=820, y=0, height=650, width=400)

        lb1_carn2 = Label(Frame_three3, text="Brand Name:-", font=("Goudy old style", 15, "bold"), fg="red",
                          bg="black").grid(row=0, column=0)
        self.txt_carn2 = Entry(Frame_three3, width=20, font=("times new roman", 15), bg="white")
        self.txt_carn2.grid(row=0, column=1)
        lb2_carb2 = Label(Frame_three3, text="Car Name:-", font=("Goudy old style", 15, "bold"), fg="red",
                          bg="black").grid(
            row=1, column=0)
        self.txt_carb2 = Entry(Frame_three3, width=20, font=("times new roman", 15), bg="white")
        self.txt_carb2.grid(row=1, column=1)

        SEARCHbutton3 = Button(Frame_three3, command=self.fetchone3_function3, text="Search", fg="blue", bg="black",
                               font=("times new roman", 13)).grid(row=2, column=2)

        self.carname3 = StringVar()
        self.brandname3 = StringVar()
        self.cost3 = StringVar()
        self.milage3 = StringVar()
        self.engine3 = StringVar()
        self.speed3 = StringVar()
        self.safty3 = StringVar()
        self.type3 = StringVar()
        self.fuel3 = StringVar()
        self.seat3 = StringVar()
        self.space3 = StringVar()

        lba_carn0 = Label(Frame_three3, text="Car Name:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=3, column=0)
        self.txt_one = Entry(Frame_three3, textvariable=self.carname3, width=20, font=("times new roman", 15),
                             bg="white")
        self.txt_one.grid(row=3, column=1)

        lbb_carn0 = Label(Frame_three3, text="Brand Name:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=4, column=0)
        self.txt_two = Entry(Frame_three3, textvariable=self.brandname3, width=20, font=("times new roman", 15),
                             bg="white")
        self.txt_two.grid(row=4, column=1)

        lbc_carn0 = Label(Frame_three3, text="Ex.S-Cost:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=5, column=0)
        self.txt_three = Entry(Frame_three3, textvariable=self.cost3, width=20, font=("times new roman", 15),
                               bg="white")
        self.txt_three.grid(row=5, column=1)

        lbd_carn0 = Label(Frame_three3, text="Milage:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=6, column=0)
        self.txt_four = Entry(Frame_three3, textvariable=self.milage3, width=20, font=("times new roman", 15),
                              bg="white")
        self.txt_four.grid(row=6, column=1)

        lbe_carn0 = Label(Frame_three3, text="Engine:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=7, column=0)
        self.txt_five = Entry(Frame_three3, textvariable=self.engine3, width=20, font=("times new roman", 15),
                              bg="white")
        self.txt_five.grid(row=7, column=1)

        lbf_carn0 = Label(Frame_three3, text="Speed:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=8, column=0)
        self.txt_six = Entry(Frame_three3, textvariable=self.speed3, width=20, font=("times new roman", 15), bg="white")
        self.txt_six.grid(row=8, column=1)

        lbg_carn0 = Label(Frame_three3, text="Safty:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=9, column=0)
        self.txt_seven = Entry(Frame_three3, textvariable=self.safty3, width=20, font=("times new roman", 15),
                               bg="white")
        self.txt_seven.grid(row=9, column=1)

        lbh_carn0 = Label(Frame_three3, text="Type:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=10, column=0)
        self.txt_eight = Entry(Frame_three3, textvariable=self.type3, width=20, font=("times new roman", 15),
                               bg="white")
        self.txt_eight.grid(row=10, column=1)

        lbi_carn0 = Label(Frame_three3, text="Fuel:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=11, column=0)
        self.txt_nine = Entry(Frame_three3, textvariable=self.fuel3, width=20, font=("times new roman", 15), bg="white")
        self.txt_nine.grid(row=11, column=1)

        lbj_carn0 = Label(Frame_three3, text="Seats:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=12, column=0)
        self.txt_ten = Entry(Frame_three3, textvariable=self.seat3, width=20, font=("times new roman", 15), bg="white")
        self.txt_ten.grid(row=12, column=1)

        lbk_carn0 = Label(Frame_three3, text="Boot Space:-", font=("Goudy old style", 13, "bold"), fg="green",
                          bg="black").grid(row=13, column=0)
        self.txt_eleven = Entry(Frame_three3, textvariable=self.space3, width=20, font=("times new roman", 15),
                                bg="white")
        self.txt_eleven.grid(row=13, column=1)


        # for loading retrived image stored as blob in new frames->
        self.Frame_image1 = Frame(Frame_one1, bg="white")
        self.Frame_image1.place(x=50, y=400, height=200, width=310)

        self.Frame_image2 = Frame(Frame_two2, bg="white")
        self.Frame_image2.place(x=50, y=400, height=200, width=310)

        self.Frame_image3 = Frame(Frame_three3, bg="white")
        self.Frame_image3.place(x=50, y=400, height=200, width=310)

        # frame4
        con = pymysql.connect(host="localhost", user="root", password="root", database="roy")
        cur = con.cursor()
        cur.execute("SELECT * FROM detailss ")
        
        Frame_four4 = Frame(self.root, bg="black")
        Frame_four4.place(x=1220, y=0, height=550, width=300)
        self.carname4 = StringVar()
        self.brandname4 = StringVar()
        self.cost4 = StringVar()

        col = ('carname4','brandname4','cost4')
        Treeview = ttk.Treeview(Frame_four4,height=650,show='headings',columns=col)
        Treeview.column('carname4',width=38,anchor ='sw')
        Treeview.column('brandname4',width=38,anchor ='sw')
        Treeview.column('cost4',width=74,anchor ='sw')   
        Treeview.heading('carname4',text='Car')
        Treeview.heading('brandname4',text='Brand')
        Treeview.heading('cost4',text='Cost')        
        Treeview.pack(side=TOP,fill=BOTH)

        i=0
        for ro in cur:
            Treeview.insert('',END,values=(ro[0],ro[1],ro[2]))
     
     #frame5
        Frame_FIVE5 = Frame(self.root, bg="black")
        Frame_FIVE5.place(x=1220, y=550, height=100, width=300)

        back = Button(Frame_FIVE5, text="  Logout  ", command=self.back_functioN, fg="RED", bg="KHAKI",
                      font=("times new roman", 20)).grid(row=0,column=0)
        about = Button(Frame_FIVE5, text="          ?          ", command=self.about_functioN, fg="RED", bg="KHAKI",
                      font=("times new roman", 20)).grid(row=0,column=1)


    def fetchone1_function1(self):
        if self.txt_carb0.get() == "" or self.txt_carn0.get() == "":
            messagebox.showerror("error", "all fields are required", parent=self.root)
        else:
            con = pymysql.connect(host="localhost", user="root", password="root", database="roy")
            cur = con.cursor()
            cur.execute("SELECT * FROM detailss WHERE name=%s and brand=%s",
                        (self.txt_carb0.get(), self.txt_carn0.get()))
            rows = cur.fetchone()
            if rows != None:
                self.carname.set(rows[0])
                self.brandname.set(rows[1])
                self.cost.set(rows[2])
                self.milage.set(rows[3])
                self.engine.set(rows[4])
                self.speed.set(rows[5])
                self.safty.set(rows[6])
                self.type.set(rows[7])
                self.fuel.set(rows[8])
                self.seat.set(rows[9])
                self.space.set(rows[10])
                BLOBimage = rows[11]
                self.make_image(r"D:\sr turbo\car1.jpg", BLOBimage)
                self.ph1 = ImageTk.PhotoImage(Image.open(r"D:\sr turbo\car1.jpg"))
                self.ph1_photo = Label(self.Frame_image1, image=self.ph1).grid(row=0, column=0)


            else:
                messagebox.showerror("error", " Not found!", parent=self.root)

    def make_image(self, path, blob):
        self.write_file(blob, path)

    def write_file(self ,data, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, "wb") as fh:
            fh.write(base64.decodebytes(data))

    def fetchone2_function2(self):
        if self.txt_carb1.get() == "" or self.txt_carn1.get() == "":
            messagebox.showerror("error", "all fields are required", parent=self.root)
        else:
            con = pymysql.connect(host="localhost", user="root", password="root", database="roy")
            cur = con.cursor()
            cur.execute("SELECT * FROM detailss WHERE name=%s and brand=%s",
                        (self.txt_carb1.get(), self.txt_carn1.get()))
            rows = cur.fetchone()
            if rows != None:
                self.carname1.set(rows[0])
                self.brandname1.set(rows[1])
                self.cost1.set(rows[2])
                self.milage1.set(rows[3])
                self.engine1.set(rows[4])
                self.speed1.set(rows[5])
                self.safty1.set(rows[6])
                self.type1.set(rows[7])
                self.fuel1.set(rows[8])
                self.seat1.set(rows[9])
                self.space1.set(rows[10])
                BLOBimage = rows[11]
                self.make_image(r"D:\sr turbo\car2.jpg", BLOBimage)
                self.ph2 = ImageTk.PhotoImage(Image.open(r"D:\sr turbo\car2.jpg"))
                self.ph2_photo = Label(self.Frame_image2, image=self.ph2).grid(row=0, column=0)



            else:
                messagebox.showerror("error", " Not found!", parent=self.root)

    def fetchone3_function3(self):
        if self.txt_carb2.get() == "" or self.txt_carn2.get() == "":
            messagebox.showerror("error", "all fields are required", parent=self.root)
        else:
            con = pymysql.connect(host="localhost", user="root", password="root", database="roy")
            cur = con.cursor()
            cur.execute("SELECT * FROM detailss WHERE name=%s and brand=%s",
                        (self.txt_carb2.get(), self.txt_carn2.get()))
            rows = cur.fetchone()
            if rows != None:
                self.carname3.set(rows[0])
                self.brandname3.set(rows[1])
                self.cost3.set(rows[2])
                self.milage3.set(rows[3])
                self.engine3.set(rows[4])
                self.speed3.set(rows[5])
                self.safty3.set(rows[6])
                self.type3.set(rows[7])
                self.fuel3.set(rows[8])
                self.seat3.set(rows[9])
                self.space3.set(rows[10])
                BLOBimage = rows[11]
                self.make_image(r"D:\sr turbo\car3.jpg", BLOBimage)
                self.ph3 = ImageTk.PhotoImage(Image.open(r"D:\sr turbo\car3.jpg"))
                self.ph3_photo = Label(self.Frame_image3, image=self.ph3).grid(row=0, column=0)


            else:
                messagebox.showerror("error", " Not found!", parent=self.root)

    def back_functioN(self):
        self.root.destroy()
        import roy

    def about_functioN(self):
        import roy5


root = Tk()
obj = User_home(root)
root.mainloop()
