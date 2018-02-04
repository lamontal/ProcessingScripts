path = r'D:/Dropbox/XRD/CaPd3O4/xrdplotting' # path to folder containing .xy patterns you want to plot
scale = 1.05 #how seperated you want the patterns to be,should be >1 to stop overlap



# Don't change anything below this line
import os
import pandas as pd
import matplotlib.pyplot as plt



plt.close()
files = [each for each in os.listdir(path) if each.endswith('.xy')] #create list of .xy files
os.chdir(path)
export = pd.DataFrame({"#X" : [], "data": []})
newset = pd.DataFrame({"#X" : ["&"], "data": ["newxy"]})
for f in files:
    df = pd.read_table(f, delim_whitespace=True, names=('#X', f)) #read xy files into a dataframe
    df[f] = (df[f]/df[f].max() + files.index(f) * scale) #scale the pattern so the max is 1 and then is offset from previous patterns
    df.columns.values[1] = "data"
    export = pd.concat([export, df, newset])
    plt.plot(df.iloc[1:,0], df.iloc[1:,1], label = f)

#plt.set_position([box.x0, box.y0, box.width * 0.8, box.height])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.).draggable() #puts the legend outside the plot and makes it moveable
#plt.legend(loc= "best") 
plt.show()
#print(os.listdir(path))
#ylim = (-0.05, 1.05*(files.index(f)+1))
export.to_csv("forgrace.csv", index=False, sep = "\t")

""" Attempting to fit background
background = np.poly1d(np.polyfit(df.iloc[1:,0], df.iloc[1:,1], 3))
bckg_fit = background(df.iloc[1:,0])

plt.plot(df.iloc[1:,0], bckg_fit,)
"""
