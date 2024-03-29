from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_classifier import Face_classifier
from attendance import attendance_system
from developer import Developer
from datetime import datetime
import tkinter
import os
from time import strftime
from helpdesk import help_desk
class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        # Add a method to initialize the GUI components
        self.initialize_gui()

    def initialize_gui(self):

#IMAGE 1
        img = Image.open(r"images\facialrecognition.png")
        img = img.resize((500, 130), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        # Store the PhotoImage in an instance variable
        self.photoimg = ImageTk.PhotoImage(img)
        label = Label(self.root, image=self.photoimg)
        label.place(x=0,y=0,width=500,height=130)
#IMAGE 2
        img2 = Image.open(r"images\facialrecognition.png")
        img2 = img2.resize((500, 130), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        # Store the PhotoImage in an instance variable
        self.photoimg2 = ImageTk.PhotoImage(img2)
        label = Label(self.root, image=self.photoimg2)
        label.place(x=500,y=0,width=500,height=130)
#IMAGE 3
        img3 = Image.open(r"images\facialrecognition.png")
        img3 = img3.resize((500, 130), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        # Store the PhotoImage in an instance variable
        self.photoimg3 = ImageTk.PhotoImage(img3)
        label = Label(self.root, image=self.photoimg3)
        label.place(x=1000,y=0,width=500,height=130)
#BG IMAGE
        img4 = Image.open(r"images\bg1.jpg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        # Store the PhotoImage in an instance variable
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)


# APPLICATION TITLE
        title_lbl = Label (bg_img,text="FACE RECOGNISTION ATTENDANCE SYSTEM ",font=('Helvetica', 26),bg="White",fg="red",)
        title_lbl.place(x=0,y=0,width=1530,height=50)


#CURRENT TIME DISPLAY
        def time():
                string= strftime('%H:%M:%S %p')
                lbl.config( text = string )
                lbl.after(1000, time)

        lbl = Label(title_lbl,font =('times new roman',14,'bold'),background= 'white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()


# STUDENT BUTTON 
        img5 = Image.open(r"images\gettyimages-1022573162.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details, cursor="hand2")
        b1.place(x=100,y=90,width=220,height=220) # Change X & Y to change the postion of the button

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=('Helvetica', 24),bg="White",fg="red") # TEXT DETAILS
        b1_1.place(x=100,y=290,width=220,height=50)


# FACE DETECT BUTTON
        img6 = Image.open(r"images\face_classifier_.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.face_data, cursor="hand2")
        b1.place(x=400,y=90,width=220,height=220) # Change X & Y to change the postion of the button

        b1_1=Button(bg_img,text="FACE DETECT",command=self.face_data,cursor="hand2",font=('Helvetica', 24),bg="White",fg="red") # TEXT DETAILS
        b1_1.place(x=400,y=290,width=220,height=50)


# ATTENDANCE
        img7 = Image.open(r"images\attendance_btn.png")
        img7 = img7.resize((220, 220), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.attendance, cursor="hand2")
        b1.place(x=700,y=90,width=220,height=220) # Change X & Y to change the postion of the button

        b1_1=Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attendance,font=('Helvetica', 24),bg="White",fg="red") # TEXT DETAILS
        b1_1.place(x=700,y=290,width=220,height=50)


# HELP DESK 
        img8 = Image.open(r"images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.help, cursor="hand2")
        b1.place(x=1000,y=90,width=220,height=220) # Change X & Y to change the postion of the button

        b1_1=Button(bg_img,text="HELP DESK",command=self.help,cursor="hand2",font=('Helvetica', 24),bg="White",fg="red") # TEXT DETAILS
        b1_1.place(x=1000,y=290,width=220,height=50)


#TRAIN DATA
        img9 = Image.open(r"images\di.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.train_data, cursor="hand2")
        b1.place(x=100,y=390,width=220,height=220) # Change X & Y to change the postion of the button

        b1_1=Button(bg_img,text="TRAIN DATA",command=self.train_data,cursor="hand2",font=('Helvetica', 24),bg="White",fg="red") # TEXT DETAILS
        b1_1.place(x=100,y=610,width=220,height=50)

#PHoTOS
        img10 = Image.open(r"images\opencv_face_reco_more_data.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,command=self.open_img,cursor="hand2")
        b1.place(x=400,y=390,width=220,height=220) # Change X & Y to change the postion of the button

        b1_1=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=('Helvetica', 24),bg="White",fg="red") # TEXT DETAILS
        b1_1.place(x=400,y=610,width=220,height=50)

#DEVELOPERS
        img11 = Image.open(r"images\devo.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,command=self.dev, cursor="hand2")
        b1.place(x=700,y=390,width=220,height=220) # Change X & Y to change the postion of the button

        b1_1=Button(bg_img,text="DEVELOPERS",cursor="hand2",command=self.dev,font=('Helvetica', 24),bg="White",fg="red") # TEXT DETAILS
        b1_1.place(x=700,y=610,width=220,height=50)


        #EXIT
        img12 = Image.open(r"images\exit.jpg")
        img12 = img12.resize((220, 220), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,command=self.iExit, cursor="hand2")
        b1.place(x=1000,y=390,width=220,height=220) # Change X & Y to change the postion of the button

        b1_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=('Helvetica', 24),bg="White",fg="red") # TEXT DETAILS
        b1_1.place(x=1000,y=610,width=220,height=50)    


# Function to open Images Folder
    def open_img(self):
         os.startfile("data")

#Function to Close Program
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Program","Are you sure",parent=self.root)
        if self.iExit >0:
                self.root.destroy()
        else:
                return

#Fuction For Student Details section to open
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)



#Fuction For Train Data section to open
        
    def train_data (self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


#Fuction For Face Classifier section to open
        
    def face_data (self):
        self.new_window=Toplevel(self.root)
        self.app=Face_classifier(self.new_window)


#Fuction For Attendance section to open
        
    def attendance (self):
        self.new_window=Toplevel(self.root)
        self.app=attendance_system(self.new_window)

#Fuction For Developer section to open
        
    def dev (self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

#Fuction For Helpdesk section to open
        
    def help (self):
        self.new_window=Toplevel(self.root)
        self.app=help_desk(self.new_window)



if __name__ == "__main__":
        root = Tk()
        obj = Face_Recognition_System(root)
        root.mainloop()
