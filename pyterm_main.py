import tkinter
from tkinter import filedialog

mywind = tkinter.Tk()
mywind.geometry("500x300")

f = None

filepath = tkinter.StringVar()
filepath.set("filepath")

#1:#/1_1_openfile/1_2_savefile/1_3_savefile/1_4_exit
def f11_openfile():
	global f
	f = filedialog.askopenfile("rb")
	filepath.set(f.name)

def f12_savefile():
	global f
	a = f.read()
	if a is None:
		return
	else:
		save_f = filedialog.asksaveasfile("wb")
		print(save_f.name)
		filepath.set(save_f.name)
		save_f.write(a)
	f.close()
	save_f.close()

def f13_saasfile():
	print("f13_saasfile")

def f14_exit():
	print("f14_exit")
	mywind.quit()

#2:#/f21_font/f22_color/f23_style/f24_convention
def	f21_font():
	print("font")

def f22_color():
	print("color")

def f23_style():
	print("style")

def f24_convention():
	print("convention")

#3:#/f31_conserial/f32_contcpip/
def f31_conserial():
	print("")
def f32_contcpip():
	print("")


#4:#/f41_original/f42_project/f43_version/f44_donation/
def f41_original():
	print("")
def f42_project():
	print("")
def f43_version():
	print("")
def f44_donation():
	print("")

#5:#/f51_pyshoot/f52_pyTalk/f53_superpi/f54_pycalc/
def f51_pyshoot():
	print("")
def f52_pyTalk():
	print("")
def f53_superpi():
	print("")
def f54_pycalc():
	print("")




label_path = tkinter.Label(mywind, textvariable = filepath)
label_path.grid(row = 0, column = 0)

menubar = tkinter.Menu(mywind)
mywind['menu'] = menubar

#####################
#tab registration
menu_file = tkinter.Menu(menubar, tearoff = 0)
menu_edit = tkinter.Menu(menubar, tearoff = 0)
menu_config = tkinter.Menu(menubar, tearoff = 0)
menu_setting = tkinter.Menu(menubar, tearoff = 0)
menu_help = tkinter.Menu(menubar, tearoff = 0)
menu_amusement = tkinter.Menu(menubar, tearoff = 0)

#############################################################
#############################################################
#tab down registration
menubar.add_cascade(menu = menu_file, label = "File")
menubar.add_cascade(menu = menu_edit, label = "Edit")
menubar.add_cascade(menu = menu_config, label = "Config")
#menubar.add_cascade(menu = menu_setting, label = "Setting")
menubar.add_cascade(menu = menu_help, label = "Help")
menubar.add_cascade(menu = menu_amusement, label = "Amusement")
#############################################################
#############################################################


#tab down menu disp
##########################################################
######/ 1.file / 2.Edit / 3.Config / 4.Help / 5.Amusement
##########################################################
#1:#/1_1_openfile/1_2_savefile/1_3_savefile/1_4_exit
#2:#/f21_font/f22_color/f23_style/f24_convention
#3:#/f31_conserial/f32_contcpip/
#4:#/f41_original/f42_project/f43_version/f44_donation/
#5:#/f51_pyshoot/f52_pyTalk/f53_superpi/f54_pycalc/


################
#1.File tab down
menu_file.add_command(label = "Open", command = f11_openfile)
menu_file.add_command(label = "Save", command = f12_savefile)
menu_file.add_command(label = "Save as", command = f13_saasfile)
menu_file.add_command(label = "Exit", command = f14_exit)
#/f11_openfile/f12_savefile/f13_savefile/f14_exit


################
#2.Edit tab down
menu_edit.add_command(label = "Font", command = f21_font )
menu_edit.add_command(label = "Color", command = f22_color)
menu_edit.add_command(label = "Style", command = f23_style)
menu_edit.add_command(label = "Convention", command = f24_convention)
#/f21_font/f22_color/f23_style/f24_convention


################
#3.Config tab down
menu_config.add_command(label = "Config Serial", command = f31_conserial)
menu_config.add_command(label = "Config TCP/IP", command = f32_contcpip)
#/f31_conserial/f32_contcpip/


################
#4.Help tab down
menu_help.add_command(label = "Original From", command = f41_original)
menu_help.add_command(label = "Project Info", command = f42_project)
menu_help.add_command(label = "Version Info", command = f43_version)
menu_help.add_command(label = "Donation", command = f44_donation)
#/f41_original/f42_project/f43_version/f44_donation/

################
#5.Amusement tab down
menu_amusement.add_command(label = "Python game", command = f51_pyshoot)
menu_amusement.add_command(label = "Python Talk", command = f52_pyTalk)
menu_amusement.add_command(label = "Super PI", command = f53_superpi)
menu_amusement.add_command(label = "Python Calc", command = f54_pycalc)
#/f51_pyshoot/f52_pyTalk/f53_superpi/f54_pycalc/


mywind.mainloop()