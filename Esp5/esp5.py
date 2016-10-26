from uncertainties import ufloat
from error_lib import get_value_error
from lab_lib import *
import matplotlib.pyplot as plt


def create(value, mode='R'):
    return ufloat(*get_value_error(value, mode))


def plot_osc(t, v, v_c, name):
    plt.figure(name)
    plt.grid(True)
    plt.plot(t * 1000, v, '.')
    plt.plot(t * 1000, v_c)
    plt.xlabel("Time [ms]")
    plt.ylabel("Voltage [V]")
    plt.legend([r'$v_{o}$', r'$v_{c}$', r'$v_o$'], loc=2)
    plt.savefig(name + '.png')


C = create(101.1 * 10 ** -9, 'C')
R1 = create(9933.6)
R2 = create(9976.8)
R_1k = create(984.367)
R_5k = create(4721.18)
R_10k = create(9919.3)
R_15k = create(14638.0)
R_20k = create(19774.0)

t, vo, v_c = read_data('rilass_10k.csv')
plot((t, vo, v_c), 'figure')
period = []
dPeriod = []
for r in ['1k', '5k', '10k', '15k', '20k']:
    t, v, v_c = read_data('rilass_'+ r + '.csv')
    plot_osc(t, v, v_c, 'oscillation_' + r)
plt.show()