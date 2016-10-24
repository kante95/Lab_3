from math import sqrt, log10, floor
from sympy import *
import numpy as np
import matplotlib.pyplot as plt


def propagate_error(f, variables):
    # Author: Canteri Marco
    # Calcolate the error of a quantity q=f(x,y,z,....) from the errors on the
    # variables x,y,z,...
    # input: f is a string that contains the function f
    # dict1 is a dictionary which has for keys the variables and for
    # values a 2-dimensional array with the variabile value and is error.
    # output: The error of q
    # Example: propagate_error('x+y*3',{'x':[1,0.5],'y':[2,0.3]})

    squareerror = 0
    var = variables.keys()
    dict2 = {}
    for i in var:
        x = symbols(i)
        dict2[x] = variables[i][0]
    for i in var:
        x = symbols(i)
        g = diff(f, x)
        pd = g.evalf(subs=dict2)
        squareerror += (pd * variables[i][1]) ** 2
    return squareerror ** 0.5


def err_prop(x, dx, y, dy, operator):
    if operator == "+" or operator == "-":
        dz = sqrt(dx ** 2 + dy ** 2)
    elif operator == "*":
        dz = abs(x * y) * sqrt((dx / x) ** 2 + (dy / y) ** 2)
    elif operator == "/":
        dz = abs(x / y) * sqrt((dx / x) ** 2 + (dy / y) ** 2)
    return dz


def resolution_error(Delta_x):
    return (Delta_x / sqrt(12))


def error_mean(dx, N):
    return dx / N


def get_error(value, mode='Ohm'):
    multimiter_setting = set_multimiter(mode)
    for ranges, xcent_val, xcent_range in multimiter_setting:
        if value < ranges:
            return (value * xcent_val) / 100 + (ranges * xcent_range) / 100


def set_multimiter(mode):
    if mode == 'Ohm':
        ranges = [200.0, 2000.0, 20000.0, 200000.0,
                  float(10 ** 6), float(10 ** 7)]
        percent_values = [0.010, 0.010, 0.010, 0.010, 0.012, 0.040]
        percent_ranges = [0.004, 0.001, 0.001, 0.001, 0.001, 0.001]
    elif mode == 'V':
        ranges = [0.2, 2.0, 20.0, 200.0, 1000.0]
        percent_values = [0.004, 0.0035, 0.004, 0.005, 0.0055]
        percent_ranges = [0.0025, 0.0006, 0.0005, 0.0006, 0.001]

    return zip(ranges, percent_values, percent_ranges)


def round_to_err(x, dx):
    to_decimal = - log10(dx) + 1
    return round(x, int(to_decimal))


def round_to_last2(x):
    return round(x, -int(floor(log10(abs(x)))) + 1)

# Ananlysis of data


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
    plt.savefig(name + '.png')


def regressione_lineare(x, y, dy):
    w = 1 / (dy ** 2)
    nabla = sum(w) * sum(w * x ** 2) - (sum(w * x)) ** 2
    a = (sum(w * x ** 2) * sum(w * y) - sum(w * x) * sum(w * x * y)) / nabla
    b = (sum(w) * sum(w * y * x) - sum(w * y) * sum(w * x)) / nabla
    da = sqrt(sum(w * x ** 2) / nabla)
    db = sqrt(sum(w) / nabla)
    chi2 = sum((y - a - b * x) ** 2 / (dy ** 2)) / len(x)
    return [a, b, da, db, chi2]