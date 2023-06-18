from tkinter import *

def file_menu_command():
    print("File menu command executed.")

def edit_menu_command():
    print("Edit menu command executed.")

def help_menu_command():
    print("Help menu command executed.")

root = Tk()
root.title("Menu Example")
root.config(bg="blue")

#create root
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
file_menu.add_command(label="Open", command=file_menu_command)
file_menu.add_command(label="Save", command=file_menu_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#create edit menu
edit_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Prove .png editing", command=edit_menu_command)
edit_menu.add_command(label="Brighten", command=edit_menu_command)
edit_menu.add_command(label="Adjust contrast", command=edit_menu_command)
edit_menu.add_command(label="Blur", command=edit_menu_command)
edit_menu.add_command(label="Apply kernel", command=edit_menu_command)
edit_menu.add_command(label="Combine images", command=edit_menu_command)

#create help menu
help_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=help_menu_command)

root.mainloop()


