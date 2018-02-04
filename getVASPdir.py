#User Inputs
compound_name = "PdO2" 

elementlist = ["Pd","O"] #List the elements in quotes seperated by commas in the order you want them for the POTCAR

ENCUTfactor = 1.3 #Use 1.3 times the highest ENMAX from the individual POTCARS for ENCUT in the INCAR

#Don't change anything below this line

import os
from shutil import copyfile
import csv

csvfile = csv.reader(open(r'D:/Dropbox/Python/test/ele_POTCAR.csv'))
ele_POTCAR = dict(csvfile)  #Element symbol and corresponding POTCAR dictionary   

ENCUT = []
POTCAR = []

for i in elementlist:
    infile = r'D:/Dropbox/DFT/potpaw_default/%s' % (ele_POTCAR[i])    
    raw = []
    with open( infile , 'r' ) as f:
        for line in f:
            raw.append( line )
    for r in raw:
        if 'ENMAX' in r:
            ENCUT.append(float(r.split()[2].strip(";")) * ENCUTfactor)  #Finding the ENMAX in the POTCAR to later set ENCUT in INCAR
        POTCAR.append(r)

with open(r'D:/Dropbox/Python/test/INCAR', 'r') as f:  #Reading sample INCAR and changing ENCUT
    INCAR = f.readlines()
    INCAR[1] = 'ENCUT= %s\n' % (max(ENCUT)) #Changing ENCUT to desired value

newpath = r'D:/Dropbox/Python/test/%s' % (compound_name) 

if not os.path.exists(newpath):  #Makes a directory of your compound name and copies the POTCAR and sample INCAR, job, and KPOINT files
    os.makedirs(newpath)
    copyfile(r'D:/Dropbox/Python/test/KPOINTS',r'D:/Dropbox/Python/test/%s/KPOINTS' % (compound_name))
    copyfile(r'D:/Dropbox/Python/test/job-test_opt',r'D:/Dropbox/Python/test/%s/job-%s_opt' % (compound_name, compound_name))
    with open(r'D:/Dropbox/Python/test/%s/INCAR' % (compound_name), 'w' ) as f:
        for item in INCAR:
            f.write("%s" % item)
    with open(r'D:/Dropbox/Python/test/%s/POTCAR' % (compound_name), 'w' ) as f:
        for item in POTCAR:
            f.write("%s" % item)
 
else:
    print("Directory already exists")


   
