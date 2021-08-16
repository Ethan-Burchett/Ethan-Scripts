This set of functions will periodically index the company server, collect all of the 
file names and prepare them for searching. 
The file folder searching can be done every few hours. 

This function will have two options, one to index just job folders
this is spec by csv file that has list of main job folders. 

The other option is to index every folder in the company. This takes much longer 
and will be slow to search. Only do this once every day as it will take around an hour. 


JobSearchIndexMain: 
    This program will run on the company server and be stored in a file called Ethan scripts in Admin/computer+phone


    This will recursively traverse through the spec directories and save the directory 
    file name and the path name as a string. 
    It will then place that into a pandas dataframe, sort, clean, deduplicate and 
    then export that to a csv file for future reading by JobSearchGUI