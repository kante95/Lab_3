from errorlib import measure
import numpy as np
import matplotlib.pyplot as plt



R4 = measure('R4', [10.112], 'R')
R1 = measure('R1', [9912.], 'R')
R2 = measure('R2', [9899.0], 'R')
R3 = measure('R3', [9926.35], 'R')
Rosc = measure('Rosc', [float(10 ** 6), 0.000001], 'R')

print R1.name, R1
print R2.name, R2
print R3.name, R3
print R4.name, R4
print Rosc.name, Rosc


weight = measure('weight', [(R3.value / R4.value) + 1])
weight.calculate_error('(R3 / R4) + 1', [R3, R4])
print weight



frequency = np.array([200000., 100000., 60000., 30000., 15000., 10000.])
phase = np.array([-87, -88, -89, -88, -87, -85])
Vout = np.array([0.692, 0.533, 1.010, 0.991, 1., 1.0])
VA = np.array([0.145, 0.055, 0.063, 0.031, 0.016, 0.011])
A_OL = (Vout / VA)

new_frequency = np.array(
    [5000., 3000., 1500., 1000., 500., 200., 100., 60, 30.])
new_phase = np.array([-86, -88.7, -91, -88, -90, -90, -91, -92, -92])
new_Vout = np.array([0.074, 0.231, 0.455, 0.672,
                     1.160, 1.749, 1.955, 4.940, 4.950])
new_VA = np.array([0.335, 0.668, 0.656, 0.632, 0.548,
                   0.331, 0.1861, 0.286, 0.148])
new_A_OL = new_Vout / new_VA * weight.value

amp_frequency = np.array(
    [30., 100., 300., 1000., 3000., 10000, 30000, 100000, 200000])
amp_phase = np.array([0., 1., 2., 5, 17, 45, 74, 86, 90])
amp_Vin = np.array([0.105, 0.1048, 0.1048, 0.1048,
                    0.104, 0.104, 0.103, 0.103, 0.1038])
amp_Vout = np.array([10.16, 10.32, 10.16, 10.16,
                     9.840, 7.28, 3.28, 0.978, 0.499])

amp_frequency1 = np.array(
    [30., 100., 300., 1000, 3000, 10000, 30000, 100000, 200000, 300000])
amp_phase1 = np.array([0., 0., 0., 0., 2., 5., 19., 50., 70., 79.])
amp_Vin1 = np.array([0.505, 0.514, 0.510, 0.505, 0.506,
                     0.505, 0.500, 0.203, 0.104, 0.103])
amp_Vout1 = np.array([5.580, 5.700, 5.630, 5.640, 5.640,
                      5.580, 5.340, 1.457, 0.471, 0.334])

abs_aol = 1.5 * (10 ** 5)
# TEORICO
teo_frequency = 10 ** np.arange(0, 5.8, 0.1)
teo_Aol = abs(abs_aol / (1 + 1j * (teo_frequency / 7)))
teo_H = ((abs_aol / (1 + abs_aol*0.01))) / (1 + 1j* (teo_frequency/ (8 + 8*abs_aol*0.01)))
teo_H_10 = ((abs_aol / (1 + abs_aol*0.11))) / (1 + 1j* (teo_frequency/ (8 + 8*abs_aol*0.11)))


plt.figure('Open loop transfer function')
plt.grid(True, which="both", ls=":")
plt.plot(new_frequency, new_A_OL, 'o')
plt.plot(frequency, A_OL, 'o')
plt.plot(amp_frequency, amp_Vout / amp_Vin, 'o')
plt.plot(amp_frequency1, amp_Vout1 / amp_Vin1, 'o')
plt.plot(teo_frequency, teo_Aol)

plt.yscale('log')
plt.xscale('log')

plt.figure('decibell')
plt.plot(new_frequency, 20 * np.log10(new_A_OL), 'o')
plt.plot(frequency, 20 * np.log10(A_OL) + 0.4, 'o')
plt.plot(amp_frequency, 20 * np.log10(amp_Vout / amp_Vin) + 0.4, 'o')
plt.plot(amp_frequency1, 20 * np.log10(amp_Vout1 / amp_Vin1) + 0.4, 'o')
plt.plot(teo_frequency, 20 * np.log10(teo_Aol) + 0.4)
plt.plot(teo_frequency, 20 * np.log10(abs(teo_H)))
plt.plot(teo_frequency, 20 * np.log10(abs(teo_H_10)))

plt.xlabel('Frequency [Hz]')
plt.ylabel('Voltage amplification [dB]')
plt.legend([r'High voltage $A_{ol}$', r'Low voltage $A_{ol}$',
            r'Transfer function G $\simeq$ 100',
            r'Transfer function G $\simeq$ 10', 'Theoretical $A_{ol}$'])

plt.xscale('log')
plt.grid(True, which="both", ls=":")
plt.savefig('plot.png')

plt.show()
