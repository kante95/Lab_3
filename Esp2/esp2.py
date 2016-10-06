# This code was nor written nor approved by LorenzoBi


import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-
import numpy as np
from error_lib import *

plt.rc('text', usetex=True)


FONDO_SCALA = 0.16
dv = FONDO_SCALA / (2 ** 8)

files = ['1', '2', '4', '5']


def read_data(file, numcols=3):

    data = np.genfromtxt('data/' + file, delimiter=",",
                         usecols=range(numcols), skip_header=2)
    data = data[~np.isnan(data).any(axis=1)]
    vin = data[:, 1]
    vout = data[:, 2]
    data = np.genfromtxt('data/' + file, delimiter=",",
                         usecols=range(5), skip_header=1, max_rows=1)
    start = data[-2]
    step = data[-1]
    t = np.arange(start, start + step * 1400, step)
    return t, vin, vout


RF = 983.9
Rin = 199.842
R3 = 1001.34
R2 = 1483.5
R1 = 1484.7

dRF = get_error(RF)
dRin = get_error(Rin)
dR3 = get_error(R3)
dR2 = get_error(R2)
dR1 = get_error(R1)
dR = get_error(100178)
dRl = get_error(19863)
dRc = get_error(4969.3)

print dRF,dRin,dR3,dR2,dR2,dR,dRl,dRc

plt.figure("Variable amplifier")
_, _, vout1 = read_data("1_1.csv")
_, _, vout2 = read_data("1_2.csv")
t, vin, vout3 = read_data("1_3.csv")
plt.grid(True)
plt.plot(t*1000, vin, '', t * 1000, vout1, '', t * 1000, vout2, '', t * 1000, vout3, '')
plt.xlabel("Time [ms]")
plt.ylabel("Voltage [V]")
plt.legend([r'$v_{in}$', r'$v_{o}$', r'$v_o$', r'$v_o$'], loc=2)


plt.figure("Weighted amplifier")
t, vin, vout = read_data("2_1.csv")
plt.grid(True)
plt.plot(t * 1000, vin)
plt.plot(t * 1000, vout)
plt.xlabel("Time [ms]")
plt.ylabel("Voltage [V]")
plt.legend([r'$v_{in}$', r'$v_{o}$'])

pkpk_Vin = max(vin) - min(vin)
sum_Vin_Vin = pkpk_Vin
rF_div_r3 = RF / R3
pkpk_Vout = sum_Vin_Vin * (1 + rF_div_r3)
err_sum_Vin_Vin = err_prop(max(vin), sqrt(2) * dv, min(vin), sqrt(2) * dv, '-')
err_division = err_prop(RF, dRF, R3, dR3, '/')
err_pkpk_Vout = err_prop(sum_Vin_Vin, err_sum_Vin_Vin, rF_div_r3, err_division, '*')
print 'Summing amp theoretical value approx', pkpk_Vout, '+-', err_pkpk_Vout
print 'Measurament of Summing amp output', max(vout) - min(vout), '+-', sqrt(2) * dv

plt.figure("Emitter follower compared")
t, vin, vout = read_data("4_1.csv")
t, vin, vout2 = read_data("4_2.csv")
plt.grid(True)
plt.plot(t * 1000, vin)
plt.plot(t * 1000, vout)
plt.plot(t * 1000, vout2)
plt.xlabel("Time [ms]")
plt.ylabel("Voltage [V]")
plt.legend([r'$v_{in}$', r'Senza follower', r'Con follower'])

plt.figure("Tuning diff-amplifier")
t, vin, vout = read_data("5_1.csv")
plt.grid(True)
plt.plot(t * 1000, vin)
plt.plot(t * 1000, vout)
plt.xlabel("Time [ms]")
plt.ylabel("Voltage [V]")
plt.legend([r'$v_{in}$', r'$v_0$'])

plt.figure("Differential amplifier")
t, vin, vout = read_data("5_2.csv")
plt.grid(True)
plt.plot(t * 1000, vin)
plt.plot(t * 1000, vout)
plt.xlabel("Time [ms]")
plt.ylabel("Voltage [V]")
plt.legend([r'$v_{in}$', r'$v_0$'])

plt.show()
 

