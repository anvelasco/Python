from tkinter import *
from PIL import ImageTk, Image

window = Tk()
name = Label(
    window,text='PythonX - Learn Python',
    bg='white',
    fg='Blue',
    font=('Serif',16)
    )
img = Image.open('python.png')
logo = ImageTk.PhotoImage(img)
image = Label(window,image=logo)
button = Button(window,text='Let us start')

username = Label(
    window,text='Username',
    font=('Serif,12'))
inputBox = Entry(window)

name.pack()
image.pack()
username.pack(side=LEFT)
inputBox.pack(side=RIGHT)
button.place(x=300,y=670)
window.mainloop()