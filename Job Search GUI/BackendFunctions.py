import pandas as pd 
import numpy as np 
import subprocess
import os
#import searchPaths
import path_name_class

#This set of functions loads the JobSearch Path index from company server and makes it ready for searching 

def init_search_path():
    pathArr = pd.read_csv(r'C:\Users\EBurchett\Automation\JobSearchGUI\JobSearchGUI\out.csv', skip_blank_lines=True,error_bad_lines=False)
    pathArr = pathArr.to_numpy()

    return pathArr


def search_get_filepath(path_array, jobNum):
    
    
    pc = path_name_class.PathClass()
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






































# def search_paths(jobnum,pathArr):
#     path = 'NULL'

#     length = pathArr.size
#     i = 0
#     while i < length: 
#         #print(pathArr[i])
#         i = i + 1
#         #print(i)
#         #try:
#             #print(pathArr[i][0])
#         #except:
#             #print('error out of bounds')
        
#         try:
#             if jobnum in pathArr[i][0]:
#                 path = pathArr[i][1]
#                 break
#         except:
#             pass

        
#     print(path, jobnum)


#     return path