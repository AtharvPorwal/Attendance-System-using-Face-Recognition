from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_classifier import Face_classifier
from attendance import attendance_system
from developer import Developer
import tkinter
import os

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")




if __name__ == "__main__":
        root = Tk()
        obj = Face_Recognition_System(root)
        root.mainloop()
