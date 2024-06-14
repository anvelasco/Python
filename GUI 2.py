from tkinter import *

window = Tk()

#Button example
"""frame = Frame(window)
lbl = Label(frame,text='Inside the frame')
btn = Button(frame,text='Inside the frame')
frame.pack()
lbl.pack(side=TOP)
btn.pack(side=BOTTOM)
window.mainloop()"""

#Check Button example
"""lbl =Label(window,text='Choose your favorite programing languages:')
frame = Frame(window)
python = Checkbutton(frame,text='Python')
java = Checkbutton(frame,text='Java')
js = Checkbutton(frame,text='JavaScrtipt')
cpp = Checkbutton(frame,text='C++')

lbl.pack()
frame.pack()
python.pack()
java.pack()
js.pack()
cpp.pack()

window.mainloop()"""

#Radio Button example
lbl = Label(window,text='Gender')
var = StringVar()
male = Radiobutton(window,
                   text='Male',
                   variable=var,
                   value='M')
female = Radiobutton(window,
                   text='Female',
                   variable=var,
                   value='F')
lbl.pack()
male.pack()
female.pack()

window.mainloop()