from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root =root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #First
        img =Image.open(r"imgGui/bg.png")
        img=img.resize((500,130),Image.BICUBIC)
        self.photoimg=ImageTk.PhotoImage(img)

        frame_label = Label(self.root,image=self.photoimg)
        frame_label.place(x=0,y=0,width=475,height=130)



        #Second
        img2 =Image.open(r"imgGui/bgmidtop.jpg")
        img2=img2.resize((500,200),Image.BICUBIC)
        self.photoimg2=ImageTk.PhotoImage(img2)

        frame_label = Label(self.root,image=self.photoimg2)
        frame_label.place(x=500,y=0,width=500,height=130)


        #Third
        img3 =Image.open(r"imgGui/bg.png")
        img3=img3.resize((500,130),Image.BICUBIC)
        self.photoimg3=ImageTk.PhotoImage(img3)

        frame_label = Label(self.root,image=self.photoimg3)
        frame_label.place(x=1000,y=0,width=550,height=130)


        #bg image
        img4 =Image.open(r"imgGui/bgmid.jpg")
        img4=img4.resize((1530,710),Image.BICUBIC)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img,text="Hệ thống quản lí học sinh", font=("times new roman",36,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)


        #left label frame
        Left_frame= LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        
        img_left =Image.open(r"imgGui/bg.png")
        img_left=img_left.resize((720,130),Image.BICUBIC)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        frame_label = Label(Left_frame,image=self.photoimg_left)
        frame_label.place(x=5,y=0,width=720,height=130)


        #current course infor
        current_course_frame= LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course information",font=("time new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=115)

        #Deparment
        dep_label = Label(current_course_frame,text="Deparment",font=("time new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)


        dep_combo = ttk.Combobox(current_course_frame,font=("time new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Deparment","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #Course
        course_label = Label(current_course_frame,text="Course",font=("time new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)


        course_combo = ttk.Combobox(current_course_frame,font=("time new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Years
        years_label = Label(current_course_frame,text="Year",font=("time new roman",13,"bold"),bg="white")
        years_label.grid(row=1,column=0,padx=10,sticky=W)


        year_combo = ttk.Combobox(current_course_frame,font=("time new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        semester_label = Label(current_course_frame,text="Semester",font=("time new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)


        semester_combo = ttk.Combobox(current_course_frame,font=("time new roman",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)



        #Class student infor
        class_student_frame= LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("time new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)


        #student ID
        StudentId_label = Label(class_student_frame,text="Student ID",font=("time new roman",13,"bold"),bg="white")
        StudentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry = ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #student name
        StudentName_label = Label(class_student_frame,text="Student Name",font=("time new roman",13,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        StudentName_entry = ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Class division
        Class_div_label = Label(class_student_frame,text="Class Division",font=("time new roman",13,"bold"),bg="white")
        Class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Class_division_entry = ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        Class_division_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #Roll No
        Roll_no_label = Label(class_student_frame,text="Roll No",font=("time new roman",13,"bold"),bg="white")
        Roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        RollNo_entry = ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        RollNo_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #Gender
        Gender_label = Label(class_student_frame,text="Gender",font=("time new roman",13,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Gender_entry = ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        Gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #DOB
        dob_label = Label(class_student_frame,text="DOB",font=("time new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry = ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #Email
        Email_label = Label(class_student_frame,text="Email",font=("time new roman",13,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Email_entry = ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #Phone no
        phone_label = Label(class_student_frame,text="Phone no",font=("time new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry = ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #Address
        Address_label = Label(class_student_frame,text="Address",font=("time new roman",13,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Address_entry = ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name
        techer_label = Label(class_student_frame,text="Teacher Name",font=("time new roman",13,"bold"),bg="white")
        techer_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry = ttk.Entry(class_student_frame,width=20,font=("time new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #Radio Buttons

        radbtn1 = ttk.Radiobutton(class_student_frame,text="Take Photo Sample",value="Yes")
        radbtn1.grid(row=6,column=0)

        radbtn2 = ttk.Radiobutton(class_student_frame,text="No Photo Sample",value="No")
        radbtn2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)


        save_btn=Button(btn_frame,text="Save",width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        #button frame2
        btn_frame2=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame2,text="Take Photo Sample",width=35,font=("time new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame2,text="Update Photo Sample",width=35,font=("time new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


        #Right label frame
        Right_frame= LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        img_right =Image.open(r"imgGui/bg.png")
        img_right=img_right.resize((720,130),Image.BICUBIC)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        frame_label = Label(Right_frame,image=self.photoimg_right)
        frame_label.place(x=5,y=0,width=720,height=130)


        #=====================Tim kiem Student==============


        Search_frame= LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("time new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=710,height=70)

        search_label = Label(Search_frame,text="Search by",font=("time new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        


        search_combo = ttk.Combobox(Search_frame,font=("time new roman",13,"bold"),state="readonly",width=10)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(Search_frame,width=15,font=("time new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)




        search_btn=Button(Search_frame,text="Search",width=12,font=("time new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        ShowAll_btn=Button(Search_frame,text="Show All",width=12,font=("time new roman",12,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=4)

        #==============Table Frame=============
        Table_frame= Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=210,width=710,height=350)

        srcoll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        srcoll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=srcoll_x.set,yscrollcommand=srcoll_y.set)

        srcoll_x.pack(side=BOTTOM,fill=X)
        srcoll_y.pack(side=RIGHT,fill=Y)

        srcoll_x.config(command=self.student_table.xview)
        srcoll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Deparmet")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")    
        
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")

        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("dep",width=100)

        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        

        
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        






if __name__=="__main__":
    root=Tk()
    obj =Student(root)
    root.mainloop()

