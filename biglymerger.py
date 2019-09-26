# Federico Tondolo
# Summer 2019 at the Columbia University Medical Center
import csv
import os
import subprocess

def main():
    # Prompt for Letter Number of Column
    print('Letter Number:')
    letter=input()
    # Variable to know whether to include header
    once=0
    # Interval time
    time_rate=0.050
    # Running time counter (i.e. clock)
    tim_counter=time_rate
    # List with all values of interest
    biglylist=[]
    # Loops for every file inside current dir
    for filename in sorted(os.listdir('.')):
        # If file is an asc file
        if (filename.endswith(".asc")):
           # Copy file and convert to txt
           subprocess.call(['cp', filename, (filename[:-4] + ".txt")])
           # Update filename variable
           filename=filename[:-4]+".txt"
           # Read text file and split by whitespace
           file = open(filename).read().split()
           # Set initial position to first actual value
           pos_counter=64
           # While not at end of file
           while (pos_counter<len(file)):
               # Append value of interest
               biglylist.append(file[pos_counter])
               # Update to proceed to next row
               pos_counter+=letter+43
               # Update time counter
               tim_counter+=time_rate
               # Round for sanity's sakes!
               round(tim_counter,3)
           # Remove unnecessary text file
           subprocess.call(['rm', filename])
        # If file is not asc
        else:
            continue
    # Write useful fata to CSV
    with open('merged.csv', mode='a') as csv_file:
                   # Header setup
                   fieldnames = ['time', 'value']
                   writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                   # Write header if first time around
                   if(once==0):
                       writer.writeheader()
                       once=1
                   # While loop which copies timestamp and value until biglylist is exhaused 
                   q=0
                   while (q<len(biglylist)):
                          writer.writerow({'time': round(time_rate*(q+1), 3), 'value': biglylist[q]})
                          q+=1

# Ya done
main()
