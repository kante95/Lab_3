from error_lib import *
import matplotlib.pyplot as plt
import numpy as np
import math


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


def plot(data, name='figure'):
    t = data[0]
    vin = data[1]
    vout = data[2]
    plt.figure(name)
    plt.grid(True)
    plt.plot(t * 1000, vin)
    plt.plot(t * 1000, vout)
    plt.xlabel("Time [ms]")
    plt.ylabel("Voltage [V]")
    plt.legend([r'$v_{in}$', r'$v_{o}$', r'$v_o$', r'$v_o$'], loc=2)


def regressione_lineare(x, y, dy):
    w = 1 / (dy ** 2)
    nabla = sum(w) * sum(w * x ** 2) - (sum(w * x)) ** 2
    a = (sum(w * x ** 2) * sum(w * y) - sum(w * x) * sum(w * x * y)) / nabla
    b = (sum(w) * sum(w * y * x) - sum(w * y) * sum(w * x)) / nabla
    da = math.sqrt(sum(w * x ** 2) / nabla)
    db = math.sqrt(sum(w) / nabla)
    chi2 = sum((y - a - b * x) ** 2 / (dy ** 2)) / len(x)
    return [a, b, da, db, chi2]

FONDO_SCALA = 0.16
dv = FONDO_SCALA / (2 ** 8)

# Direct measurament offset
V_off = -1.484 * 10 ** -3
dV_off = get_error(V_off, 'V')
V_off = round_to_err(V_off, dV_off)
print 'Direct measurament V offset:', V_off, '+-', round_to_last2(dV_off)

# Amplified measurament with bias current
R10_1 = 9.963
dR10_1 = get_error(R10_1)
R10k_1 = 9906
dR10k_1 = get_error(R10k_1)

V_out = -1.3265
dV_out = get_error(V_out, 'V')

V_off_1 = V_out / (1 + R10k_1 / R10_1)
Rk_R = R10k_1 / R10_1
dRk_R = err_prop(R10k_1, dR10k_1, R10_1, dR10_1, '/')
dV_off_1 = err_prop(V_out, dV_out, Rk_R, dRk_R, '/')
V_off_1 = round_to_err(V_off_1, dV_off_1)

print 'Amplified measurament with bias current', V_off_1, '+-', round_to_last2(dV_off_1)

# Amplified without polarized current

R10_2 = 10.003
dR10_2 = get_error(R10_2)
R10k_2 = 9926.4
dR10k_2 = get_error(R10k_2)

V_outc = 1.301
dV_outc = get_error(V_outc, 'V')
V_off_1c = V_outc / (1 + R10k_1 / R10_1)
dV_off_1c = round_to_last2(err_prop(V_outc, dV_outc, Rk_R, dRk_R, '/'))
V_off_1c = round_to_err(V_outc / (1 + R10k_1 / R10_1), dV_off_1c)

print 'Amplified measurament with no bias current', V_off_1c, '+-', dV_off_1c

# Current di bias measurament
V_ip = -3.837
V_im = 3.865
dV_ip = get_error(V_ip, 'V')
dV_im = get_error(V_im, 'V')

R_M = 982000.0
dR_M = get_error(R_M)
R_ck = 99219.6
dR_ck = get_error(R_ck)
R_k = 1001.4
dR_k = get_error(R_k)

dR_ck_R_k = err_prop(R_ck, dR_ck, R_k, dR_k, '/')
dR_prod = err_prop(R_M, dR_M, R_ck / R_k, dR_ck_R_k, '*')
R_prod = R_M * (1 + (R_ck / R_k))
di_bp = err_prop(V_ip, dV_ip, R_prod, dR_prod, '/')
i_bp = round_to_err(V_ip / R_prod, di_bp)

print 'Non invertent current of bias', i_bp, '+-', round_to_last2(di_bp)

V_im_R_ck = V_im / R_ck
R_k_R_M = R_k / R_M
dV_im_R_ck = err_prop(V_im, dV_im, R_ck, dR_ck, '/')
dR_k_R_M = err_prop(R_k, dR_k, R_M, dR_M, '/')
di_bm = err_prop(V_im_R_ck, dV_im_R_ck, R_k_R_M, dR_k_R_M, '*')
i_bm = round_to_err(V_im_R_ck * R_k_R_M, di_bm)

print 'Invertent current of bias', i_bm, '+-', round_to_last2(di_bm)

# Max current
t, vin, vout = read_data('Max_I.csv')
plot((t, vin, vout), 'Maximum current erogated')
v_max = max(vout)
v_min = min(vout)
R_osc = 50
dmax_i = round_to_last2(dv / 50)
print 'Max positive current', round_to_err(v_max / 50, dmax_i), '+-', dmax_i
print 'Max negative current', round_to_err(v_min / 50, dmax_i), '+-', dmax_i

# Slew Ratio
t, vin, vout = read_data('Slew_R.csv')


from_v = min(vout[(0.0000004 < t) & (t < 0.0000095)])
to_v = max(vout[(0.0000004 < t) & (t < 0.0000095)])
from_v = (to_v - from_v) * 0.1 + from_v
to_v = (to_v - from_v) * 0.9 + from_v

slew_part = (from_v < vout) & (vout < to_v)

a, b, _, db, chi2 = regressione_lineare(t[slew_part], vout[slew_part], dv * np.ones(sum(slew_part)))
print 'The slew rate is:', round_to_err(b, db), '+-', round_to_last2(db), 'V / s'
plot((t, vin, vout), 'Slew Ratio')
plt.plot([-0.002, 0.012], [from_v, from_v], [-0.002, 0.012], [to_v, to_v], 'r')
# plt.plot(t[slew_part] * 1000, (a + b * t[slew_part]), 'brown')

plt.show()