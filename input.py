import re
import mathlib
import equationlib

def check_input(elements):
	for e in elements:
		if e == '' or e == '\t':
			print("Input not well formated. Maybe you have entered too much space.")
			exit()

def check_key_exists(equation):
	i = 0
	for e in equation:
		if e >= 0:
			i = e
	if i != len(equation) - 1:
		print("Not all X are presents")
		exit()

def parse_input(argv):
	p = re.compile(r'X\^\d*$')
	equation = dict()
	elements = argv.split(' ')
	check_input(elements)
	tmp = ''
	sign = False
	for e in elements:
		if not p.match(e) and e[0] != 'X' and e != '*' and e != '=':
			tmp += e
		elif e == '=':
			sign = True 
		elif e[0] == 'X' and not p.match(e):
			print("Wrong input for {}, must be X^n".format(e))
			exit()
		elif p.match(e):
			key = int(e.split('^')[-1])
			if equation.get(key):
				equation[key] = equationlib.simplify_equation(equation[key], float(tmp), sign)
			else:
				if sign:
					equation[key] = mathlib.change_sign(float(tmp))
				else:
					equation[key] = float(tmp)
			tmp = ''
	check_key_exists(equation)
	return equation