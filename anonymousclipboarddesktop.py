from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def collect_file():
	print('file collect')

def submit_form():
	print('form submit')

def limit_id_length(*args):
	value = id_value.get()
	trimmed_value = value.replace(' ','')
	if len(value) > 8:
		id_value.set(trimmed_value[:8])
	print(id_value.get())

root = Tk()

id_value = StringVar()
id_value.trace('w', limit_id_length)
frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0,row=0,sticky=(N,W,E,S))

im = PhotoImage(file='logo.gif',)
fame_w = frame['width']
frame_h = frame['height']


im = im.subsample(9,9)
il = ttk.Label(frame, style='green/black.TLabel',image=im,text ='Anonymous Clipboard')

il['compound'] = TOP
il['anchor'] = CENTER
il['font']=('', 18)
il.grid(column=0,row=0, columnspan=2 ,sticky=(N,W,E,S))



text_entry = Text(frame)
text_entry.grid(column=0, row=1,columnspan=2, sticky=(W,E))

id_label = ttk.Label(frame, text = 'Enter Id:')
id_label.grid(column=0,row=3,sticky=(W,E))

id_entry = ttk.Entry(frame,textvariable=id_value)
id_entry.grid(column=0,row=3)

file_label = ttk.Label(frame, text='Enter File:')
file_button = ttk.Button(frame, text='Select File', command = collect_file)

file_button.grid(column=1, row=2,sticky=(W,E))


submit_button = ttk.Button(frame, text='Submit', command = submit_form)

submit_button.grid(column=1, row=3,sticky=(W,E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

root.mainloop()
