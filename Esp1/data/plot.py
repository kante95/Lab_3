import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-
import numpy as np

file = ['scope1.csv','scope2.csv','scope3.csv','scope4.csv']

def read_data(file):
	data = np.genfromtxt(file, delimiter=",",usecols = (0,1,2),skip_header=2)
	data = data[~np.isnan(data).any(axis=1)]
	t =  data[:,0]
	vin = data[:,1]
	vout = data[:,2]
	return t,vin,vout

for i in file:
	t,vin,vout = read_data(i)
	plt.figure(i)
	plt.grid(True)
	plt.plot(t,vin)
	plt.plot(t,vout)
	plt.xlabel("time [s]")
	plt.ylabel("Voltage [V]")


plt.show() 



