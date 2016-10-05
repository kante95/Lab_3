from sympy import *


def propagate_error(f,dict1):
	#Author: Canteri Marco
	#Calcolate the error of a quantity q=f(x,y,z,....) from the errors on the variables x,y,z,...
	#input: f is a string that contains the function f
	#		dict1 is a dictionary which has for keys the variables and for values a 2-dimensional array with the variabile value and is error.
	#output: The error of q
	#Example: propagate_error('x+y*3',{'x':[1,0.5],'y':[2,0.3]})

	l = len(dict1)
	squareerror = 0
	var = dict1.keys()
	dict2 = {}
	for i in var:
		x = symbols(i)
		dict2[x] = dict1[i][0]
	for i in var:
		x = symbols(i)
		g = diff(f,x)
		pd = g.evalf(subs=dict2)
		squareerror += (pd*dict1[i][1])**2
	return squareerror**0.5


#list1 = {'x':[2,3],'y':[3,4]}
#print(propagate_error('sin(x*y)',list1))