from tkinter import *
from tkinter import ttk

def collect_file():
	print('file collect')

root = Tk()
frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0,row=0,sticky=(N,W,E,S))



data_label = ttk.Label(frame, text = 'Enter Data:')
data_label.grid(column=0,row=0,sticky=(W,E))

id_label = ttk.Label(frame, text = 'Enter Id:')
id_label.grid(column=0,row=1,sticky=(W,E))

file_button = ttk.Button(frame, text='Select File', command = collect_file)

file_button.grid(column=0, row=2,sticky=(W,E))


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

root.mainloop()