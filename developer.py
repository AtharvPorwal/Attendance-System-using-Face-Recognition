from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_classifier import Face_classifier
from attendance import attendance_system
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Developer")
    


        # APPLICATION TITLE
        title_lbl = Label (self.root,text="Developers",font=('Helvetica', 26),bg="Blue",fg="red",)
        title_lbl.place(x=0,y=0,width=1530,height=50)

        #TOP LABEL IMAGE
        img_top = Image.open(r"images\facialrecognition.png")
        img_top = img_top.resize((1550,350), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        # Store the PhotoImage in an instance variable
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        label = Label(self.root,image=self.photoimg_top)
        label.place(x=0,y=50,width=1530,height=280)






if __name__ == "__main__":
        root = Tk()
        obj = Developer(root)
        root.mainloop()