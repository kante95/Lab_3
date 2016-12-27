import matplotlib.pyplot as plt
import numpy as np
import math



def read_data(file, numcols=2):
    data = np.genfromtxt(file, delimiter="\t", usecols=range(2))
    t = data[:, 0]
    vout = data[:, 1]
    return t, vout


#t, vout = read_data('20hz-10hz.csv')
t = np.arange(0, 2, 0.04)
vout = 2.5*np.sin(10*2*np.pi*t+1.3)

T = 0.04
t1 = np.arange(0, 2, 0.001)
x = np.zeros(len(t1))

for i in range(len(t1)):
    x[i] = sum(vout*np.sinc((t1[i]-t)/T))

plt.figure("25Hz")
plt.grid(True)
plt.plot(t, vout,'.')
plt.plot(t1,x)
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.legend(['Sampling 25 Hz', 'Whittaker–Shannon'], loc=2,numpoints=1)

plt.savefig("25Hz.png")


t, vout = read_data('10hz-10hz.csv')
#t = np.arange(0, 5, 0.005)
#vout = 2.5*np.sin(20*2*np.pi*t)

T = 0.1
t1 = np.arange(0, 10, 0.001)
x = np.zeros(len(t1))

for i in range(len(t1)):
    x[i] = sum(vout*np.sinc((t1[i]-t)/T))

plt.figure("10Hz")
plt.grid(True)
plt.plot(t, vout,'.')
plt.plot(t1,x)
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.legend(['Sampling 10 Hz', 'Whittaker–Shannon'], loc=2,numpoints=1)

plt.savefig("10Hz.png")


t, vout = read_data('5hz-10hz.csv')
#t = np.arange(0, 5, 0.005)
#vout = 2.5*np.sin(20*2*np.pi*t)

T = 0.2
t1 = np.arange(0, 9.9, 0.001)
x = np.zeros(len(t1))

for i in range(len(t1)):
    x[i] = sum(vout*np.sinc((t1[i]-t)/T))

plt.figure("5Hz")
plt.grid(True)
plt.plot(t, vout,'.')
plt.plot(t1,x)
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.legend(['Sampling 5 Hz', 'Whittaker–Shannon'], loc=2,numpoints=1)

plt.savefig("5Hz.png")

t, vout = read_data('100hz-10hz.csv')
#t = np.arange(0, 5, 0.005)
#vout = 2.5*np.sin(20*2*np.pi*t)

T = 0.01
t1 = np.arange(0, 1, 0.001)
x = np.zeros(len(t1))

for i in range(len(t1)):
    x[i] = sum(vout*np.sinc((t1[i]-t)/T))

plt.figure("100Hz")
plt.grid(True)
plt.plot(t, vout,'.')
plt.plot(t1,x)
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.legend(['Sampling 100 Hz', 'Whittaker–Shannon'], loc=2,numpoints=1)


plt.savefig("100Hz.png")



t, vout = read_data('triang-500hz-100hz.csv')
#t = np.arange(0, 5, 0.005)
#vout = 2.5*np.sin(20*2*np.pi*t)

T = 0.002
t1 = np.arange(0, 0.2, 0.0001)
x = np.zeros(len(t1))

for i in range(len(t1)):
    x[i] = sum(vout*np.sinc((t1[i]-t)/T))

plt.figure("500Hz")
plt.grid(True)
plt.plot(t, vout,'.')
plt.plot(t1,x)
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.legend(['Sampling 500 Hz', 'Whittaker–Shannon'], loc=2,numpoints=1)



plt.savefig("500Hz.png")



