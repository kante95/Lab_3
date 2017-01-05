import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-
import numpy as np



vin = [-2.322]*1400 + np.random.normal(0, 0.001, 1400)
start = -0.35
step = 5*10**(-5)

t = np.arange(-start, -start + step * 1400, step)


clock = 5*0.002
number = t[-1]/clock

upstep = 0.008

vout = np.zeros(len(t))

for i in range(42):
	vout[i] = -2.28+ np.random.normal(0, 0.0008, 1)
	vout[i+42] = -2.28 -upstep + np.random.normal(0, 0.0008, 1)
	vout[i+2*42] = -2.28 -2*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+3*42] = -2.28 -3*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+4*42] = -2.28 -4*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+5*42] = -2.28 -5*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+6*42] = -2.28 -6*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+7*42] = -2.28 -5*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+8*42] = -2.28 -6*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+9*42] = -2.28 -5*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+10*42] = -2.28 -6*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+11*42] = -2.28 -5*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+12*42] = -2.28 -6*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+13*42] = -2.28 -5*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+14*42] = -2.28 -6*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+15*42] = -2.28 -5*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+16*42] = -2.28 -6*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+17*42] = -2.28 -5*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+18*42] = -2.28 -6*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+19*42] = -2.28 -5*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+20*42] = -2.28 -6*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+21*42] = -2.28 -5*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+22*42] = -2.28 -6*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+23*42] = -2.28 -5*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+24*42] = -2.28 -6*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+25*42] = -2.28 -5*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+26*42] = -2.28 -6*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+27*42] = -2.28 -5*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+28*42] = -2.28 -6*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+29*42] = -2.28 -5*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+30*42] = -2.28 -6*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+31*42] = -2.28 -5*upstep+ np.random.normal(0, 0.0008, 1)
	vout[i+32*42] = -2.28 -6*upstep+ np.random.normal(0, 0.0008, 1)
	


plt.figure("ciao")
plt.grid(True)

plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
 
plt.plot(t,vin)
plt.plot(t,vout)
plt.xlim(0.35,0.419)
plt.ylim(-2.35,-2.25)

plt.savefig("good.png")

