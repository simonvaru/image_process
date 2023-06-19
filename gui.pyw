from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
##
import numpy as np
import png
from PIL import Image, ImageTk

# <a href="https://www.flaticon.com/free-icons/school" title="school icons">School icons created by Freepik - Flaticon</a>
# <a href="https://www.flaticon.com/free-icons/calculator" title="calculator icons">Calculator icons created by Freepik - Flaticon</a>
# <a href="https://www.flaticon.com/free-icons/id-card" title="id card icons">Id card icons created by Freepik - Flaticon</a>
# <a href="https://www.flaticon.com/free-icons/glasses" title="glasses icons">Glasses icons created by Freepik - Flaticon</a>

####################################1st winndow using Menubuttom########################
def write_image(self, output_file_name, gamma=2.2):
    '''
    3D numpy array (Y, X, channel) of values between 0 and 1 -> write to png
    '''
    im = np.clip(self.array, 0, 1)
    y, x, _ = self.array.shape
    im = im ** gamma
    im = (255 * im).astype(np.uint8)

    writer = png.Writer(x, y)
    with open(self.output_path + output_file_name, 'wb') as f:
        writer.write(f, im.reshape(-1, x * self.num_channels))

    self.array.resize(y, x, self.num_channels)

def read_image(self, filename, gamma=2.2):
    '''
    read PNG RGB image, return 3D numpy array organized along Y, X, channel
    values are float, gamma is decoded
    '''
    im = png.Reader(self.input_path + filename).asFloat()
    resized_image = np.vstack(list(im[2]))
    resized_image.resize((im[1], im[0], 3))
    resized_image = resized_image ** gamma
    return resized_image

def write_image(self, output_file_name, gamma=2.2):
    '''
    3D numpy array (Y, X, channel) of values between 0 and 1 -> write to png
    '''
    im = np.clip(self.array, 0, 1)
    y, x, _ = self.array.shape
    im = im ** gamma
    im = (255 * im).astype(np.uint8)

    writer = png.Writer(x, y)
    with open(self.output_path + output_file_name, 'wb') as f:
        writer.write(f, im.reshape(-1, x * self.num_channels))

    self.array.resize(y, x, self.num_channels)


##

def open_command():#### EXITO!!!!!!

    ftypes = [('PNG files', '*.png'), ('All files', '*')]
    dlg = filedialog.Open(initialdir="input", title="Choose image to edit", filetypes = ftypes)
    file_path = dlg.show()

    if file_path:
        # Open the image using PIL
        image = Image.open(file_path)

        # Convert the image to PhotoImage format for Tkinter
        im = ImageTk.PhotoImage(image)
        # Create a label to display the image
        label = Label(root, image=im)
        label.pack()

        # Save the image to a file
        output_path = 'output/'
        image.save(output_path+'test.png')
        
  
    
    
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
    messagebox.showinfo("PNG Image Editor", "Author: Simon vargas Russo")    

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
file_menu.add_command(label="Open File  ", command=open_command)
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

