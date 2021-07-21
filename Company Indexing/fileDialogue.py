

from tkinter import filedialog as fd
import tkinter as tk
import tkinter as ttk 


def get_path_name():
    root = tk.Tk()
    root.withdraw()
    filename = None
    try:
        filename = fd.askdirectory()
        root.destroy()
    except:
        print('Folder not opened')
        root.destroy()
    return filename

