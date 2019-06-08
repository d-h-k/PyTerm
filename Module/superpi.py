'''
import tkinter
win = tkinter.Tk()
win.geometry("{}x{}".format(300,250)

bt = tkinter.Button(win,text = "Quit")
bt.grid(row=0,column=2)
#lb_test = tkinter.Label(win, text="label Create")
lb_test = tkinter.Label(win, text="label Create")
lb_test.grid(row=0, column=1)
win.mainloop()
'''
'''
import tkinter
def change_bg():
	btn.configure(background = "green")
mywin = tkinter.Tk()
mywin.geometry("{}x{}".format(200,200))
frame_up = tkinter.Frame(mywin, height = 60, width = 90, background = "blue")
frame_down = tkinter.Frame(mywin, height = 30, width = 90, background = "red")
frame_up.pack()
frame_down.pack()
btn = tkinter.Button(frame_down, text = "click", command = change_bg,
foreground = "white", background = "black",
activeforeground = "blue",
activebackground = "#FF007F")
btn.pack()
mywin.mainloop()
'''
import tkinter

def f_comport():
	v_comport.set(v_comport.get()+1)

def f_baud():
	number.set(number.get()+100)
def f_dbit():
	v_dbit.set(v_dbit.get()+2)

def f_sbit():
	v_sbit.set(v_sbit.get()+1)

def f_okbtn():
	print("data saved and serial ComPort setting")

def f_ccbtn():
	print("shut down cc btn")

mywin = tkinter.Tk()
mywin.geometry("200x300")

frame = tkinter.Frame(mywin)
frame.pack()


v_comport = tkinter.IntVar(value = 0)
#
button1 = tkinter.Button(frame, text = "ComPort", command = f_comport)
button1.pack()
#
label1 = tkinter.Label(frame, text = "start", textvariable = v_comport)
label1.pack()



number = tkinter.IntVar(value = 0)
#
button1 = tkinter.Button(frame, text = "baud rate", command = f_baud)
button1.pack()
#
label1 = tkinter.Label(frame, text = "start", textvariable = number)
label1.pack()




v_dbit = tkinter.IntVar(value = 0)
#
button2 = tkinter.Button(frame, text = "data bit", command = f_dbit)
button2.pack()
#
label2 = tkinter.Label(frame, text = "start", textvariable = v_dbit)
label2.pack()


v_sbit = tkinter.IntVar(value = 0)
#
button2 = tkinter.Button(frame, text = "Stop bit", command = f_sbit)
button2.pack()
#
label2 = tkinter.Label(frame, text = "start", textvariable = v_sbit)
label2.pack()

ok_btn =  tkinter.Button(frame,text = "OK",command = f_okbtn)
ok_btn.pack()

cc_btn =  tkinter.Button(frame,text = "cancel",command = f_ccbtn)
cc_btn.pack()

mywin.mainloop()