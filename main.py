from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from Student import Student
from train import Train
from face_recog import Face_Recognition


class Face_Recognition_System:
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

        title_lbl = Label(bg_img,text="Face Recognition Attendance System Sofware", font=("times new roman",36,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #Btn Chi tiết student
        img5 =Image.open(r"imgGui/btnStudent.png")
        img5=img5.resize((200,200),Image.BICUBIC)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=200)

        b1_1 = Button(bg_img,text="Chi tiết học sinh",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=200,height=40)



        #Detect Face
        img6 =Image.open(r"imgGui/btndetec.png")
        img6=img6.resize((200,200),Image.BICUBIC)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2 = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=200,height=200)

        b2_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=500,y=300,width=200,height=40)



        #Attendance
        img7 =Image.open(r"imgGui/attendance.jpg")
        img7=img7.resize((200,200),Image.BICUBIC)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b3 = Button(bg_img,image=self.photoimg7,cursor="hand2")
        b3.place(x=800,y=100,width=200,height=200)

        b3_1 = Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=800,y=300,width=200,height=40)


        #Help btn
        img8 =Image.open(r"imgGui/help.png")
        img8=img8.resize((200,200),Image.BICUBIC)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b4 = Button(bg_img,image=self.photoimg8,cursor="hand2")
        b4.place(x=1100,y=100,width=200,height=200)

        b4_1 = Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1100,y=300,width=200,height=40)




        #đây là dòng dưới
        #Train Data
        img9 =Image.open(r"imgGui/traindata.jpg")
        img9=img9.resize((200,200),Image.BICUBIC)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b5 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=400,width=200,height=200)

        b5_1 = Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=200,y=600,width=200,height=40)



        #Photos
        img10 =Image.open(r"imgGui/listphotos.png")
        img10=img10.resize((200,200),Image.BICUBIC)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b6 = Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=400,width=200,height=200)

        b6_1 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=500,y=600,width=200,height=40)



        #Dev
        img11 =Image.open(r"imgGui/dev.png")
        img11=img11.resize((200,200),Image.BICUBIC)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b7 = Button(bg_img,image=self.photoimg11,cursor="hand2")
        b7.place(x=800,y=400,width=200,height=200)

        b7_1 = Button(bg_img,text="Dev",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_1.place(x=800,y=600,width=200,height=40)


        #Help btn
        img12 =Image.open(r"imgGui/exit.png")
        img12=img12.resize((200,200),Image.BICUBIC)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b8 = Button(bg_img,image=self.photoimg12,cursor="hand2")
        b8.place(x=1100,y=400,width=200,height=200)

        b8_1 = Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_1.place(x=1100,y=600,width=200,height=40)




    def open_img(self):
        os.startfile("data")



    #===============Function buttons==============

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Train(self.new_window)



    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)









if __name__=="__main__":
    root=Tk()
    obj =Face_Recognition_System(root)
    root.mainloop()
