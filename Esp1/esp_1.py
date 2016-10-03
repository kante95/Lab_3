import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-
import numpy as np
from error_lib import *

plt.rc('text', usetex=True)
#plt.rc('font', family='serif')


FONDO_SCALA = 0.16
dv = 1.414*FONDO_SCALA / (2 ** 8)

files = ['scope1.csv', 'scope2.csv', 'scope3.csv', 'scope4.csv', 'scope5.csv']


def read_data(file, numcols=3):
    data = np.genfromtxt('data/' + file, delimiter=",",
                         usecols=range(numcols), skip_header=2)
    data = data[~np.isnan(data).any(axis=1)]
    t = data[:, 0]
    vin = data[:, 1:numcols - 1]
    vout = data[:, -1]

    return t, vin, vout


for file in files:
    if file == 'scope5.csv':
        numcols = 4
    else:
        numcols = 3
    t, vin, vout = read_data(file, numcols)
    plt.figure(file)
    plt.grid(True)
    plt.plot(t*1000, vin)
    plt.plot(t*1000, vout)
    plt.xlim(t[0]*1000,t[-1]*1000)
    plt.xlabel("Time [ms]")
    plt.ylabel("Voltage [V]")
    if file == 'scope5.csv':
        plt.legend([r'$v_{in1}$', r'$v_{in2}$', '$v_o$'])
        f_vin1 = max(vin[:, 0])-min(vin[:, 0])
        f_vin2 = max(vin[:, 1])-min(vin[:, 1])
        f_vout = max(vout)-min(vout)
    else:
        plt.legend([r'$v_{in}$', r'$v_{o}$'])
    if file == 'scope3.csv':
        follow_gain_vout = max(vout)-min(vout)
        follow_gain_vin = max(vin)[0] - min(vin)[0]
    elif file == 'scope4.csv':
        amp_invertent_vout = max(vout)-min(vout)
        amp_invertent_vin = max(vin)[0]- min(vin)[0]
    elif file == 'scope1.csv':
        print 'Max volatage in open loop:', max(vout), 'V\n'
        print 'Min volatage in open loop:', min(vout), 'V\n'
    #plt.savefig(file+'.png');

plt.show()

R1 = 99.8913
R2 = 218.371
R3 = 99.8990
R = [0, R1, R2, R3]
dR = []
cnt = 0
for r in R:
    dR.append(get_error(r))
    if len(dR) != 1:
        print 'R' + str(cnt) + ':', str(r), '+-', str(get_error(r)), 'V'
    cnt += 1
print '\n'

R2_div_R1 = R[2] / R[1]
R2_div_R1_err = err_prop(R[2], dR[2], R[1], dR[1], '/')
amp_v_err = err_prop(follow_gain_vin, dv, R2_div_R1, R2_div_R1_err, '*')
teo_follow_gain_vout = follow_gain_vin * (1 + R2_div_R1)

amp_invertent_vout_err = err_prop(amp_invertent_vin, dv, R2_div_R1, R2_div_R1_err, '*')
teo_amp_invertent_vout = amp_invertent_vin * R2_div_R1

v1_div_r2 = f_vin1 / R[1]
v2_div_r3 = f_vin2 / R[3]
v1_div_r2_err = err_prop(f_vin1, dv, R[1], dR[1], '/')
v2_div_r3_err = err_prop(f_vin2, dv, R[3], dR[3], '/')
v_div_R = v1_div_r2 + v2_div_r3
v_div_R_err = err_prop(v1_div_r2, v1_div_r2_err, v2_div_r3, v2_div_r3_err, '+')
vout_teo = R[2] * (v_div_R)
vout_teo_err = err_prop(R[2], dR[2], v_div_R, v_div_R_err, '*')

print 'Amplifier:'
print 'V_in', follow_gain_vin, '+-', dv, 'V'
print 'V_out', follow_gain_vout, '+-', dv, 'V'
print 'Theoric v_out', teo_follow_gain_vout, '+-', amp_v_err, 'V'
print '\n'


print "Invertent amplifier"
print 'V_in', amp_invertent_vin, '+-', dv, 'V'
print 'V_out', amp_invertent_vout, '+-', dv, 'V'
print 'Theoric v_out', teo_amp_invertent_vout, '+-', amp_invertent_vout_err, 'V'
print '\n'

print 'Weighted summing amplifier'
print 'V_in1', f_vin1, '+-', dv, 'V'
print 'V_in2', f_vin2, '+-', dv, 'V'
print 'V_out', f_vout, '+-', dv, 'V'
print 'Theoric v_out', vout_teo, '+-', vout_teo_err, 'V'
print '\n'
