
infile = r'D:/Dropbox/XRD/SrPd3O4/170612_SrPd3O4/LKL063_Sr85Na15Pd3O4_testingdecomp.txt'	
outfile = r'D:/Dropbox/XRD/SrPd3O4/170612_SrPd3O4/LKL063_Sr85Na15Pd3O4_testingdecomp_grace.txt'	

# Don't change anything below this line

import csv
#Reading exported data from TOPAS

raw = []
with open( infile , 'r' ) as f:
    for line in f.readlines()[2:]: #Skip the first two lines of data
        raw.append(line) 
raw = [ r.strip('\n') for r in raw ]
raw = [ r for r in raw if r is not '' ]

raw = [r.split(",") for r in raw ]

header = [ ]
with open( infile , 'r' ) as f:
    for line in f.readlines()[:2]: #reads the 1st 2 lines of TOPAS export
        header.append(line) 
header = ["#" + h  for h in header ] # adds a "#" so grace won't read them

#writing export file
        
with open( outfile , 'w' ) as f:
    for item in header:
        f.write("%s" % item)
    wr = csv.writer(f, delimiter="\t") #delimits columns of data with tabs for grace
    wr.writerows(raw)
