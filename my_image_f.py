"""
myImage class definition, including several own methods 
mainly used in gui.pyw

"""

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
##
import numpy as np
import png
from PIL import Image, ImageTk
import gui_root
from gui_root import root


class myImage:
      
    def __init__(self, x_pixels=0, y_pixels=0, num_channels=0, filename=''):
        # initialization and set of the array attribute
        self.array = np.zeros((y_pixels, x_pixels, num_channels))

    def write_image(self, output_file_name, gamma=2.2):
        '''
        3D numpy array (Y, X, channel) of values between 0 and 1 -> write to png
        '''
        output_path = 'output/'
        im = np.clip(self.array, 0, 1)
        y, x, _ = self.array.shape
        im = im ** gamma
        im = (255 * im).astype(np.uint8)

        writer = png.Writer(x, y)
        with open(output_path + output_file_name, 'wb') as f:
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

    def open_command(self):
        ftypes = [('PNG files', '*.png'), ('All files', '*')]
        dlg = filedialog.Open(initialdir="input", title="Choose image to edit", filetypes=ftypes)
        file_path = dlg.show()

        if file_path:
            # Open the image using PIL
            image = Image.open(file_path)

            # Convert the image to PhotoImage format for Tkinter
            im = ImageTk.PhotoImage(image)
            # Create a label to display the image
            label = Label(gui_root.root, image=im)
            label.pack()

            # Save the image to a file
            self.write_image('test.png')