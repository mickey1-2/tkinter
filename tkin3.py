from tkinter import *
from PIL import Image, ImageTK
root=Tk()
root.title('image')
root.geometry('400x400')
upload=image.open("c:/Users/shali/OneDrive/Pictures/duck.png")
image=ImageTK.PhotoImage(upload)
label=Label(root,image=image,height=350,width=300)
label.place(x=50,y=0)
root.mainloop()
