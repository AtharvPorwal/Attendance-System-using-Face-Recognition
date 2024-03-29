from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import csv
import cv2
from time import strftime
from datetime import  datetime
from tkinter import filedialog

mydata=[]
class attendance_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Manage Attendance")

#============= VARIABLES 
        self.var_attendance_id=StringVar()
        self.var_roll_no=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance_status=StringVar()


        #IMAGE 1
        img = Image.open(r"images\facialrecognition.png")
        img = img.resize((800, 200), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        # Store the PhotoImage in an instance variable
        self.photoimg = ImageTk.PhotoImage(img)
        label = Label(self.root, image=self.photoimg)
        label.place(x=0,y=0,width=800,height=200)



        #IMAGE 2
        img2 = Image.open(r"images\facialrecognition.png")
        img2 = img2.resize((800, 200), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS      
        # Store the PhotoImage in an instance variable
        self.photoimg2 = ImageTk.PhotoImage(img2)
        label = Label(self.root, image=self.photoimg2)
        label.place(x=800,y=0,width=800,height=200)



#BG IMAGE
        img4 = Image.open(r"images\bg1.jpg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        # Store the PhotoImage in an instance variable
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0,y=200,width=1530,height=710)

# APPLICATION TITLE
        title_lbl = Label (bg_img,text="Attendance Management System",font=('Helvetica', 26),bg="White",fg="red",)
        title_lbl.place(x=0,y=0,width=1530,height=50)


# Main Frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=25,y=55,width=1480,height=600)

#left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman" ,12, "bold"))
        Left_frame.place(x=20,y=10,width=700,height=580)


        #Left LABEL IMAGE
        img_left = Image.open(r"images\face-recognition.png")
        img_left = img_left.resize((600, 130), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        # Store the PhotoImage in an instance variable
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        label = Label(Left_frame, image=self.photoimg_left)
        label.place(x=40,y=10,width=600,height=130)

        #Frame Inside LEFT FRAME
        Left_inside_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE)
        Left_inside_frame.place(x=5,y=135,width=686,height=445)


        #Labels and Entry 

        #Attendance ID
        attendance_id_label =Label(Left_inside_frame,text="Attendance Id :",font=("times new roman" ,12, "bold"),bg="white")
        attendance_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendance_id_entry =Entry(Left_inside_frame,textvariable=self.var_attendance_id,width=20,font=("times new roman" ,12, "bold"))
        attendance_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll No 
        stu_rollno_label =Label(Left_inside_frame,text="Roll No:",font=("times new roman" ,12, "bold"),bg="white")
        stu_rollno_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        stu_rollno_entry = Entry(Left_inside_frame,textvariable=self.var_roll_no,width=20,font=("times new roman" ,12, "bold"))
        stu_rollno_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Name
        stu_name_label =Label(Left_inside_frame,text="Name :",font=("times new roman" ,12, "bold"),bg="white")
        stu_name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        stu_name_entry = Entry(Left_inside_frame,textvariable=self.var_name,width=20,font=("times new roman" ,12, "bold"))
        stu_name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Department
        stu_dep_label =Label(Left_inside_frame,text="Department :",font=("times new roman" ,12, "bold"),bg="white")
        stu_dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        stu_dep_entry = Entry(Left_inside_frame,textvariable=self.var_department,width=20,font=("times new roman" ,12, "bold"))
        stu_dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Time
        stu_time_label =Label(Left_inside_frame,text="Time :",font=("times new roman" ,12, "bold"),bg="white")
        stu_time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        stu_time_entry = Entry(Left_inside_frame,textvariable=self.var_time,width=20,font=("times new roman" ,12, "bold"))
        stu_time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date
        stu_date_label =Label(Left_inside_frame,text="Date :",font=("times new roman" ,12, "bold"),bg="white")
        stu_date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        stu_date_entry = Entry(Left_inside_frame,textvariable=self.var_date,width=20,font=("times new roman" ,12, "bold"))
        stu_date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Attendance Status
        stu_status_label =Label(Left_inside_frame,text="Attendance ",font=("times new roman" ,12, "bold"),bg="white")
        stu_status_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        stu_div_combo=ttk.Combobox(Left_inside_frame,textvariable=self.var_attendance_status,font=("times new roman" ,12, "bold"),width=17,state="readonly")
        stu_div_combo['values']=("Status","Present","Absent")
        stu_div_combo.current(0)
        stu_div_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)





#button Frame
        btn_frame = Frame(Left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300, width=680, height=40)


        save_btn = Button(btn_frame,text="Import csv",width=18,command=self.import_csv,font=("times new roman" ,12, "bold"),bg="blue",fg="White")
        save_btn.grid(row=0,column=1,)

        update_btn = Button(btn_frame,text="Export csv",command=self.exprt_csv,width=18,font=("times new roman" ,12, "bold"),bg="blue",fg="White")
        update_btn.grid(row=0,column=2,)

        delete_btn = Button(btn_frame,text="Update",width=18,font=("times new roman" ,12, "bold"),bg="blue",fg="White")
        delete_btn.grid(row=0,column=3,)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman" ,12, "bold"),bg="blue",fg="White")
        reset_btn.grid(row=0,column=4,)





#Right label frame
        
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman" ,12, "bold"))
        Right_frame.place(x=750,y=10,width=700,height=580)

        # table frame
        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5, width=680, height=440)

        #scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


        #FETCH DATA

    def  fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
             self.AttendanceReportTable.insert("",END,values=i)
#++++++++++++ IMPORT CSV
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
             csvread=csv.reader(myfile,delimiter=",")
             for i in csvread:
                  mydata.append(i)
             self.fetchData(mydata) 

#++++++++++++++++ExPORT CSV++++++++++++++
    def exprt_csv(self):
        try:
             if len(mydata)<1:
                  messagebox.showerror("No Data","No Data Found",parent=self.root)
                  return False
             fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
             with open(fln,mode="w",newline="") as myfile:
                  exp_write=csv.writer(myfile,delimiter=",")
                  for i in mydata:
                       exp_write.writerow(i)
                  messagebox.showinfo("Data Export","Your Data has been Exported to" +os.path.basename(fln)+"Successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)   





#==========================Fuction to Retreive Data
                
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attendance_id.set(rows[0])
        self.var_roll_no.set(rows[1])
        self.var_name.set(rows[2])
        self.var_department.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance_status.set(rows[6])




#==========================Fuction to Clear Data Cells
                
    def reset_data(self):
        self.var_attendance_id.set("")
        self.var_roll_no.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance_status.set("")





        if __name__ == "__main__":
                root = Tk()
                obj = attendance_system(root)
                root.mainloop()