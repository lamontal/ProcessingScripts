# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 09:14:54 2017

@author: Leo
"""
upperTcutoff = 300  #(1/kbT) cutoff value, 0 default
lowerTcutoff = 130
infile = r'test.txt'	
kB = 8.6173303*10**(-5)

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
import numpy as np

plt.close()


df = pd.read_table(infile, delim_whitespace=True, names=('#X', "Resistivity")) #read xy files into a dataframe

setindex = df[df['#X'].str.contains("&")].index

cooldf=df.iloc[:setindex[0],:].astype(float)  
cooldf = cooldf[( cooldf["#X"] > lowerTcutoff) & (cooldf["#X"] <  upperTcutoff)]
             
warmdf=df.iloc[(setindex[0]+1):,:].astype(float)             
warmdf = warmdf[(warmdf["#X"] > lowerTcutoff) & (warmdf["#X"] < upperTcutoff)]

plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure 
plt.plot(cooldf.iloc[1:,0], cooldf.iloc[1:,1])
plt.plot(warmdf.iloc[1:,0], warmdf.iloc[1:,1])
               
cooldf["#X"] = 1/(kB* cooldf["#X"])
cooldf["Resistivity"] = np.log(cooldf["Resistivity"])



cool_x = cooldf["#X"].values
cool_x=cool_x.reshape(len(cool_x),1)

cool_y = cooldf["Resistivity"].values
cool_y=cool_y.reshape(len(cool_y),1)


# Create linear regression object
coolregr = linear_model.LinearRegression()


coolregr.fit(cool_x,cool_y)

plt.subplot(212)
plt.plot(cool_x,cool_y)
plt.plot(cool_x, coolregr.predict(cool_x), color='orange', linewidth=3, label = "cool")
print( "%f cooling" % (coolregr.coef_))

warmdf["#X"] = 1/(kB* warmdf["#X"])
warmdf["Resistivity"] = np.log(warmdf["Resistivity"])




warm_x = warmdf["#X"].values
warm_x=warm_x.reshape(len(warm_x),1)

warm_y = warmdf["Resistivity"].values
warm_y=warm_y.reshape(len(warm_y),1)

# Create linear regression object
warmregr = linear_model.LinearRegression()


warmregr.fit(warm_x,warm_y)


plt.plot(warm_x,warm_y)
plt.plot(warm_x, warmregr.predict(warm_x), color='orange', linewidth=3, label = "warm")
print( "%f warming" % (warmregr.coef_))
