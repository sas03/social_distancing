# Python program to create 
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog
from social_distance_detector import main


# Function for opening the
# file explorer window
FILE = ""
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Video files",
                                                      "*.mp4*"),
                                                     ("all files",
                                                      "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)
    main(filename)

# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("700x500")

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="Distanciation sociale",
                            width=100, height=4,
                            fg="blue")

button_explore = Button(window,
                        text="Selectionner une Vidéo ou une image",
                        command=browseFiles)
button_webcam= Button(window,
                        text="Lancer via WebCam",
                        command=main)

button_exit = Button(window,
                     text="Exit",
                     command=exit)

# Grid method is chosen for placing
# the widgets at respective positions 
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column=1, row=1)

button_webcam.grid(column=1, row=2)
button_explore.grid(column=1, row=3)


button_exit.grid(column=1, row=4)

# Let the window wait for any events
window.mainloop()
