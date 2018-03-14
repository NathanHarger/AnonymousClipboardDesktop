from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import requests as r
def collect_file():
	filename = filedialog.askopenfilename()
	info.set(filename.split('/')[-1])
	print(filename)

def submit_file():
	print('form submit')

def submit_text():
	print('form submit')

def limit_id_length(*args):
	value = id_value.get()
	trimmed_value = value.replace(' ','')
	if len(value) > 8:
		id_value.set(trimmed_value[:8])
	print(id_value.get())

def dragged_document(*args):
	print("doc dragged")
def about_app():
	print("about app")
root = Tk()
root.title('Anonymous Clipboard')

menubar = Menu(root)


appmenu = Menu(menubar, name='apple')
appmenu.add_command(label='About My Application',command=about_app)
appmenu.add_separator()
menubar.add_cascade(menu=appmenu)

menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')

root.config(menu= menubar)

#windowmenu = Menu(menubar, name='window')
#menubar.add_cascade(menu=windowmenu, label='Window')




info = StringVar()
id_value = StringVar()
id_value.trace('w', limit_id_length)
frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0,row=0,sticky=(N,W,E,S))

im = PhotoImage(file='logo.gif',)
fame_w = frame['width']
frame_h = frame['height']


im = im.subsample(9,9)
il = ttk.Label(frame, image=im,text ='Anonymous Clipboard')

il['compound'] = TOP
il['anchor'] = CENTER
il['font']=('', 18)
il.grid(column=0,row=0, columnspan=4 ,sticky=(N,W,E,S))


text_entry = Text(frame)
text_entry.grid(column=0, row=1,columnspan=4, sticky=(W,E))



file_label = ttk.Label(frame, text='Enter File:')
file_button = ttk.Button(frame, text='Select File', command = collect_file)

file_button.grid(column=0, row=2,sticky=(W))

info_label = ttk.Label(frame, textvariable=info)
info_label.grid(column=1,row=2,sticky=(W))

submit_button = ttk.Button(frame, text='Submit Text', command = submit_text)

submit_button.grid(column=2, row=2,sticky=(E))

submitfile_button = ttk.Button(frame, text='Submit File', command = submit_file)

submitfile_button.grid(column=3, row=2,sticky=(E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

root.mainloop()
