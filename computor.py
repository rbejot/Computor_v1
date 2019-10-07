#!/usr/bin/env python

# TODO: Detecter le degre de lequation
# TODO: Resolve equation premier degre
# TODO: REsolve equation second degre
# TODO: Gestion cas D'erreurs

import sys
import re

def change_sign(value):
	return abs(value) if value <= 0 else -value

def simplify_equation(old_value, new_value, sign):
	if sign:
		new_value = change_sign(new_value)
	return old_value + new_value

def parse_input(argv):
	p = re.compile(r'X\^\d*')
	equation = dict()
	elements = argv.split(' ')
	tmp = ''
	sign = False
	for e in elements:
		if not p.match(e) and e != '*' and e != '=':
			tmp += e
		elif e == '=':
			sign = True 
		elif p.match(e):
			key = float(e.split('^')[-1])
			if equation.get(key):
				equation[key] = simplify_equation(equation[key], float(tmp), sign)
			else:
				if sign:
					equation[key] = change_sign(float(tmp))
				else:
					equation[key] = float(tmp)
			tmp = ''
	return equation

# TODO: affichage propre de la forme reduite
def print_reduced_form(equation):
	print(equation)


equation = parse_input("8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0 + 4 * X^4")
print_reduced_form(equation)