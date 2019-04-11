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

directorychooser()
root.mainloop()