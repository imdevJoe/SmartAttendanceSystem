# from tkinter import *
# from PIL import ImageTk
#
# def once_clicked(event):
#     if usernameEntry.get() == "Username":
#         usernameEntry.delete(0, END)
#
# def pass_click(event):
#     if passwordEntry.get() == "Password":
#         passwordEntry.delete(0, END)
#
# root = Tk()
#
# # Window dimensions
# window_width = 990
# window_height = 660
#
# # Get screen dimensions
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
#
# # Calculate position
# position_top = int(screen_height / 2 - window_height / 2)
# position_right = int(screen_width / 2 - window_width / 2)
#
# # Center the window on the screen
# root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
# root.resizable(0, 0)
# root.title('LOGIN')
#
# # Load and place background image
# bgImage = ImageTk.PhotoImage(file='signIn.jpg')
# bgLabel = Label(root, image=bgImage)
# bgLabel.place(x=0, y=0)
#
# # Heading
# heading = Label(root, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white', fg='#EFA8CD')
# heading.place(x=650, y=120)
#
# # Username field
# usernameEntry = Entry(root, width=25, font=('Microsoft Yahei UI Light', 10, 'bold'), bd=0, fg='#EFA8CD')
# usernameEntry.place(x=660, y=200)
# usernameEntry.insert(0, 'Username')
# usernameEntry.bind('<FocusIn>', once_clicked)
#
# # Username underline
# Frame1 = Frame(root, width=180, height=2, bg='#EFA8CD')
# Frame1.place(x=660, y=220)
#
# # User password
# passwordEntry = Entry(root, width=25, font=('Microsoft Yahei UI Light', 10, 'bold'), bd=0, fg='#EFA8CD')
# passwordEntry.place(x=660, y=300)
# passwordEntry.insert(0, 'Password')
# passwordEntry.bind('<FocusIn>', pass_click)
#
# # Password underline
# Frame2 = Frame(root, width=180, height=2, bg='#EFA8CD')
# Frame2.place(x=660, y=320)
#
# signInButton = Button(root,bd=-5,bg='#EFA8CD', fg='white', text='Log In')
# signInButton.place(x=740,y=380)
# root.mainloop()
from tkinter import *
from PIL import ImageTk
import subprocess

def once_clicked(event):
    if usernameEntry.get() == "Username":
        usernameEntry.delete(0, END)

def pass_click(event):
    if passwordEntry.get() == "Password":
        passwordEntry.delete(0, END)

def check_credentials():
    if usernameEntry.get() == "ipmc" and passwordEntry.get() == "joe":
        root.destroy()
        subprocess.run(["python", "descisionPage.py"])
    else:
        error_label.config(text="Incorrect username or password")

root = Tk()

# Window dimensions
window_width = 813
window_height = 475

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Center the window on the screen
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
root.resizable(0, 0)
root.title('LOGIN')

# Load and place background image
bgImage = ImageTk.PhotoImage(file='signUp.jpg')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

# Heading
heading = Label(root, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white', fg='#EFA8CD')
heading.place(x=550, y=80)

# Username field
usernameEntry = Entry(root, width=25, font=('Microsoft Yahei UI Light', 10, 'bold'), bd=0, fg='#EFA8CD')
usernameEntry.place(x=550, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', once_clicked)

# Username underline
Frame1 = Frame(root, width=180, height=2, bg='#EFA8CD')
Frame1.place(x=550, y=220)

# User password
passwordEntry = Entry(root, width=25, font=('Microsoft Yahei UI Light', 10, 'bold'), bd=0, fg='#EFA8CD', show='*')
passwordEntry.place(x=550, y=300)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', pass_click)

# Password underline
Frame2 = Frame(root, width=180, height=2, bg='#EFA8CD')
Frame2.place(x=550, y=320)

# Error message label
error_label = Label(root, text='', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='red')
error_label.place(x=550, y=350)

# Log In button
signInButton = Button(root, bd=-5, bg='#EFA8CD', fg='white', text='Log In', command=check_credentials, font=('lemon juice',20
                                                                                                             ))
signInButton.place(x=600, y=380)

root.mainloop()
