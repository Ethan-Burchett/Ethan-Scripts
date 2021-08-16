import pandas as pd 
import numpy as np 
import subprocess
import os
#import searchPaths
#import path_name_class

#-----------------------------------------------------------#
class PathClass:
    path_string = str()
    folder_string = str()
#-----------------------------------------------------------#

#This set of functions loads the JobSearch Path index from company server and makes it ready for searching 
def init_search_path():
    pathArr = pd.read_csv(r'R:\Administrative\Computer & Phone Systems\Ethan Scripts\index.csv', skip_blank_lines=True,error_bad_lines=False)
    pathArr = pathArr.to_numpy()

    return pathArr

#searches folder list with job num and returns the path if found
def search_get_filepath(path_array, jobNum):
    
    pc = PathClass()
    pc.path_string = 'NULL'

    length = path_array.size
    i = 1
    found = False
    while i < length:
        i = i + 1

        try:
            if jobNum in path_array[i][0]:
                pc.path_string = path_array[i][1]
                pc.folder_string = path_array[i][0]
                found = True
                break
        except:
            found=False
            #print('Job not found')

    if not found:
        print('Not found')  
    return pc
