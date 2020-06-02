# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 10:45:40 2020

@author: HP
"""


import tkinter as tk
from tkinter import ttk

window= tk.Tk()
window.title('loop')

label= ['what is your name', 'what is your age', 'what is your city']


''' name_label= ttk.Label(window, text="Enter your name")
name_label.grid(row=0,column=0,sticky=tk.W) ''' #coppy this and pste in a for loop

for i in range(len(label)):
    cur_label= 'label' + str(i) # label0,label1.... no need of this line
    cur_label= ttk.Label(window, text= label[i])
    cur_label.grid(row=i, column=0, padx=50,pady=0)

name_var= tk.StringVar()
name_info= {
    'Name' : tk.StringVar(),
    'Age' : tk.StringVar(),
    'City' : tk.StringVar() }

counter=0
   
for i in name_info:
    
    cur_entrybox= 'entry' + i
    cur_entrybox= tk.Entry(window, width= 16, textvariable= name_info[i])
    cur_entrybox.grid(column=1, row= counter,padx=50,pady=0)
    counter += 1
    
def submit():
    print(name_info.get('Name').get())
    print(name_info.get('Age').get())
    print(name_info['City'].get())
    
Submit_btn= ttk.Button(window,text="submit", command=submit)
Submit_btn.grid()    
    
window.mainloop()