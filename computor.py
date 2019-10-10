#!/usr/bin/env python

# TODO: Clean code
# TODO: Multiple files
# TODO: Faire test pour correction
# TODO: COmparer resultat vs. polynome solver

import sys
import re

# Absolute perso function
def change_sign(value):
    return -value
	# return absolute(value) if value <= 0 else -value
    
    # FIXME: ligne dorigine
    # return abs(value) if value <= 0 else -value

def simplify_equation(old_value, new_value, sign):
	if sign:
		new_value = change_sign(new_value)
	return old_value + new_value


def parse_input(argv):
    # regex
	p = re.compile(r'X\^\d*')
	equation = dict()
	elements = argv.split(' ')
	tmp = ''
	sign = False
	for e in elements:
		if not p.match(e) and e != '*' and e != '=':
            # stock signe + chiffre dans une string
			tmp += e
		elif e == '=':
            # signe egal detecter, on va changer le signe quand un chiffre est detecte mtn
			sign = True 
		elif p.match(e):
            # on choppe le chiffre dans le dernier index de [X, ^, chiffre]
			key = int(e.split('^')[-1])
			if equation.get(key):
                # si le X correspondant existe alors on simplifie
				equation[key] = simplify_equation(equation[key], float(tmp), sign)
			else:
				if sign:
                    # si on detecte le X apres '='
					equation[key] = change_sign(float(tmp))
				else:
					equation[key] = float(tmp)
			tmp = ''
	return equation

def absolute(number):
	if number < 0:
		print(number, -number)
		return -number
	return number

def reduced_form(equation):
	equation_str = ''
	for k, v in equation.items():
		if v < 0:
			equation_str += '- '
		elif k > 0:
			equation_str += '+ '
		if v == int(v):
			equation_str += str(absolute(int(v))) + ' ' + '* ' + 'X^' + str(k) + ' '
		else:
			equation_str += str(absolute(v)) + ' ' + '* ' + 'X^' + str(k) + ' '
	return 'Reduced form: ' + equation_str + '= 0'


def polynomial_degree(equation):
	degree = equation.keys()[-1]
	if equation[degree] == 0:
		i = 2
		degree_detected = False
		while i <= len(equation):
			if equation[equation.keys()[-i]] == 0:
				i += 1
			else:
				degree_detected = True
				degree = equation.keys()[-i]
				break
		if degree_detected == False:
			degree = 0
	return degree


def output_equation(equation):
	print(reduced_form(equation))
	print('Polynomial degree: ' + str(polynomial_degree(equation)))


def no_degree_solution(equation):
	if equation[0] == 0:
		print('All real numbers are solutions.')
	else:
		print('No solutions')


def first_degree_solution(equation):
	a = equation[0]
	b = equation[1]
	a = float_check(a)
	a = change_sign(a)
	solution = a / b
	solution = float_check(solution)
	print('The solution is:')
	print(solution)

def discriminant_zero(a, b):
	solution = - b / (2 * a)
	return solution

# Babylonian method
def sq_rt(number):
	n = 1
	for _ in range(10):
		n = (n + number / n) * 0.5
	return n

def float_check(number):
	if number == int(number):
		number = int(number)
	return number

def number_round(number):
	if '.' in str(number) and len(str(number).split('.')[1]) >= 6:
		return "%.6f" % number
	return number

def discriminant_positive(a, b, discriminant):
	first_solution = (- b - sq_rt(discriminant)) / (2 * a)
	second_solution = (- b + sq_rt(discriminant)) / (2 * a)
	first_solution = float_check(first_solution)
	second_solution = float_check(second_solution)
	print(number_round(first_solution))
	print(number_round(second_solution))

def second_degree_solution(equation):
	a = equation[2]
	b = equation[1]
	c = equation[0]
	discriminant = b * b - 4 * a * c
	if discriminant < 0:
		print('Discriminant is strictly negative, no solutions.')
	elif discriminant == 0:
		print('Discriminant is equal to 0, the solution is:')
		print(discriminant_zero(a, b))
	else:
		print('Discriminant is strictly positive, the two solutions are:')
		discriminant_positive(a, b, discriminant)


def resolve_equation(equation, degree):
	if degree == 2:
		second_degree_solution(equation)
	elif degree == 1:
		first_degree_solution(equation)
	else:
		no_degree_solution(equation)


def process_equation(equation):
	output_equation(equation)
	degree = polynomial_degree(equation)
	if degree > 2:
		print('The polynomial degree is strictly greater than 2, I can\'t solve.')
	else:
		resolve_equation(equation, degree)


# if len(sys.argv) == 2:
# 	equation = parse_input(sys.argv[1])
# 	process_equation(equation)
# else:
# 	exit()

equation = parse_input("- 2 * X^0 - 4 * X^1 = 2 * X^0 - 4 * X^1")
process_equation(equation)