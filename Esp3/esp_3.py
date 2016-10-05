from error_lib import *

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
V_im = get_error(V_im, 'V')

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

print 'Current of bias +', i_bp, '+-', round_to_last2(di_bp)

