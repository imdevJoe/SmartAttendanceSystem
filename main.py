# # import tkinter as tk
# # from tkinter import Toplevel
# # from tkinter import *
# # import subprocess
# #
# #
# # def open_sign_up(event):
# #     subprocess.run(["python", "signUp.py"])
# #     root.destroy()
# #
# # # Function to open child windows
# # def open_child_window_1():
# #     child_window_1 = Toplevel(root)
# #     child_window_1.title("Child Window 1")
# #     child_window_1.geometry("300x200")
# #     # Add widgets to the child window 1
# #     lbl = tk.Label(child_window_1, text="This is child window 1")
# #     lbl.pack(pady=20)
# #
# # def open_child_window_2():
# #     child_window_2 = Toplevel(root)
# #     child_window_2.title("Child Window 2")
# #     child_window_2.geometry("300x200")
# #     # Add widgets to the child window 2
# #     lbl = tk.Label(child_window_2, text="This is child window 2")
# #     lbl.pack(pady=20)
# #
# # def open_child_window_3():
# #     child_window_3 = Toplevel(root)
# #     child_window_3.title("Child Window 3")
# #     child_window_3.geometry("300x200")
# #     # Add widgets to the child window 3
# #     lbl = tk.Label(child_window_3, text="This is child window 3")
# #     lbl.pack(pady=20)
# #
# # def open_child_window_4():
# #     child_window_4 = Toplevel(root)
# #     child_window_4.title("Child Window 4")
# #     child_window_4.geometry("300x200")
# #     # Add widgets to the child window 4
# #     lbl = tk.Label(child_window_4, text="This is child window 4")
# #     lbl.pack(pady=20)
# #
# # # Main window setup
# # root = Tk()
# # root.title("Main Window")
# # root.geometry("1366x768")
# #
# # # Load and set the background image
# # background_image = tk.PhotoImage(file="rootBg.png")
# # canvas = tk.Canvas(root, width=1366, height=768)
# # canvas.pack(fill="both", expand=True)
# # canvas.create_image(0, 0, image=background_image, anchor="nw")
# #
# # # Add buttons to open child windows
# # # open_child_btn_1 = tk.Button(root, text="Open Child Window 1", command=open_child_window_1)
# # # open_child_btn_2 = tk.Button(root, text="Open Child Window 2", command=open_child_window_2)
# # # open_child_btn_3 = tk.Button(root, text="Open Child Window 3", command=open_child_window_3)
# # # open_child_btn_4 = tk.Button(root, text="Open Child Window 4", command=open_child_window_4)
# #
# # # canvas.create_window(50, 50, anchor="nw", window=open_child_btn_1)
# # # canvas.create_window(50, 100, anchor="nw", window=open_child_btn_2)
# # # canvas.create_window(50, 150, anchor="nw", window=open_child_btn_3)
# # # canvas.create_window(50, 200, anchor="nw", window=open_child_btn_4)
# #
# # text_label = Label(root, text="Click to Continue",bg= '#B4BEE4', fg='#89A0DB', cursor="hand2",font=('lemon juice', 30, 'bold'),)
# # text_label.place(x=690, y=555)  # Adjust position as needed
# # text_label.bind("<Button-1>",open_sign_up)
# #
# # root.mainloop()
# import tkinter as tk
# from tkinter import Toplevel
# from tkinter import *
# import subprocess
#
# def open_sign_up(event):
#     subprocess.run(["python", "signUp.py"])
#     # Change the background image
#     # new_background_image = tk.PhotoImage(file="rRootBg.png")
#     # canvas.itemconfig(background_image_id, image=new_background_image)
#     # canvas.image = new_background_image  # Keep a reference to prevent garbage collection
#     # Enable other buttons (if needed)
#     enable_other_buttons()
#
# # Function to open child windows
# def open_child_window_1():
#     child_window_1 = Toplevel(root)
#     child_window_1.title("Child Window 1")
#     child_window_1.geometry("300x200")
#     # Add widgets to the child window 1
#     lbl = tk.Label(child_window_1, text="This is child window 1")
#     lbl.pack(pady=20)
#
# def open_child_window_2():
#     child_window_2 = Toplevel(root)
#     child_window_2.title("Child Window 2")
#     child_window_2.geometry("300x200")
#     # Add widgets to the child window 2
#     lbl = tk.Label(child_window_2, text="This is child window 2")
#     lbl.pack(pady=20)
#
# def open_child_window_3():
#     child_window_3 = Toplevel(root)
#     child_window_3.title("Child Window 3")
#     child_window_3.geometry("300x200")
#     # Add widgets to the child window 3
#     lbl = tk.Label(child_window_3, text="This is child window 3")
#     lbl.pack(pady=20)
#
# def open_child_window_4():
#     child_window_4 = Toplevel(root)
#     child_window_4.title("Child Window 4")
#     child_window_4.geometry("300x200")
#     # Add widgets to the child window 4
#     lbl = tk.Label(child_window_4, text="This is child window 4")
#     lbl.pack(pady=20)
#
# # Function to enable other buttons after successful login
# def enable_other_buttons():
#     open_child_btn_1.config(state=tk.NORMAL)
#     open_child_btn_2.config(state=tk.NORMAL)
#     open_child_btn_3.config(state=tk.NORMAL)
#     open_child_btn_4.config(state=tk.NORMAL)
#
# # Main window setup
# root = Tk()
# root.title("Main Window")
# root.geometry("1366x768")
#
# # Load and set the background image
# background_image = tk.PhotoImage(file="rootBg.png")
# canvas = tk.Canvas(root, width=1366, height=768)
# canvas.pack(fill="both", expand=True)
# background_image_id = canvas.create_image(0, 0, image=background_image, anchor="nw")
#
# # Add buttons to open child windows
# open_child_btn_1 = tk.Button(root, text="Open Child Window 1", command=open_child_window_1,)
# open_child_btn_2 = tk.Button(root, text="Open Child Window 2", command=open_child_window_2, state=tk.DISABLED)
# open_child_btn_3 = tk.Button(root, text="Open Child Window 3", command=open_child_window_3, state=tk.DISABLED)
# open_child_btn_4 = tk.Button(root, text="Open Child Window 4", command=open_child_window_4, state=tk.DISABLED)
#
# canvas.create_window(50, 50, anchor="nw", window=open_child_btn_1)
# canvas.create_window(50, 100, anchor="nw", window=open_child_btn_2)
# canvas.create_window(50, 150, anchor="nw", window=open_child_btn_3)
# canvas.create_window(50, 200, anchor="nw", window=open_child_btn_4)
#
# text_label = Label(root, text="Click to Continue", bg='#B4BEE4', fg='#89A0DB', cursor="hand2", font=('lemon juice', 30, 'bold'))
# text_label.place(x=690, y=555)  # Adjust position as needed
# text_label.bind("<Button-1>", open_sign_up)
#
# root.mainloop()
from tkinter import *
from PIL import ImageTk
import subprocess

def open_sign_up(event):
    root.destroy()
    subprocess.run(["python", "signUp.py"])


root = Tk()

# Window dimensions
window_width = 1366
window_height = 768

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Center the window on the screen
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
root.resizable(0, 0)
root.title('Main')

# Load and place background image
bgImage = ImageTk.PhotoImage(file='rootBg.png')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)




text_label = Label(root, text="Click to Continue", bg='#B4BEE4', fg='#89A0DB', cursor="hand2", font=('lemon juice', 30, 'bold'))
text_label.place(x=690, y=555)  # Adjust position as needed
text_label.bind("<Button-1>", open_sign_up)


root.mainloop()