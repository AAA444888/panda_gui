import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import addD
import deleteD
import queryD
import updateD
import os

wnd = tk.Tk()
wnd.geometry("400x400")
wnd.title("bmr database")

button = tk.Button(wnd,text="Add Data",underline=-1,command=addD.add)
button.place(relx=0.125,rely=0.7,anchor='n')
button = tk.Button(wnd,text="Delete Data",underline=-1,command=deleteD.delete)
button.place(relx=0.3625,rely=0.7,anchor='n')
button = tk.Button(wnd,text="Query Data",underline=-1,command=queryD.query)
button.place(relx=0.6,rely=0.7,anchor='n')
button = tk.Button(wnd,text="Update Data",underline=-1,command=updateD.update)
button.place(relx=0.85,rely=0.7,anchor='n')

close = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
close.place(relx=0.5,rely=0.9,anchor="n")

wnd.mainloop()