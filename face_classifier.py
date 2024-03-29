from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2
from time import strftime
from datetime import  datetime

class Face_classifier:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Classifier")

        # APPLICATION TITLE
        title_lbl = Label (self.root,text=" Face Recognition ",font=('Helvetica', 26),bg="Blue",fg="red",)
        title_lbl.place(x=0,y=0,width=1530,height=50)


        #LEFT  IMAGE
        img_top = Image.open(r"images\face_classifier_.jpg")
        img_top = img_top.resize((650,735), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        # Store the PhotoImage in an instance variable
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        label = Label(self.root,image=self.photoimg_top)
        label.place(x=0,y=50,width=650,height=735)




        #RIGHT IMAGE
        img_bottom = Image.open(r"images\face_classifier.jpg")
        img_bottom = img_bottom.resize((950,735), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        # Store the PhotoImage in an instance variable
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        label = Label(self.root,image=self.photoimg_bottom)
        label.place(x=650,y=50,width=950,height=735)

# Button 
        b1_1=Button(label,text="Face Recognition",command=self.face_recog,cursor="hand2",font=('Helvetica', 16),bg="White",fg="red") # TEXT DETAILS
        b1_1.place(x=370,y=650,width=200,height=40)






# Attendance MArks

    def mark_attendance(self,i,r,n,d):
        with open("sheet.csv", "r+" ,newline="\n" ) as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList: 
                entry=line.split((","))
                name_list.append(entry[0])

            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ):
                print("At least one ID already exists in the file. Skipping...")
                now =datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


# Function of this page


    def face_recog(self):
        def draw_border(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coordinates= []
            for (x,y,w,h) in features:
                cv2.rectangle(img,  (x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+h])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
                my_cursor =conn.cursor()

                my_cursor.execute("select name from Student where studentid="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)


                my_cursor.execute("select roll from Student where studentid="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)


                my_cursor.execute("select dep from Student where studentid="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select studentid from Student where studentid="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)



                if confidence>90:
                    cv2.putText(img,f"ID ::{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll No:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coordinates =[x,y,w,h]
            return coordinates
        
        def recognize(img,clf,faceCascade):
            Coordinates = draw_border(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videocap=cv2.VideoCapture(0)

        while True:
            ret,img=videocap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome TO system",img)
            if cv2.waitKey(50)==13:
                break
        videocap.release()
        cv2.destroyAllWindows()








        if __name__ == "__main__":
                root = Tk()
                obj = Face_classifier(root)
                root.mainloop()
