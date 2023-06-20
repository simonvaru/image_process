from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
##
import numpy as np
import png
from PIL import Image, ImageTk
##
import my_image_f
import gui_root
from gui_root import root
# <a href="https://www.flaticon.com/free-icons/school" title="school icons">School icons created by Freepik - Flaticon</a>
# <a href="https://www.flaticon.com/free-icons/calculator" title="calculator icons">Calculator icons created by Freepik - Flaticon</a>
# <a href="https://www.flaticon.com/free-icons/id-card" title="id card icons">Id card icons created by Freepik - Flaticon</a>
# <a href="https://www.flaticon.com/free-icons/glasses" title="glasses icons">Glasses icons created by Freepik - Flaticon</a>



        
my_image=my_image_f.myImage()  
    
    
def save_command():
    print("File menu command executed.")    

def prove_command():
    print("Edit menu command executed.")

def brighten_command():
    print("Edit menu command executed.")
    
def contrast_command():
    print("Edit menu command executed.")

def blur_command():
    print("Edit menu command executed.")

def kernel_command():
    print("Edit menu command executed.")
    
def combine_command():
    print("Edit menu command executed.")
         
def about_info():
    messagebox.showinfo("PNG Image Editor", "Author: Simon Vargas Russo")    


####################################1st winndow using Menubuttom########################
myFrame = Frame(root)
myFrame.pack()


# red square for frame
canvas = Canvas(myFrame, bg="red", width=400, height=300)
canvas.pack(side="bottom")

#create menu bar
menubar = Menubutton(myFrame, text="PNG Image Editor", relief="raised", bg="lightgray")
menubar.pack(side="top", fill="x")

#create menu 
menu = Menu(menubar, tearoff=False)
menubar.config(menu=menu)

#create file menu
file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open File  ", command=my_image_f.open_command)
file_menu.add_command(label="Save", command=save_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#create edit menu
edit_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Prove .png editing", command=prove_command)
edit_menu.add_command(label="Brighten", command=brighten_command)
edit_menu.add_command(label="Adjust contrast", command=contrast_command)
edit_menu.add_command(label="Blur", command=blur_command)
edit_menu.add_command(label="Apply kernel", command=kernel_command)
edit_menu.add_command(label="Combine images", command=combine_command)

#create help menu
help_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about_info)


























####################################2st window using Frame########################
myFrame2=Frame(root)
myFrame2.pack(side="right")
myFrame2.config(bg="green")
myFrame2.config(width="650", height="350")
myFrame2.config(bd="5")
myFrame2.config(cursor="crosshair")
myFrame2.config(highlightbackground="grey")
myFrame2.config(relief="groove")                
myFrame2.config(cursor="cross")
myLabel2=Label(myFrame2, text="APP2")
myLabel2.place(x=5,y=5)  
miImagen2=PhotoImage(file="icons\glasses.png")
myLabel2b=Label(myFrame2, image=miImagen2)
myLabel2b.place(x=50,y=5)

root.mainloop()

