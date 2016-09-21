import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-
import numpy as np
from error_lib import *


FONDO_SCALA = 0.16
dv = FONDO_SCALA / (2 ** 8)

files = ['scope1.csv', 'scope2.csv', 'scope3.csv', 'scope4.csv']


def read_data(file):
    data = np.genfromtxt('data/' + file, delimiter=",",
                         usecols=(0, 1, 2), skip_header=2)
    data = data[~np.isnan(data).any(axis=1)]
    t = data[:, 0]
    vin = data[:, 1]
    vout = data[:, 2]

    return t, vin, vout


def read_data_final(file):
    data = np.genfromtxt('data/' + file, delimiter=",",
                         usecols=(0, 1, 2, 3), skip_header=2)
    data = data[~np.isnan(data).any(axis=1)]
    t = data[:, 0]
    vin1 = data[:, 1]
    vin2 = data[:, 2]
    vout = data[:, 3]

    return t, vin1, vin2, vout


for file in files:
    t, vin, vout = read_data(file)
    plt.figure(file)
    plt.grid(True)
    plt.plot(t, vin)
    plt.plot(t, vout)
    plt.xlabel("time [s]")
    plt.ylabel("Voltage [V]")
    plt.legend(['V1_in', 'V_out'])
    if file == 'scope3.csv':
        follow_gain_vout = max(vout)
        follow_gain_vin = max(vin)
    elif file == 'scope4.csv':
        amp_invertent_vout = max(vout)
        amp_invertent_vin = max(vin)
    elif file == 'scope1.csv':
        print max(vout)

t, vin1, vin2, vout = read_data_final('scope5.csv')
plt.figure('scope5.csv')
plt.grid(True)
plt.plot(t, vin1)
plt.plot(t, vin2)
plt.plot(t, vout)
plt.xlabel("time [s]")
plt.ylabel("Voltage [V]")
f_vin1 = max(vin1)
f_vin2 = max(vin2)
f_vout = max(vout)
plt.legend(['V1_in', 'V2_in', 'V_out'])

plt.show()

R2 = 218.371
R1 = 99.8913
R3 = 99.8990
R = [0, R1, R2, R3]
dR = []
cnt = 0
for resitance in R:
    dR.append(get_error(resitance))
    print 'Resistance' + ' ' + str(cnt) + ': ' + str(resitance) + '+-' + str(get_error(resitance))
    cnt += 1

R2_div_R1 = R[2] / R[1]
R2_div_R1_err = err_prop(R[2], dR[2], R[1], dR[1], '/')
follow_gain_vout_err = err_prop(follow_gain_vin, dv, R2_div_R1, R2_div_R1_err, '*')
teo_follow_gain_vout = follow_gain_vin * (1 + R2_div_R1)

amp_invertent_vout_err = err_prop(amp_invertent_vin, dv, R2_div_R1, R2_div_R1_err, '*')
teo_amp_invertent_vout = amp_invertent_vin * R2_div_R1

v1_div_r2 = f_vin1 / R[1]
v2_div_r3 = f_vin2 / R[3]
v1_div_r2_err = err_prop(f_vin1, dv, R[1],dR[1], '/')
v2_div_r3_err = err_prop(f_vin2, dv, R[3], dR[3], '/')
v_div_R = v1_div_r2 + v2_div_r3
v_div_R_err = err_prop(v1_div_r2, v1_div_r2_err, v2_div_r3, v2_div_r3_err, '+')
vout_teo = R1 * (v_div_R)
vout_teo_err = err_prop(R[2], dR[2], v_div_R, v_div_R_err, '*')

print 'Emitter follower:'
print 'V_in', follow_gain_vin, '+-', dv
print 'V_out', follow_gain_vout, '+-', dv
print 'Theoric v_out', teo_follow_gain_vout, '+-', follow_gain_vout_err

print "Invertent amplifier"
print 'V_in', amp_invertent_vin, '+-', dv
print 'V_out', amp_invertent_vout, '+-', dv
print 'Theoric v_out', teo_amp_invertent_vout, '+-', amp_invertent_vout_err

print 'Weighted summing amplifier'
print 'V_in1', f_vin1, '+-', dv
print 'V_in2', f_vin2, '+-', dv
print 'V_out', f_vout, '+-', dv
print 'Theoric v_out', vout_teo, '+-', vout_teo_err

