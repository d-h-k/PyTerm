import calendar
import tkinter
from tkinter import messagebox

calroot = tkinter.Tk()
#calframe = tkinter.Frame(calroot)

text = tkinter.Text(calroot,width = 80, height = 50)
text.pack()
text.insert("1.0",calendar.calendar(2019))
#text = tkinter.Text(calroot,title="calendar2019",detail = calendar.calendar(2019))
#calframe.pack()
calroot.mainloop()


