import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-
import numpy as np


plt.rc('text', usetex=True)
#plt.rc('font', family='serif')

def read_data(file, numcols=3):

    data = np.genfromtxt( file, delimiter=",",
                         usecols=range(numcols), skip_header=2)
    data = data[~np.isnan(data).any(axis=1)]
    vin = data[:, 1]
    vout = data[:, 2]
    data = np.genfromtxt(file, delimiter=",",
                         usecols=range(5), skip_header=1, max_rows=1)
    start = data[-2]
    step = data[-1]
    t = np.arange(start, start + step * 1400, step)
    return t, vin, vout


t, vin, vout = read_data("schmitt_zoom.csv")
plt.figure("ciao")
plt.grid(True)



plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
 
plt.plot(t,vin)
plt.plot(t,vout)

plt.show()


