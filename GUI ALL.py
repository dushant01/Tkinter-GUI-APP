# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 23:37:49 2020

@author: HP
"""


# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 10:16:47 2020

@author: HP
"""

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Login Form')

# create lables
#----- widets,button,radio button --- tk or ttk

#creating label for first name

first_name=ttk.Label(window,text='Enter your first name:- ') 
first_name.grid(row=0, column=0, sticky=tk.W) #tk.W means left side W mean west

#entry box

first_var= tk.StringVar() #we made a varile to store name
first_entrybox= ttk.Entry(window, width= 18, textvariable= first_var)
first_entrybox.grid(row=0, column=1)
first_entrybox.focus()

# creating label for last name

last_name= ttk.Label(window,text='Enter your last name:-')
last_name.grid(row=6, column=0, sticky=tk.W)

last_var= tk.StringVar()
last_entrybox= ttk.Entry(window, width= 18, textvariable= last_var)
last_entrybox.grid(row=6, column=1)

#creating a lable for countries and combobox

country_var= tk.StringVar()
country_select= ttk.Label(window, text= "Please select your country:-")
country_select.grid(row=7, column=0)

#comobo box gender

country_custom = ttk.Combobox(window, width= 16, state='readonly',textvariable= country_var) #state we have to define to tell we can only select
country_custom['values']= ('India', 'USA','Nepal','Africa','Sri lanka', 'Pakistan', 'UK','others')
country_custom.current(0) #it will help to cover up the empty part and print Male its position is 0
country_custom.grid(row=7,column=1)

# Radio Button

# defining Labels
gender_select=ttk.Label(window, text="Please select your gender:-")
gender_select.grid(row=8,column=0)

#creating radio

gender_var= tk.StringVar()
gender_radio=ttk.Radiobutton(window, text='Male', value ='Male', variable=gender_var)
gender_radio.grid(row=8 , column=1)

gender_radio=ttk.Radiobutton(window, text='Female', value ='Female', variable=gender_var)
gender_radio.grid(row=8 , column=2)

# creating a check button
check_var=tk.IntVar()
checkbtn= ttk.Checkbutton(window, text='Do you want to subscribe this channel for new updates', variable=check_var)
checkbtn.grid(row=9, columnspan=3) #cloum span is used to stop overridig the size of all rows

# create a button

def action():
    first= first_var.get()
    last=last_var.get()
    print(f'Your first name is {first} and last is {last}') #formating in print
    country= country_var.get()
    gender= gender_var.get()
    if check_var.get()== 0:
        Subscribed = 'NO'
    else:
        Subscribed = 'YES'
    print(f'You are from {country} and your\'re is  {gender} and you subcribed to chaneel{Subscribed}' )

    # creating a file and store files in that

    with open('file.txt', 'a') as F:
        F.write(f'{first}, {last}, {country}, {gender}, {Subscribed}\n')
   
    ''' # how to write in CSV
    
    from csv import DictWriter
    import os
    with open('file.csv', 'a',newline=''# for spacing) as f:
        dict_writer= DictWriter(f,fieldnames=['First Name','Last Name', 'Country', 'Gender'
                                              , 'subscribed'])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'First Name': first,
            'Last Name': last,
            'Country': country,
            'Gender': gender,
            'subscribed': Subscribed}) '''

    # it will clear the filed after submit 
            
    first_entrybox.delete(0, tk.END)
    last_entrybox.delete(0, tk.END)
 
# final submit cbutton
   
first_button= ttk.Button(window, text='Submit', command= action)
first_button.grid()


window.mainloop() # **** very import *******
 