Ethan Burchett Summer 2021

There are several programs in the folder. 

Company Indexing. 
	This python script recursively scans the sharedrive job files such as 
	"M,R:\Default\Path" and records both the directory name and the 
	path name of each job file, but excludes the majority of sub folders that don't 
	need to be searched. 

	ex: "B000000, C:\Pathname"
	(name, path) pair. 

	This script does not edit or change any information in any of the job folders 
	or any other file in the companyshare, except for internal files used by 
	this script and the front facing job searching GUI. 

	There is some optimization that I could do to potentially make it run faster, 
	ex: using different internal data storage, numpy array vs pandas dataframe. 

	This program writes (name, path) data to index.csv

	This program writes to time_log file, date of index, time script ran, how many new files
	it discovered.

	Goal: make this script run in 5 min and schedule it to run every 2 hours during
	the work day. 


Company Job Search GUI. 
	This is the front facing application for the users at Budinger. 
	Simply type in a job number(or close to the job num you want)
	and it will search an index already loaded in memory. If found, it will 
	display the job name/number and let the user open the job folder 
	in the windows explorer. 

	This mostly works and is relativity stable. I have searched several hundred
	job numbers and ~95% of them are functional. 

	This program reads (name, path) data from index.csv and has a simple user
	interface to search and open job folders. 
