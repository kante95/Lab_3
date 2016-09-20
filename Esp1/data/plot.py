
import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-
import numpy as np

data = np.genfromtxt("scope5.csv", delimiter=",",usecols = (0,1,2),skip_header=2)
#eliminate rows with nan
data = data[~np.isnan(data).any(axis=1)]
#extract columns
t =  data[:,0]
vin = data[:,1]
vout = data[:,2]

plt.grid(True)
plt.plot(t,vin)
plt.plot(t,vout)


plt.show() 



