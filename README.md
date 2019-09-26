# BiglyMerger
Program created with the purpose of merging a number of .ASC files into a single .CSV file.  More specifically, when the code is run and a specific column is selected, the program concatenates all the values into a single excel column with a corresponding timestamp for each value following a +0.05s rule across all .ASC files in its directory following an alphabetical order.  The program works on every single file of the aforementioned format by first converting it into a .TXT file and then reading it at which point the intermediary text file is deleted.


## Notice
Due to the naming structure, __it is necessary that there are no files with the same filenames as the .ASC files but with .TXT extensions as these files must be createed by the program__. Moreover, __this program was designed to work solely with a very specific .ASC file format, if you wish to use it you will have to make modifications__. Spaces in filenames are allowed!<br>

## Windows Install
_Administrator Privileges Required_
1) Download and install all of the following files **in the order in which they appear:**<br>
    - Visual Studio 2019 : https://aka.ms/vs/16/release/vc_redist.x64.exe<br>
    - Python 3.7.3 : https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe<br> 
      > Custom->Next->Add Python to environment variables
2) Download biglymerger.py and position it in a folder with all of the .ASC files you want examined<br>
3) Open biglymerger.py in IDLE (Python 3.7 64-bit)
   > File->Open...
  
4) Run biglymerger.py
    > Run->Run Module
   
5) Wait for completion, should be practically instantaneous <br>
**DO NOT MANIPULATE THE FILE STRUCTURE UNTIL THE PROGRAM FINISHES**


## Debian Install
_Administrator Privileges Required_
1) Download biglymerger.py and position it in a folder with all of the .ASC files you want examined<br>
3) Open a Terminal window and navigate to the directory which you have selected
   > `cd /...`
  
4) Run biglymerger.py
    > `python biglymerger.py`
  
5) Wait for completion, should be practically instantaneous <br>
**DO NOT MANIPULATE THE FILE STRUCTURE OR THE TERMINAL WINDOW UNTIL THE PROGRAM FINISHES**<br>
