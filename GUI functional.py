from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


#Command method example
"""def gui():

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

    frame = Frame(window)
    username = Label(
        window,text='Username',
        font=('Serif,12'))
    inputBox = Entry(frame)
    button = Button(window,
                text='Let us start',
                command=showMessage)

    name.pack()
    image.pack()
    frame.pack()
    username.pack(side=LEFT)
    inputBox.pack(side=RIGHT)
    button.pack(side=BOTTOM)
    window.mainloop()

def showMessage():
    messagebox.showinfo('PythonX - Learn Python','Welcome')

if __name__ == '__main__':
    gui()"""


#Bind method example
def greetUser(event):
    username = inputBox.get()
    greet['text'] = 'Welcome'+username

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

frame = Frame(window)
username = Label(
        window,text='Username',
        font=('Serif,12'))
inputBox = Entry(frame)
button = Button(window,
                text='Let us start')
button.bind('<Button-1>',greetUser)
greet = Label(window)

name.pack()
image.pack()
frame.pack()
username.pack(side=LEFT)
inputBox.pack(side=RIGHT)
button.pack(side=BOTTOM)
greet.pack()
window.mainloop()