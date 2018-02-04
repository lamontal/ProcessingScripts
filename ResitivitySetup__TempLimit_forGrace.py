# user inputs
width = 0.503 # pellet width in cm
thickness = 0.306 # pellet thickness in cm
separation = 0.084 #separation of inner contacts

temp_cutoff = 0 #only take cooling/warming data above given temperature (set to 0 for default)

infile = r'170728_LixTiNb2O7_MMB2119_3.txt'	
outfile = r'test.txt'	

# Don't change anything below this line
import numpy as np

#Reading raw data from resistivity setup

raw = []
with open( infile , 'r' ) as f:
	#for line in f:
        for line in f.readlines()[8:]:
            line = line.split()
            raw.append(line)
raw = [ r for r in raw if r is not '' ]


#Reducing data
temp = [] 
res = []
for i in raw:   #creating seperate lists for temperature and resistivity
    temp.append(float(i[0]))
    res.append(float(i[1]))

restiv = [i * width * thickness / separation for i in res] #converting resistance to resistivity

         
raw2 = list((i,j) for (i,j) in zip(temp, restiv) if i > temp_cutoff) #only taking data greater than temp_cutoff
raw3 = np.array(raw2)


mintemp = np.argmin(raw3[:,0]) #finding minimum temperature
cool = np.array(raw3[0:mintemp,:]) #data on cooling down to temp_cutoff
warm = np.array(raw3[mintemp:,:]) #data on warming above temp_cutoff
newset = np.array([["&", "newxy"]]) #adding ampersand to start new set in grace

final = np.concatenate((cool,newset,warm))



# write output file
np.savetxt(outfile,final, delimiter = "\t", fmt="%s")

