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
class yoyo:
    def __init__(self, root):
        self.root = root
        self.root.title('SR_TURBO_')
        self.root.geometry("683x61+0+0")
        self.root.resizable(False, False)

        notice = Label(self.root, text="Confused in buying a new car, then contact us for getting best opinion.", font=("Goudy old style", 15, "bold"), fg="blue1",bg="khaki").grid(row=0, column=0)
        notice1 = Label(self.root, text=" Whatsapp us at 8369877897 ", font=("Goudy old style", 15, "bold"), fg="black",bg="green1").grid(row=1, column=0)
root = Tk()
obj = yoyo(root)
root.mainloop()
