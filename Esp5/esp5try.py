import matplotlib.pyplot as plt
import math
import numpy as np


plt.rc('text', usetex=True)


C = 98.0 * 10 ** -9
R2 = 9979.74
R1 = 9922.40
R = np.array([4722.14, 2157, 17907.5, 9905, 46496, 32680])
T = np.array([1.070, 0.516, 3.920, 2.180, 10.1, 7.12]) * 10 ** -3
m = 2 * C * math.log(1 + 2 * (R2 / R1))

plt.figure('Resistance - Period')
plt.grid(True)
plt.plot(R / 1000, m * R * 1000)
plt.plot(R / 1000, T * 1000, '.')
plt.xlabel(r"Resistance [k\Omega]")
plt.ylabel("Period [ms]")
# plt.figure('Residuals')
# plt.plot(R / 1000, (T - m * R) * 1000, '.')
plt.savefig('fit.png')

