# Federico Tondolo
# Summer 2019 at the Columbia University Medical Center
import csv
import os
import subprocess

def main():
    print('Letter #:')
    letter=input()
    once=0
    tim_counter=0.050
    biglylist=[]
    # Loops for every file inside current dir
    for filename in sorted(os.listdir('.')):
        # If file is a video file
        if (filename.endswith(".asc")):
           subprocess.call(['cp', filename, (filename[:-4] + ".txt")])
           filename=filename[:-4]+".txt"
           file = open(filename).read().split()
           pos_counter=64
           while (pos_counter<len(file)):
               biglylist.append(file[pos_counter])
               pos_counter+=letter+43
               tim_counter+=0.05
               round(tim_counter,3)
           subprocess.call(['rm', filename])
        # If file is not a video
        else:
            continue
    with open('merged.csv', mode='w') as csv_file:
                   fieldnames = ['time', 'value']
                   writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                   if(once==0):
                       writer.writeheader()
                       once=1
                   q=0
                   while (q<len(biglylist)):
                          writer.writerow({'time': round(0.05*(q+1), 3), 'value': biglylist[q]})
                          q+=1

main()
