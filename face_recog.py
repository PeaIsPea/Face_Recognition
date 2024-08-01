from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root =root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root,text="FACE RECOGNITION", font=("times new roman",36,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top =Image.open(r"imgGui/bg.png")
        img_top=img_top.resize((650,700),Image.BICUBIC)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        frame_label = Label(self.root,image=self.photoimg_top)
        frame_label.place(x=0,y=55,width=650,height=700)

        img_bottom =Image.open(r"imgGui/bg.png")
        img_bottom=img_bottom.resize((950,700),Image.BICUBIC)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        frame_label = Label(self.root,image=self.photoimg_bottom)
        frame_label.place(x=650,y=55,width=950,height=700)

        b1_1 = Button(frame_label,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="RED",fg="white")
        b1_1.place(x=350,y=620,width=250,height=50)


#=========FACE RECOGNITON ==============


    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color, text, clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y + h),(0,255,0),3)
                id, predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))


                conn=mysql.connector.connect(user = 'root', password='123123',host='localhost',database= 'face')
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id= "+ str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)


                my_cursor.execute("select Roll from student where Student_id= "+ str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)


                my_cursor.execute("select Dep from student where Student_id= "+ str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)


                if confidence > 77:

                    cv2.putText(img,f"Roll: {r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8(255,255,255),3)
                    cv2.putText(img,f"Name: {n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8(255,255,255),3)
                    cv2.putText(img,f"Department: {d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8(255,255,255),3)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y + h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img, clf,faceCascade):
            coord = draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()

        clf.read("classi/classifier.xml")

        video_cap= cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
            video_cap.release()

            cv2.destroyAllWindows()




    





if __name__=="__main__":
    root=Tk()
    obj =Face_Recognition(root)
    root.mainloop()