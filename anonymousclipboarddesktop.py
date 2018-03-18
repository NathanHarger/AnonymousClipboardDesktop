from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import json

import requests

production_url = 'https://vast-chamber-77416.herokuapp.com'
test_url = 'http://localhost:8000'
def collect_file():
	global filename
	file = filedialog.askopenfilename()
	filename.set(file)

	info.set(file.split('/')[-1])
	print(file)

def submit_file():

	global filename,info_label
	info.set('')

	print('file submit')
	files = {'file': open(filename.get(), 'rb')}
	r = requests.post(production_url + "/api/clipboard/",files=files, data={'media_type':1})
	json = r.json()
	info.set(json['id'])

def submit_text():
	global text_entry,info_label
	text = text_entry.get("1.0",END)
	r = requests.post(production_url + "/api/clipboard/",data = { 'text' :text, 'media_type':0})
	json = r.json()
	info.set(json['id'])

def get_data():
	global text_entry,id_value,root

	print("get data")

	r = requests.get(production_url + "/api/clipboard/getMetadata/",params={'session_id': id_value.get()})
	metadata = r.json() 


	if('media_type' not in metadata):
		messagebox.showwarning(message="The id is invalid",detail="The data has already been retrieved or the id is incorrect.")
	else:
		print(metadata)
		if(metadata['media_type'] == "Text"):
			r = requests.get(production_url + "/api/clipboard/getData/",params={'session_id': id_value.get()})

			print("text")
			text_entry.delete(1.0, END)

			text_entry.insert(END,r.json()['data'])

		elif metadata['media_type'] == 'File':

			
			print(r.content)

			filename = filedialog.asksaveasfilename(initialfile=metadata['FileMetaData']['file_name'])

			file = open(filename,'wb')

			if r.encoding is None:
				r.encoding = 'utf-8'

			data = requests.get(production_url + "/api/clipboard/getData/",params={'session_id': id_value.get()},stream=True)
			print(data.content)

			file.write(data.content)

			file.close()
			#xFileDownload(response.data, metadata.FileMetaData['file_name']);
		  
	   


def limit_id_length(*args):
	value = id_value.get()
	trimmed_value = value.replace(' ','')
	if len(value) > 8:
		id_value.set(trimmed_value[:8])
	print(id_value.get())

def about_app():
	global root,im
	about_app_window = Toplevel(root)
	about_app_window.resizable(0, 0)

	il = ttk.Label(about_app_window, image=im,text ='Anonymous Clipboard',font=('',18),compound=TOP)
	il.grid()
	ttk.Label(about_app_window, font=("",10),text="Copyright © 2018 Nathan Harger").grid(sticky=(N,S,E,W))

def collect_id():
	global root
	collect_id_window = Toplevel(root)
	collect_id_window.resizable(0, 0)
	ttk.Label(collect_id_window,text="Enter Id:").grid(sticky=(N,S,E,W))
	ttk.Entry(collect_id_window,textvariable=id_value).grid(column=1,row=0)
	ttk.Button(collect_id_window,text="Submit",command=get_data).grid(column=2,row=0)

	


root = Tk()
root.title('Anonymous Clipboard')
root.option_add('*tearOff', FALSE)

filename = StringVar()

menubar = Menu(root)

windowsystem = root.tk.call('tk', 'windowingsystem')
if windowsystem == 'aqua':
	appmenu = Menu(menubar, name='apple')
	appmenu.add_command(label='About Anonymous Clipboard',command=about_app)
	appmenu.add_separator()
	menubar.add_cascade(menu=appmenu)
	windowmenu = Menu(menubar, name='window')
	menubar.add_cascade(menu=windowmenu, label='Window')
		
menu_file = Menu(menubar)
menu_file.add_command(label='Get Data', command=collect_id)
menubar.add_cascade(menu=menu_file,label='File')

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
il = ttk.Label(frame, image=im,text ='Anonymous Clipboard',font=('',18),compound=TOP)

il['anchor'] = CENTER
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
