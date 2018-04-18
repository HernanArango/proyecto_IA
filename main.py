from lib import *
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog


root = Tk()
root.filename = tkFileDialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
path=root.filename
root.destroy()
Interfaz = Interfaz()
Interfaz.ambInicial(str(path))

