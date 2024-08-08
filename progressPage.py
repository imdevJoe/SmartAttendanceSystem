from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import time
import subprocess

def open_main():
    root.destroy()
    subprocess.run(["python", "main.py"])


def update_progress_bar():
    for i in range(101):
        progress['value'] = i
        root.update_idletasks()
        time.sleep(0.1)
    open_main()

root = Tk()

# Window dimensions
window_width = 450
window_height = 350

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
bgImage = ImageTk.PhotoImage(file='progressBg.jpg')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

# Create and place the progress bar
progress = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
progress.place(x=25, y=300)

# Start updating the progress bar
root.after(50, update_progress_bar)

root.mainloop()

