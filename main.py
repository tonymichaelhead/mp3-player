import os
import pygame
from tkinter.filedialog import askdirectory
from tkinter import *

root = Tk()
root.minsize(300,300)

listofsongs = []

index = 0

def directorychooser():

    directory = askdirectory()  
    os.chdir(directory)

    for files in os.listdir():
        if files.endswith(".mp3"):

            listofsongs.append(files)
            print(files)

root.mainloop()