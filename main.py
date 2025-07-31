import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

# Function Area Start

def open_file_with_s(o):
    file_path = filedialog.askopenfile(defaultextension='.txt',
                                filetypes=[
                                    ('Text File','.txt'),
                                    ('Html File','.html'),
                                    ('All Files','*.*')
                                ])
    fileData = file_path.read()
    textArea.delete(1.0, 'end')
    textArea.insert(1.0, fileData)
    app.title(f"File Open: {file_path.name}")

def open_file():
    file_path = filedialog.askopenfile(defaultextension='.txt',
                                filetypes=[
                                    ('Text File','.txt'),
                                    ('Html File','.html'),
                                    ('All Files','*.*')
                                ])
    fileData = file_path.read()
    textArea.delete(1.0, 'end')
    textArea.insert(1.0, fileData)
    app.title(f"File Open: {file_path.name}")

def save_file_with_s(s):
    data = textArea.get(1.0 , 'end')
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ('Text File', '.txt'),
                                        ('Html File', '.html'),
                                        ('All Files', '*.*')
                                    ])
    file.write(data)
    file.close()

def save_file():
    data = textArea.get(1.0 , 'end')
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ('Text File', '.txt'),
                                        ('Html File', '.html'),
                                        ('All Files', '*.*')
                                    ])
    file.write(data)
    file.close()


def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    textArea.event_generate(("<<Paste>>"))


def About_Developer():
    messagebox.showinfo(title="About Developer", message="This Notepad Application Made by Ayush Developer as a Tkinter First Project | GitHub : @user-synax")

def ExitApp():
    app.destroy()

# Functions Area End
app = tk.Tk()
app.title('Notepad | By Ayush')

textArea = tk.Text(app, font=('Arial', 21))
textArea.pack(expand=True, fill=BOTH)

open_img = tk.PhotoImage(file='F:/Python GUI Apps/NotePad/Assets/folder.png')
save_img = tk.PhotoImage(file='F:/Python GUI Apps/NotePad/Assets/diskette.png')
close_img = tk.PhotoImage(file='F:/Python GUI Apps/NotePad/Assets/close.png')

# Menu Bar
menuBar = tk.Menu(app)
app.config(menu=menuBar)
app.geometry('1000x500')

# File Manu
fileMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File',menu=fileMenu)

fileMenu.add_command(label='Open',command=open_file, image=open_img, compound='left')
fileMenu.add_command(label='Save',command=save_file, image=save_img, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=ExitApp, image=close_img, compound='left')

# Edit Menu
editMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy',  command=copy)
editMenu.add_command(label='Paste', command=paste)

# Help Menu
helpMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label="About", command=About_Developer)

# Scroll Bar
scroll = tk.Scrollbar(textArea)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=textArea.yview)
textArea.config(yscrollcommand=scroll.set)

# Keyboard Shortcut Keys Area
app.bind('<Control-s>', save_file_with_s)
app.bind('<Control-o>', open_file_with_s)


app.mainloop()