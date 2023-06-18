from tkinter import *
# import wxpython
# import pyqt
# import pygtk
# <a href="https://www.flaticon.com/free-icons/school" title="school icons">School icons created by Freepik - Flaticon</a>
# <a href="https://www.flaticon.com/free-icons/calculator" title="calculator icons">Calculator icons created by Freepik - Flaticon</a>
# <a href="https://www.flaticon.com/free-icons/id-card" title="id card icons">Id card icons created by Freepik - Flaticon</a>
# <a href="https://www.flaticon.com/free-icons/glasses" title="glasses icons">Glasses icons created by Freepik - Flaticon</a>

#root start
root=Tk()
root.title("ROOT WINDOW")
root.resizable()
root.iconbitmap("icons\school.png")
root.config(bg="blue")

#1st wijndow x 1st app
myFrame=Frame(root)
myFrame.pack(side="left")
myFrame.config(bg="red")
myFrame.config(width="650", height="350")
myFrame.config(bd="5")
myFrame.config(cursor="crosshair")
myFrame.config(highlightbackground="grey")
myFrame.config(relief="groove") 
myFrame.config(cursor="X_cursor")
Label(myFrame, text="APP1").place(x=5,y=5)
miImagen=PhotoImage(file="icons\calculator.png")
Label(myFrame, image=miImagen).place(x=50,y=5)
################Menu inside myFrame: ####################





#2st wijndow x 2st app
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

