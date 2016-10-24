from sympy import *

def propagate_error(formula, variables):
	#Author: Canteri Marco
	#Calcolate the error of a quantity q=f(x,y,z,....) from the errors on the variables x,y,z,...
	#input: f is a string that contains the function f
	#		dict1 is a dictionary which has for keys the variables and for values a 2-dimensional array with the variabile value and is error.
	#output: The error of q
	#Example: propagate_error('x+y*3',{'x':[1,0.5],'y':[2,0.3]})

    error = 0
    var_values = {symbols(var): variables[var][0] for var in variables.keys()}
    for var in variables.keys():
        partial_derivative = diff(formula, symbols(var)).evalf(subs=var_values)
        error += (partial_derivative * variables[var][1]) ** 2
    return sqrt(error)

list1 = {'Vo':[-12.8785,0.0042],'R1':[10000,500],'R2':[100000,5000],'R3':[1000000,50000]}
print(propagate_error('-Vo/(R3*(1+R2/R1))',list1))