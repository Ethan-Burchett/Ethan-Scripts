#-----------------------------------------------------------#
# Ethan Burchett Summer 2021
# GUI application for job searching. This replaces the autohotkey script that does the same thing. 

import json
import subprocess
import os
from tkinter.constants import BOTTOM, COMMAND
from typing_extensions import IntVar


import BackendFunctions
import tkinter as tk 
import tkinter as ttk
from tkinter import simpledialog
from datetime import datetime
import webhook as wh

#-----------------------------------------------------------#
class PathClass:
    path_string = str()
    folder_string = str()
#-----------------------------------------------------------#

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
    searchField.grid(row=0,column=0)
    openBut.grid(row=0,column=2)
    checkButton.grid(row=1,column=1)

    JobNameLabel.grid(row=1,column=1)
    bugReportButton.grid(row=3,column=2)
    reInitIndexButton.grid(row=4,column=2)
    infoButton.grid(row=5,column=2)

    frame.pack()
    frame2.pack()       
#-----------------------------------------------------------#


#-----------------------------------------------------------#
zap_hook_url = 'https://hooks.zapier.com/hooks/catch/dummy/'

def bug_report_webhook():
    global pc    
    now = datetime.now()

    answer = simpledialog.askstring("Input", "Please Describe Issue") # returns None if either cancel or if no entry AND ok
    print(answer)

    if answer:
        dictionary = {"Date": now.strftime("%m/%d/%Y, %H:%M"), "SearchValue": d.job_num_var.get(), "DirName": pc.folder_string, "Path": pc.path_string, "Comment": answer }
        print('bug report')
        print(dictionary)

        json_object = json.dumps(dictionary, indent = 4)  

        print(json_object)
        # what data forms do I need?  name, path, comment
        hook = wh.Webhook(json_object,zap_hook_url)
        hook.postRequest()
        JobNameLabel.config(text='thanks for the feedback')
#-----------------------------------------------------------#


#-----------------------------------------------------------#
global pc
pc = PathClass()
pc.path_string = 'NULL'

#init system
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

#init root
gui = tk.Tk(className=' Job Directory Search')
#gui.geometry("510x315")    # this works!
gui.geometry("520x321")

global d 
d = Data() # init class
d.int_auto_open.set(0)

frame = tk.Frame(gui, padx = 0,pady = 15)
frame2 = tk.Frame(gui, padx = 10,pady = 0)
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
def reInitButtonPress():
    d.path_array = BackendFunctions.init_search_path() 
    JobNameLabel.config(text='Index Reloaded')
#-----------------------------------------------------------#

#-----------------------------------------------------------#
def infoPress():
    info_text = "\
Search: search company for job folder\n\
Open: open folder in windows explorer\n\
Report Issue: sends a bug report\n\
Reload Index: allows searching for new jobs "
    JobNameLabel.config(text=info_text, justify=tk.LEFT) 
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

bugReportButton = tk.Button(frame, text='Report Issue', width=10, height=1, bg='#83a3d4', fg='#ffffff', activebackground='#83a3d4', activeforeground='#aaffaa',command=bug_report_webhook) 

JobNameLabel = tk.Label(frame2, text = 'Job Name',font=('Verdana',13))

reInitIndexButton = tk.Button(frame, text='Reload Index', width=10, height=1, bg='#83a3d4', fg='#ffffff', activebackground='#83a3d4', activeforeground='#aaffaa',command=reInitButtonPress) 

infoButton =  tk.Button(frame, text='Info', width=10, height=1, bg='#83a3d4', fg='#ffffff', activebackground='#83a3d4', activeforeground='#aaffaa',command=infoPress) 
#-----------------------------------------------------------#


#-----------------------------------------------------------#
geometry()

gui.mainloop() 
#-----------------------------------------------------------#
