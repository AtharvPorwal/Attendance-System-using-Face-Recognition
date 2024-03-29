from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import time

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student")


        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_stu_id=StringVar()
        self.var_stu_name=StringVar()
        self.var_stu_div=StringVar()
        self.var_stu_rollno=StringVar()
        self.var_stu_gender=StringVar()
        self.var_stu_dob=StringVar()
        self.var_stu_email=StringVar()
        self.var_stu_phn=StringVar()
        self.var_stu_address=StringVar()
        self.var_stu_mentor=StringVar()
        self.var_radio1=StringVar()



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
        title_lbl = Label (bg_img,text="Student Management System",font=('Helvetica', 26),bg="White",fg="red",)
        title_lbl.place(x=0,y=0,width=1530,height=50)
# Main Frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1515,height=600)

#left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman" ,12, "bold"))
        Left_frame.place(x=10,y=10,width=720,height=580)

        #Left LABEL IMAGE
        img_left = Image.open(r"images\facialrecognition.png")
        img_left = img_left.resize((500, 130), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        # Store the PhotoImage in an instance variable
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        label = Label(Left_frame, image=self.photoimg_left)
        label.place(x=5,y=10,width=500,height=130)

        #Current Frame 
        Current_left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Details",font=("times new roman" ,12, "bold"))
        Current_left_frame.place(x=10,y=175,width=720,height=120)

        #departmencourse
        dep_label=Label(Current_left_frame,text="Department",font=("times new roman" ,12, "bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)
        dep_combo=ttk.Combobox(Current_left_frame,textvariable=self.var_dep,font=("times new roman" ,12, "bold"),width=17,state="readonly")
        dep_combo['values']=("Select Department","CSE","CIVIL","MECHANICAL",'ECE','EEE')
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(Current_left_frame,text="Course",font=("times new roman" ,12, "bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo=ttk.Combobox(Current_left_frame,textvariable=self.var_course,font=("times new roman" ,12, "bold"),width=17,state="readonly")
        course_combo['values']=("Select Course","C1","C2","C3",'C4','c5')
        course_combo.current(0)
        course_combo.grid(row=0, column=3,padx=2,pady=10,sticky=W)

#Year
        year_label=Label(Current_left_frame,text="Year",font=("times new roman" ,12, "bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(Current_left_frame,textvariable=self.var_year,font=("times new roman" ,12, "bold"),width=17,state="readonly")
        year_combo['values']=("Select Year","1st Year","2nd Year","3rd Year",'4th Year','5th Year')
        year_combo.current(0)
        year_combo.grid(row=1, column=1,padx=2,pady=10,sticky=W)

        #Semester
        sem_label=Label(Current_left_frame,text="Semester",font=("times new roman" ,12, "bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)
        sem_combo=ttk.Combobox(Current_left_frame,textvariable=self.var_sem,font=("times new roman" ,12, "bold"),width=17,state="readonly")
        sem_combo['values']=("Select Semester","Semester 1","Semester 2","Semester 3",'Semester 4','Semester 5','Semester 6','Semester 7','Semester 8','Semester 9','Semester 10')
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3,padx=2,pady=10,sticky=W)


#Student Class ID FRAME
        class_stu_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Details",font=("times new roman" ,12, "bold"))
        class_stu_frame.place(x=10,y=280,width=720,height=330)


        #Student ID Input
        stu_id_label =Label(class_stu_frame,text="StudentID:",font=("times new roman" ,12, "bold"),bg="white")
        stu_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        stu_id_entry =Entry(class_stu_frame,textvariable=self.var_stu_id,width=20,font=("times new roman" ,12, "bold"))
        stu_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #Student NAME Input
        stu_name_label =Label(class_stu_frame,text="Student Name:",font=("times new roman" ,12, "bold"),bg="white")
        stu_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        stu_name_entry =Entry(class_stu_frame,textvariable=self.var_stu_name,width=20,font=("times new roman" ,12, "bold"))
        stu_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #Student CLASS DIVISION Input
        stu_div_label =Label(class_stu_frame,text="Class Division",font=("times new roman" ,12, "bold"),bg="white")
        stu_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        #stu_div_entry = Entry(class_stu_frame,textvariable=self.var_stu_div,width=20,font=("times new roman" ,12, "bold"))
        #stu_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        stu_div_combo=ttk.Combobox(class_stu_frame,textvariable=self.var_stu_div,font=("times new roman" ,12, "bold"),width=17,state="readonly")
        stu_div_combo['values']=("Select Divison ","A","B","C")
        stu_div_combo.current(0)
        stu_div_combo.grid(row=1, column=1,padx=10,pady=5,sticky=W)


        #Student Roll No Input
        stu_rollno_label =Label(class_stu_frame,text="Roll No",font=("times new roman" ,12, "bold"),bg="white")
        stu_rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        stu_rollno_entry = Entry(class_stu_frame,textvariable=self.var_stu_rollno,width=20,font=("times new roman" ,12, "bold"))
        stu_rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #Student Gender Input
        stu_gender_label =Label(class_stu_frame,text="Gender",font=("times new roman" ,12, "bold"),bg="white")
        stu_gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        stu_gender_combo=ttk.Combobox(class_stu_frame,textvariable=self.var_stu_gender,font=("times new roman" ,12, "bold"),width=17,state="readonly")
        stu_gender_combo['values']=("Select Gender","Male","Female","Others")
        stu_gender_combo.current(0)
        stu_gender_combo.grid(row=2, column=1,padx=10,pady=5,sticky=W)


        #Student Date Of Birth Input
        stu_dob_label =Label(class_stu_frame,text="Date Of Birth",font=("times new roman" ,12, "bold"),bg="white")
        stu_dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        stu_dob_entry = Entry(class_stu_frame,textvariable=self.var_stu_dob,width=20,font=("times new roman" ,12, "bold"))
        stu_dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        # Student Email Input
        stu_email_label =Label(class_stu_frame,text="Email",font=("times new roman" ,12, "bold"),bg="white")
        stu_email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        stu_email_entry = Entry(class_stu_frame,textvariable=self.var_stu_email,width=20,font=("times new roman" ,12, "bold"))
        stu_email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        # Student Phone No Input
        stu_phn_label =Label(class_stu_frame,text="Phone No:",font=("times new roman" ,12, "bold"),bg="white")
        stu_phn_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        stu_phn_entry = Entry(class_stu_frame,textvariable=self.var_stu_phn,width=20,font=("times new roman" ,12, "bold"))
        stu_phn_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        # Student Address Input
        stu_address_label =Label(class_stu_frame,text="Address:",font=("times new roman" ,12, "bold"),bg="white")
        stu_address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        stu_address_entry = Entry(class_stu_frame,textvariable=self.var_stu_address,width=20,font=("times new roman" ,12, "bold"))
        stu_address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        # Student Mentor Input
        stu_mentor_label =Label(class_stu_frame,text="Mentor Name:",font=("times new roman" ,12, "bold"),bg="white")
        stu_mentor_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        stu_mentor_entry = Entry(class_stu_frame,textvariable=self.var_stu_mentor,width=20,font=("times new roman" ,12, "bold"))
        stu_mentor_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)



#radio_Button
        
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_stu_frame,text="Take Sample Photo",variable=self.var_radio1,value="yes")
        radiobtn1.grid(row=6,column=0)

        self.var_radio1=StringVar()     
        radiobtn1 = ttk.Radiobutton(class_stu_frame,text="No Sample Photo",variable=self.var_radio1,value="No")
        radiobtn1.grid(row=6,column=1)

#button Frame
        btn_frame = Frame(class_stu_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200, width=718, height=40)


        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman" ,12, "bold"),bg="blue",fg="White")
        save_btn.grid(row=0,column=1,)

        update_btn = Button(btn_frame,text="Update",command=self.Update_data,width=19,font=("times new roman" ,12, "bold"),bg="blue",fg="White")
        update_btn.grid(row=0,column=2,)

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=19,font=("times new roman" ,12, "bold"),bg="blue",fg="White")
        delete_btn.grid(row=0,column=3,)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman" ,12, "bold"),bg="blue",fg="White")
        reset_btn.grid(row=0,column=4,)

#button Frame DownSide
        btn_frame1 = Frame(class_stu_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=250, width=718, height=40)

        take_btn = Button(btn_frame1,text="Take Sample Photo",command=self.genrate_dataset,width=40,font=("times new roman" ,12, "bold"),bg="blue",fg="White")
        take_btn.grid(row=0,column=1,)

        update_img_btn = Button(btn_frame1,text="Update Sample Photo",width=40,font=("times new roman" ,12, "bold"),bg="blue",fg="White")
        update_img_btn.grid(row=0,column=2,)


#Right label frame
        
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman" ,12, "bold"))
        Right_frame.place(x=760,y=10,width=720,height=580)


        #Right Image Frame
        img_right = Image.open(r"D:\Projects\face regconistion attandence\images\facialrecognition.png") #Change Image
        img_right = img_right.resize((500, 130), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        # Store the PhotoImage in an instance variable
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        label1 = Label(Right_frame, image=self.photoimg_right)
        label1.place(x=5,y=10,width=500,height=130)

# Search System
        # Search Frame

        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman" ,12, "bold"))
        search_frame.place(x=0,y=150,width=718,height=50)

#search Lable 
        
        search_label =Label(search_frame,text="Search By:",font=("times new roman" ,12, "bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman" ,12, "bold"),width=17,state="readonly")
        search_combo['values']=("Select ","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(search_frame,width=20,font=("times new roman" ,12, "bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        seach_btn = Button(search_frame,text="Search",width=12,font=("times new roman" ,12, "bold"),bg="blue",fg="White")
        seach_btn.grid(row=0,column=3,padx=4)

        showall_btn = Button(search_frame,text="Show All",width=12,font=("times new roman" ,12, "bold"),bg="blue",fg="White")
        showall_btn.grid(row=0,column=4,padx=4)


# Table Frame

        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman" ,12, "bold"))
        table_frame.place(x=0,y=200,width=718,height=355)

        scroll_x =ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","rollno","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Class Division")
        self.student_table.heading("rollno",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date of Birth")
        self.student_table.heading("email",text="Email ID")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Mentor Name")
        self.student_table.heading("photo",text="Sample Image")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        #Fuctions To ADD DATA

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
             messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
             try:
                conn = mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
                my_cursor =conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_sem.get(),
                                                                                                                        self.var_stu_id.get(),
                                                                                                                        self.var_stu_name.get(),
                                                                                                                        self.var_stu_div.get(),
                                                                                                                        self.var_stu_rollno.get(),
                                                                                                                        self.var_stu_gender.get(),
                                                                                                                        self.var_stu_dob.get(),
                                                                                                                        self.var_stu_email.get(),
                                                                                                                        self.var_stu_phn.get(),
                                                                                                                        self.var_stu_address.get(),
                                                                                                                        self.var_stu_mentor.get(),
                                                                                                                        self.var_radio1.get()
                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student detials has been added to database",parent=self.root)
             except  Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

#=========================== fetch DATa
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
        my_cursor =conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()


        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()




#===============================Get DATA 

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_stu_id.set(data[4]),
        self.var_stu_name.set(data[5]),
        self.var_stu_div.set(data[6]),
        self.var_stu_rollno.set(data[7]),
        self.var_stu_gender.set(data[8]),
        self.var_stu_dob.set(data[9]),
        self.var_stu_email.set(data[10]),
        self.var_stu_phn.set(data[11]),
        self.var_stu_address.set(data[12]),
        self.var_stu_mentor.set(data[13]),
        self.var_radio1.set(data[14])


#========= Update Function
    def Update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_stu_name.get() == "" or self.var_stu_id.get() == "":
             messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to Update Student Details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE student SET dep=%s, course=%s, year=%s, sem=%s, name=%s, `div`=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, `sample photo`=%s WHERE studentid=%s", (
                                                                                                                                        self.var_dep.get(),
                                                                                                                                        self.var_course.get(),
                                                                                                                                        self.var_year.get(),
                                                                                                                                        self.var_sem.get(),
                                                                                                                                        self.var_stu_name.get(),
                                                                                                                                        self.var_stu_div.get(),
                                                                                                                                        self.var_stu_rollno.get(),
                                                                                                                                        self.var_stu_gender.get(),
                                                                                                                                        self.var_stu_dob.get(),
                                                                                                                                        self.var_stu_email.get(),
                                                                                                                                        self.var_stu_phn.get(),
                                                                                                                                        self.var_stu_address.get(),
                                                                                                                                        self.var_stu_mentor.get(),
                                                                                                                                        self.var_radio1.get(),
                                                                                                                                        self.var_stu_id.get()
                ))
                else:
                     if not Update:
                        return
                messagebox.showinfo("Success", "Student Record Updated Successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)



#====================== Delete Function
    def delete_data(self):
        if self.var_stu_id.get()=="":
            messagebox.showerror("Error","Please Select a Student ID",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page ","Do you want to delete this student details",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where studentid=%s"
                    val=(self.var_stu_id.get(),)
                    my_cursor.execute(sql,val)
                    self.fetch_data()
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Sucessfully Deleted Student Details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)   



#reset Button
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_stu_id.set("")
        self.var_stu_name.set("")
        self.var_stu_div.set("Select Division")
        self.var_stu_rollno.set("")
        self.var_stu_gender.set("Select Gender")
        self.var_stu_dob.set("")
        self.var_stu_email.set("")
        self.var_stu_phn.set("")
        self.var_stu_address.set("")
        self.var_stu_mentor.set("")
        self.var_radio1.set("")

#===============================Generate Dataset with Samples
    def genrate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_stu_name.get() == "" or self.var_stu_id.get() == "":
             messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
                my_cursor =conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                print(myresult)
                record_count = 0
                for x in myresult:
                    record_count += 1
                my_cursor.execute("UPDATE student SET dep=%s, course=%s, year=%s, sem=%s, name=%s, `div`=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, `sample photo`=%s WHERE studentid=%s", (
                                                                                                                                        self.var_dep.get(),
                                                                                                                                        self.var_course.get(),
                                                                                                                                        self.var_year.get(),
                                                                                                                                        self.var_sem.get(),
                                                                                                                                        self.var_stu_name.get(),
                                                                                                                                        self.var_stu_div.get(),
                                                                                                                                        self.var_stu_rollno.get(),
                                                                                                                                        self.var_stu_gender.get(),
                                                                                                                                        self.var_stu_dob.get(),
                                                                                                                                        self.var_stu_email.get(),
                                                                                                                                        self.var_stu_phn.get(),
                                                                                                                                        self.var_stu_address.get(),
                                                                                                                                        self.var_stu_mentor.get(),
                                                                                                                                        self.var_radio1.get(),
                                                                                                                                        self.var_stu_id.get()==record_count+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #=============Load  the data into treeview
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                        gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    print("Current img_id:", img_id)
                    print("Record count: ",record_count)
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        timestamp = int(time.time())
                        file_name_path = "data/user."+str(record_count)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                        
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Data has been saved successfully.")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)






        if __name__ == "__main__":
                root = Tk()
                obj = Student(root)
                root.mainloop()
