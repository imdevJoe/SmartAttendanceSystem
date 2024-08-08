import tkinter as tk
from tkinter import  *
from tkinter import messagebox, filedialog
import mysql.connector
from datetime import datetime
from PIL import Image, ImageTk
import cv2
import os
import subprocess


root = Tk()

# def run_script(script_path):
#     process = subprocess.Popen(["python", script_path],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     output, error= process.communicate()
#
#     if error:
#         error_message = error.decode('utf-8')
#         messagebox.showerror("Error", error_message)
#     else:
#         output_message = output.decode('utf-8')
#
#         if "Exception:" in output_message:
#             messagebox.showerror("Error", output_message)
#         else:
#             messagebox.showinfo("Output", output_message)

def run_script(script_path):
    process = subprocess.Popen(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        error_message = error.decode('utf-8')
        messagebox.showerror("Error", error_message)
    else:
        output_message = output.decode('utf-8')

        if "Exception:" in output_message:
            messagebox.showerror("Error", output_message)
        else:
            messagebox.showinfo("Output", output_message)


# root dimensions
root_width = 750
root_height = 650

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position
position_top = int(screen_height / 2 - root_height / 2)
position_right = int(screen_width / 2 - root_width / 2)

# Center the root on the screen
root.geometry(f'{root_width}x{root_height}+{position_right}+{position_top}')
root.resizable(0, 0)
root.title('Welcome')

# Load and place background image
bgImage = ImageTk.PhotoImage(file='addstudentBg.jpg')
bgLabel = tk.Label(root, image=bgImage)
bgLabel.place(x=0, y=0)


# Function to handle button click (Insert Data)
def insert_data():
    # Retrieve values from entry fields
    student_id = entry_student_id.get()
    name = entry_name.get()
    course = entry_course.get()
    starting_year = entry_starting_year.get()
    total_attendance = entry_total_attendance.get()
    standing = entry_standing.get()
    last_attendance_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current timestamp
    image_path = entry_image_path.get()

    try:
        # Open the image and resize it to 216 x 216 pixels
        with Image.open(image_path) as img:
            img = img.resize((216, 216))
            resized_image_path = f"images/{student_id}.jpg"
            img.save(resized_image_path)

        # Connect to MySQL database
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="attendance_db"
        )

        # Execute SQL query to insert data into Students table
        cursor = db_connection.cursor()

        sql = "INSERT INTO Students (student_id, name, course, starting_year, total_attendance, standing, last_attendance_time, image_path) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
        student_id, name, course, starting_year, total_attendance, standing, last_attendance_time, resized_image_path)
        cursor.execute(sql, values)

        # Commit changes to database
        db_connection.commit()

        messagebox.showinfo("Success", "Data inserted successfully!")

        # Clear the entry fields after successful insertion
        clear_entries()

        # Close cursor and database connection
        cursor.close()
        db_connection.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")


# Function to open file dialog and select image file
def browse_image():
    filename = filedialog.askopenfilename(initialdir="/", title="Select Image", filetypes=(
    ("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
    entry_image_path.delete(0, tk.END)
    entry_image_path.insert(tk.END, filename)


# Function to take a picture using the webcam
def take_picture():
    student_id = entry_student_id.get()
    if not student_id:
        messagebox.showerror("Error", "Please enter a Student ID before taking a picture.")
        return

    # Open the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Cannot open webcam")
        return

    messagebox.showinfo("Info", "Press 's' to save the image and 'q' to quit without saving.")

    while True:
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "Failed to capture image")
            break

        cv2.imshow("Capture Image", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            resized_frame = cv2.resize(frame, (216, 216))
            file_path = f"images/{student_id}.jpg"
            cv2.imwrite(file_path, resized_frame)
            messagebox.showinfo("Info", f"Image saved as {file_path}")
            entry_image_path.delete(0, tk.END)
            entry_image_path.insert(tk.END, file_path)
            break
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Function to clear all entry fields
def clear_entries():
    entry_student_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_starting_year.delete(0, tk.END)
    entry_total_attendance.delete(0, tk.END)
    entry_standing.delete(0, tk.END)
    entry_image_path.delete(0, tk.END)


def back_click():
    root.destroy()
    subprocess.run(["python", "descisionPage.py"])


# Create labels and entry fields for each attribute
Label(root, text="Student ID:", bg='#DDA8B5', fg='white', cursor="hand2", font=('lemon juice', 20, 'bold')).place(x=70,
                                                                                                                  y=90)
entry_student_id = Entry(root, font=('lemon juice', 20))
entry_student_id.place(x=250, y=90)

Label(root, text="Name:", bg='#DDA8B5', fg='white', cursor="hand2", font=('lemon juice', 20, 'bold')).place(x=70, y=150)
entry_name = Entry(root, font=('lemon juice', 20))
entry_name.place(x=250, y=150)

Label(root, text="Course:", bg='#DDA8B5', fg='white', cursor="hand2", font=('lemon juice', 20, 'bold')).place(x=70,
                                                                                                              y=200)
entry_course = Entry(root, font=('lemon juice', 20))
entry_course.place(x=250, y=200)

Label(root, text="Starting Year:", bg='#DDA8B5', fg='white', cursor="hand2", font=('lemon juice', 20, 'bold')).place(
    x=70, y=250)
entry_starting_year = Entry(root, font=('lemon juice', 20))
entry_starting_year.place(x=250, y=250)

Label(root, text="Total Attendance:", bg='#DDA8B5', fg='white', cursor="hand2", font=('lemon juice', 20, 'bold')).place(
    x=70, y=300)
entry_total_attendance = Entry(root, font=('lemon juice', 20))
entry_total_attendance.place(x=250, y=300)

Label(root, text="Standing:", bg='#DDA8B5', fg='white', cursor="hand2", font=('lemon juice', 20, 'bold')).place(x=70,
                                                                                                                y=350)
entry_standing = Entry(root, font=('lemon juice', 20))
entry_standing.place(x=250, y=350)

Label(root, text="Image Path:", bg='#DDA8B5', fg='white', cursor="hand2", font=('lemon juice', 20, 'bold')).place(x=70,
                                                                                                                  y=400)
entry_image_path = Entry(root, font=('lemon juice', 20))
entry_image_path.place(x=250, y=400)

# Button to browse image file
button_browse = Button(root, text="Browse", command=browse_image, bg='#DDA8B5', fg='white', cursor="hand2",
                       font=('lemon juice', 20, 'bold'))
button_browse.place(x=550, y=400)

# Button to take a picture
button_take_picture = Button(root, text="Take Picture", command=take_picture, bg='#DDA8B5', fg='white', cursor="hand2",
                             font=('lemon juice', 20, 'bold'))
button_take_picture.place(x=550, y=450)

# Create a button to insert data
button_insert = Button(root, text="Insert Data", command=insert_data, bg='#DDA8B5', fg='white', cursor="hand2",
                       font=('lemon juice', 20, 'bold'))
button_insert.place(x=350, y=500)

# Create a button to move back to the decision page
backButton = Button(root, text="Back", bg='#DDA8B5', command=back_click, fg='white', cursor="hand2",
                    font=('lemon juice', 20, 'bold'))
backButton.place(x=30, y=20)

# Enconde button
encodeButton = Button(root,text='encode', bd=-5, bg='#EFA8CD', fg='white', command=lambda: run_script('encodeGenerator.py'), font=('lemon juice', 20))
encodeButton.place(x=200, y=500)


# Run the tkinter main loop
root.mainloop()

