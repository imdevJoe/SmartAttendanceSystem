from tkinter import *
from PIL import ImageTk
import subprocess
from tkinter import  messagebox
import cv2
import face_recognition
import mysql.connector
import pickle
import os

root = Tk()

def markAttendance_click(event):
    root.destroy()
    subprocess.run(["python", "attendance.py"])



def addStudent_click(event):
    root.destroy()
    subprocess.run(["python", "addStudent.py"])


# Window dimensions
window_width = 650
window_height = 550

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Center the window on the screen
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
root.resizable(0, 0)
root.title('Welcome')

# Load and place background image
bgImage = ImageTk.PhotoImage(file='decisionBg.jpg')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

# Creating a label that acts like a button
text_label = Label(root, text="Add Student",bg= '#DDA8B5', fg='white', cursor="hand2",font=('Microsoft Yahei UI Light', 13, 'bold'),)
text_label.place(x=44, y=390)  # Adjust position as needed
text_label.bind("<Button-1>",addStudent_click)

markAttendance = Label(root, text="Attendance",bg= '#DDA8B5', fg='white', cursor="hand2",font=('Microsoft Yahei UI Light', 13, 'bold'),)
markAttendance.place(x=44, y=270)
markAttendance.bind("<Button-1>",markAttendance_click)


root.mainloop()
