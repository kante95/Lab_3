import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-
import numpy as np

plt.rc('text', usetex=True)


FONDO_SCALA = 0.16
dv = FONDO_SCALA / (2 ** 8)

files = ['1', '2', '4', '5']



def read_data(file, numcols=3):
    try:
        data = np.genfromtxt('data/' + file, delimiter=",",
                         usecols=range(numcols), skip_header=2)
        data = data[~np.isnan(data).any(axis=1)]
        vin = data[:, 1]
        vout = data[:, 2]
        data = np.genfromtxt('data/' + file, delimiter=",",
                         usecols=range(5), skip_header=1, max_rows=1)
        start = data[-2]
        step = data[-1]
        t = np.arange(start,start+step*1400,step)
        return t, vin, vout       
    except IOError as e:
        print False

plt.figure("prima roba")
t,vin,vout1 = read_data("1_1.csv")
t,vin,vout2 = read_data("1_2.csv")
t,vin,vout3 = read_data("1_3.csv")
plt.grid(True)
plt.plot(t*1000,vin,'',t*1000,vout1,'',t*1000,vout2,'',t*1000,vout3,'')
plt.xlabel("Time [ms]")
plt.ylabel("Voltage [V]")
plt.legend([r'$v_{in}$', r'$v_{o}$', r'$v_o$', r'$v_o$'],loc = 2)


plt.figure("secondo circuito")
t,vin,vout = read_data("2_1.csv")
plt.grid(True)
plt.plot(t*1000,vin)
plt.plot(t*1000,vout)
plt.xlabel("Time [ms]")
plt.ylabel("Voltage [V]")
plt.legend([r'$v_{in}$', r'$v_{o}$'])

plt.figure("terzo circuito")
t,vin,vout = read_data("4_1.csv")
t,vin,vout2 = read_data("4_2.csv")
plt.grid(True)
plt.plot(t*1000,vin)
plt.plot(t*1000,vout)
plt.plot(t*1000,vout2)
plt.xlabel("Time [ms]")
plt.ylabel("Voltage [V]")
plt.legend([r'$v_{in}$', r'Senza follower',r'Con follower'])

plt.figure("quinto circuito")
t,vin,vout = read_data("5_1.csv")
plt.grid(True)
plt.plot(t*1000,vin)
plt.plot(t*1000,vout)
plt.xlabel("Time [ms]")
plt.ylabel("Voltage [V]")
plt.legend([r'$v_{in}$', r'$v_0$'])

plt.figure("quinto circuito_2")
t,vin,vout = read_data("5_2.csv")
plt.grid(True)
plt.plot(t*1000,vin)
plt.plot(t*1000,vout)
plt.xlabel("Time [ms]")
plt.ylabel("Voltage [V]")
plt.legend([r'$v_{in}$', r'$v_0$'])

plt.show()
 

