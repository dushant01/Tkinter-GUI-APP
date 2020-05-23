# -*- coding: utf-8 -*-
"""
Created on Sun May 24 02:11:57 2020

@author: HP
"""

import tkinter as tkr
import tkinter
 
tk = tkr.Tk()
canvas = tkr.Canvas(width=500, height=500)
canvas.grid()
label=tkinter.Label(tk,text="Login Form")
label.grid()
tk.title('Login')

#entering window

text=tkr.Entry(tk)
text.grid()


#add button inn GUI application

def but_msg():
    a=text.get()
    print('User said: {0}'.format(a))
    print("Button Clicked")
    
but=tkr.Button(tk,text="Click me",command=but_msg)
but.grid()

#check button


def result():
    a,b=var1.get(),var2.get()
    if a==1:
        print("Cricket selected")
    if b==1:
        print("Football selected")
var1=tkinter.IntVar()
var2=tkinter.IntVar()
check1=tkinter.Checkbutton(tk,text="Cricket",variable=var1,onvalue=1,offvalue=0,command=result)
check2=tkinter.Checkbutton(tk,text="Football",variable=var2,onvalue=1,offvalue=0,command=result)
check1.grid()
check2.grid()

#Radio Button

def select():
    print(var.get())
    
var=tkinter.StringVar()
radio=tkinter.Radiobutton(tk,text="Male",variable=var,value="Male",command=select)
radio2=tkinter.Radiobutton(tk,text="Female",variable=var,value="Female",command=select)

radio.grid()
radio2.grid()

# list

def button_message():
    top=tkinter.Tk()
    list1 = tkinter.Listbox(top)
    list1.insert(1, "Python")
    list1.insert(2, "java")
    list1.insert(3, "c#")
    list1.insert(4, "Machine Learning")
    list1.grid()
    a=text.get()
    print('User said: {0}'.format(a))
    top.mainloop()





tk.mainloop()


 




