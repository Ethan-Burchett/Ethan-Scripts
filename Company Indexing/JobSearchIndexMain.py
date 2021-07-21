#-----------------------------------------------------------#
# Ethan Burchett 2021
# IndexMain.py 
# This is the main wrapper to index the company and save it as an an accessable csv file.
# it uses pandas to deal with all of the tabular and data formatting issues. 
#-----------------------------------------------------------#

import pandas as pd 
import numpy as np 
import ClassPathName
import fileDialogue

import os 


# tuple = ("name", "path")
    
#     pn = ClassPathName.PathClass()
    
#     column_names = ["name","path"]

#     fnames_df = pd.DataFrame(columns=column_names)
#     print(fnames_df)

#     list = []



def get_directory_names(root_dir): # root directory
    #print('getting directory names')
    
    list = []
    for root, dirs, files in os.walk(root_dir):
        for name in dirs:
            #print(name)
            #print(os.path.join(root, name))
            #pn.folder_string = name
            #pn.path_string = os.path.join(root, name)

            if type == name[0] or type == name[0:2]:  # will only add names to tuple if they are the right job number
                tuple = (name, os.path.join(root, name))
                list.append(tuple)
            #$list.append(pn)
            
        #for name in dirs:
           # print(os.path.join(root, name))
        
        #print(list)
    
    return list

  
    

df = pd.DataFrame()

column_names = ["name","path"]

entry_path = pd.read_csv('job_folder_path_entry.csv', skip_blank_lines=True,error_bad_lines=False)
nparr = entry_path.to_numpy()

global  job_type


#print(entry_path)

for x in range(len(nparr)):
     path = nparr[x][1]
     print(path)

     type = nparr[x][0]
     print(type)
     oneJobType_list = get_directory_names(path)

#     
#     fnames_df = pd.DataFrame(columns=column_names)


     tdf = pd.DataFrame(oneJobType_list)

     df = df.append(tdf)

#     #print(tdf)
# #pd.info(tdf)
# #fnames_df.append(oneJobType_list)

#print(fnames_df)

#print(df)

column_names = ["name","path"]
df.to_csv('out.csv', index = False, quotechar='"',header=column_names)


