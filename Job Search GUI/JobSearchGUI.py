#-----------------------------------------------------------#
# Ethan Burchett Summer 2021
# GUI application for job searching. This replaces the autohotkey script that does the same thing. 

import subprocess
import os
from tkinter.constants import COMMAND
from typing_extensions import IntVar

import path_name_class
import BackendFunctions
import tkinter as tk 
import tkinter as ttk

#-----------------------------------------------------------#
class Data:
    def __init__(self) -> None:
        self.job_num_var = tk.StringVar()
        self.path = tk.StringVar()
        self.int_auto_open = tk.IntVar()
        self.job_label_name = tk.StringVar()
        self.path_array = BackendFunctions.init_search_path() #loads paths from .csv file
        self.path_2 = str()
#-----------------------------------------------------------#
       
# open directory in explorer spec by path 
#-----------------------------------------------------------#
def explore(path):
    # explorer would choke on forward slashes
    path = os.path.normpath(path)
    #print('path:', path )
    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
#-----------------------------------------------------------#


#-----------------------------------------------------------#
def geometry():
    searchButton.grid(row=0, column=1)
    #generalSearchB.grid(row=0,column=2)
    searchField.grid(row=0,column=0)
    openBut.grid(row=0,column=2)
    checkButton.grid(row=1,column=1)

    JobNameLabel.grid(row=2,column=2)
#-----------------------------------------------------------#

#-----------------------------------------------------------#
global pc
pc = path_name_class.PathClass()
pc.path_string = 'NULL'

#init system
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

#init root
gui = tk.Tk(className=' Job Directory Search')
gui.geometry("510x315")

global d 
d = Data() # init class
d.int_auto_open.set(0)

frame = tk.Frame(gui, padx = 0,pady = 30)
frame2 = tk.Frame(gui, padx = 10,pady = 30)
#-----------------------------------------------------------#

#Buttons
#-----------------------------------------------------------#
def searchButtonPress():   #1 reads user input -> sends to formatter -> sends f_jobNum to search function
                           # -> returns job path, prints job path and job name
    global pc                      # if auto.open -> open job folder, else, just print. 
    jobNum = d.job_num_var.get()

    if jobNum:
        jobNum = jobNum.upper()
        pc = BackendFunctions.search_get_filepath(d.path_array,jobNum)
        #print('path in search button:', pc.path_string)
        #print('Name: ', pc.folder_string)
        if d.int_auto_open.get(): # if auto.open true
            openFile()

        if pc.path_string == 'NULL':
            JobNameLabel.config(text='Job Not Found')
        else:
            JobNameLabel.config(text=pc.folder_string)
#-----------------------------------------------------------#

        
#-----------------------------------------------------------#
def GeneralSearchButtonPress():
    print('General Button press')
    name = d.job_num_var.get()
    print('General search value: ', name)
#-----------------------------------------------------------#


#-----------------------------------------------------------#
def openFile():
    #print('opening:',pc.folder_string )
    #print('path in openFile:', pc.path_string) 
    if pc.path_string == 'NULL':
        pass
        #print('File not found')
    if pc.path_string != 'NULL':
        try:
            explore(pc.path_string)
        except:
            pass
            #print('unable to explore file')
#-----------------------------------------------------------#


#-----------------------------------------------------------#
#BUTTON DEFINITION 
searchButton = ttk.Button(frame, text='Job Search', width=15, height=2, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa',command=searchButtonPress)

generalSearchB = ttk.Button(frame, text='General Search', width=15, height=2, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa',command=GeneralSearchButtonPress)

searchField = tk.Entry(frame, bd =5,textvariable= d.job_num_var, font=('Verdana',15))

openBut = tk.Button(frame, text='Open', width=15, height=2, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa',command=openFile) 

checkButton = tk.Checkbutton(frame,text='Open on Search', variable=d.int_auto_open)

JobNameLabel = tk.Label(frame2, text = 'Job Name',font=('Verdana',13))
#-----------------------------------------------------------#

#-----------------------------------------------------------#
geometry()

frame.pack()
frame2.pack()

gui.mainloop() 
#-----------------------------------------------------------#
