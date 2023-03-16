from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import cv2
import os
import numpy as np


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Management System")


        img = Image.open(r"blue.jpg")
        img = img.resize((1366, 128), Image.Resampling.LANCZOS)  # resize and converting high level img to low level img.
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1366, height=138)

        title_lbl = Label(f_lbl, text="Student Management System", font=("times new roman", 30, "bold"), bg="white",
                          fg="red")
        title_lbl.place(x=25, y=25, width=1300, height=90)

        # bg image.
        img2 = Image.open(r"blue.jpg")
        img2 = img2.resize((1366, 640), Image.Resampling.LANCZOS)  # resize and converting high level img to low level img.
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=130, width=1366, height=640)

        # main frame
        main_frame = Frame(bg_img)
        main_frame.place(x=25, y=0, width=1300, height=560)



        # bbuttons_frame
        btn_frame = Frame(main_frame, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=200, width=600, height=85)


        # delete button
        delete_btn = Button(btn_frame, text="Train dataset",command=self.train_classifier, width=15,
                            font=("times new roman", 12, "bold"), fg="white", bg="red")
        delete_btn.grid(row=0, column=2, padx=2, pady=2, sticky=W)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')  # GreyScale Img
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

            # ======Train Classifier and Save======
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.yml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!")







if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()