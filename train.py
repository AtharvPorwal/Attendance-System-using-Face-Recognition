from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import numpy as np
import cv2

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Train Data")


        # APPLICATION TITLE
        title_lbl = Label (self.root,text="Train Data ",font=('Helvetica', 26),bg="Blue",fg="red",)
        title_lbl.place(x=0,y=0,width=1530,height=50)

        #TOP LABEL IMAGE
        img_top = Image.open(r"images\facialrecognition.png")
        img_top = img_top.resize((1550,350), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        # Store the PhotoImage in an instance variable
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        label = Label(self.root,image=self.photoimg_top)
        label.place(x=0,y=50,width=1530,height=280)

# Button 
        b1_1=Button(self.root,text="Model Train",command=self.train_classifier,cursor="hand2",font=('Helvetica', 24),bg="White",fg="red") # TEXT DETAILS
        b1_1.place(x=0,y=350,width=1530,height=50)


        #BOTTOM LABEL IMAGE
        img_bottom = Image.open(r"images\facialrecognition.png")
        img_bottom = img_bottom.resize((1550,350), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        # Store the PhotoImage in an instance variable
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        label = Label(self.root,image=self.photoimg_bottom)
        label.place(x=0,y=430,width=1530,height=280)



    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for  image in path:
            img=Image.open(image).convert('L')  #GrayScale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training on",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)



#================Training Model and Saving data 
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Model Training Successful!")
            #D:\Projects\face regconistion attandence\data\user.1.1.jpg





        if __name__ == "__main__":
                root = Tk()
                obj = Train(root)
                root.mainloop()