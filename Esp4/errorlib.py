from sympy import *
from math import sqrt
from error_lib import *


def propagate_error(formula, variables):
    # Author: Canteri Marco
    # Calcolate the error of a quantity q=f(x,y,z,....) from the errors on the
    # variables x,y,z,...
    # input: f is a string that contains the function f
    # variables is a dictionary which has for keys the variables and for
    # values a 2-dimensional array with the variabile value and is error.
    # output: The error of q
    error = 0
    var_values = {symbols(var): variables[var][0] for var in variables.keys()}
    for var in variables.keys():
        partial_derivative = diff(formula, symbols(var)).evalf(subs=var_values)
        error += (partial_derivative * variables[var][1]) ** 2
    return sqrt(error)


class measure():
    def __init__(self, name, num_values=None, unit_meas=''):
        self.name = name
        self.num_values = self.make_list_if_not(num_values)
        self.unit_meas = unit_meas
        if unit_meas or len(self.num_values) == 2:
            self.comes_with_error()
        else:
            self.comes_without_error()

    def __str__(self):
        val = str(round_to_err(self.value, self.error)) + ' +- '
        return val + str(round_to_last2(self.error)) + ' ' + self.unit_meas

    def make_list_if_not(self, num_values):
        if type(num_values) != list:
            return [num_values]
        return num_values

    def change_R_to_Ohm(self, unit_meas):
        if unit_meas == 'R':
            return 'Ohm'
        return unit_meas

    def calculate_error(self, formula, measures_used):
        variables = {var.name: var.num_values for var in measures_used}
        self.num_values.append(propagate_error(formula, variables))
        self.error = self.num_values[1]

    def comes_with_error(self):
        if len(self.num_values) == 1:
            self.num_values.append(get_error(self.num_values[0],
                                             self.unit_meas))
        self.num_values = self.num_values
        self.unit_meas = self.change_R_to_Ohm(self.unit_meas)
        self.value = self.num_values[0]
        self.error = self.num_values[1]

    def comes_without_error(self):
        self.value = self.num_values[0]
