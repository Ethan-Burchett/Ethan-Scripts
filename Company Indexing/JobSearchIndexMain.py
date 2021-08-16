#-----------------------------------------------------------#
# Ethan Burchett 2021
# IndexMain.py 
# This is the main wrapper to index the company and save it as an an accessable csv file. -> saves to index.csv
# it uses pandas to deal with all of the tabular and data formatting issues. 
#-----------------------------------------------------------#

import pandas as pd 
import numpy as np 
import TimeLog
import os 

timer = TimeLog.TimeLog()

timer.start()

def get_directory_names(root_dir): # root directory
    list = []
    for root, dirs, files in os.walk(root_dir):
        for name in dirs:
            
            if type == name[0] or type == name[0:2]:  # will only add names to tuple if they are the right job number
                tuple = (name, os.path.join(root, name))
                list.append(tuple)
          
    return list

df = pd.DataFrame()

column_names = ["name","path"]

entry_path = pd.read_csv('R:\Administrative\Computer & Phone Systems\Ethan Scripts\Company Indexing\entry_path_job_folder.csv', skip_blank_lines=True,error_bad_lines=False)
entry_path_np = entry_path.to_numpy()

#loops through each directory in entry_path
for x in range(len(entry_path_np)):
    
    path = entry_path_np[x][1]
    print(path)

    type = entry_path_np[x][0]

    oneJobType_list = get_directory_names(path)
    
    tdf = pd.DataFrame(oneJobType_list)

    df = df.append(tdf)
    
column_names = ["name","path"]
df.to_csv('R:\Administrative\Computer & Phone Systems\Ethan Scripts\index.csv', index = False, quotechar='"',header=column_names)

timer.end()

timer.write_log()
