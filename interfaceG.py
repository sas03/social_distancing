
from tkinter import *

from tkinter import filedialog
from social_distance_detector import main


FILE = ""
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Video files",
                                                      "*.mp4*"),
                                                     ("all files",
                                                      "*.*")))

    label_file_explorer.configure(text="File Opened: " + filename)
    main(filename)

window = Tk()

window.title('File Explorer')

window.geometry("700x500")

window.config(background="white")

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


label_file_explorer.grid(column=1, row=1)

button_webcam.grid(column=1, row=2)
button_explore.grid(column=1, row=3)


button_exit.grid(column=1, row=4)

window.mainloop()
