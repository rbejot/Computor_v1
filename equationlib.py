import mathlib

def simplify_equation(old_value, new_value, sign):
	if sign:
		new_value = mathlib.change_sign(new_value)
	return old_value + new_value

def reduced_form(equation):
	equation_str = ''
	for k, v in equation.items():
		if v < 0:
			equation_str += '- '
		elif k > 0:
			equation_str += '+ '
		if v == int(v):
			equation_str += str(mathlib.absolute(int(v))) + ' ' + '* ' + 'X^' + str(k) + ' '
		else:
			equation_str += str(mathlib.absolute(v)) + ' ' + '* ' + 'X^' + str(k) + ' '
	if len(equation_str) == 0:
		return 'Bad input'
	return 'Reduced form: ' + equation_str + '= 0'

def polynomial_degree(equation):
	if len(equation) > 0:
		degree = equation.keys()[-1]
	else:
		exit()
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
	a = mathlib.float_check(a)
	a = mathlib.change_sign(a)
	solution = a / b
	solution = mathlib.float_check(solution)
	print('The solution is:')
	print(solution)

def second_degree_solution(equation):
	a = equation[2]
	b = equation[1]
	c = equation[0]
	discriminant = b * b - 4 * a * c
	if discriminant < 0:
		print('Discriminant is strictly negative, 2 complex solutions.\n')
		discriminant_negative(a, b, discriminant)
	elif discriminant == 0:
		print('Discriminant is equal to 0, the solution is:')
		print(discriminant_zero(a, b))
	else:
		print('Discriminant is strictly positive, the two solutions are:')
		discriminant_positive(a, b, discriminant)

def discriminant_zero(a, b):
	solution = - b / (2 * a)
	return solution

def discriminant_positive(a, b, discriminant):
	first_solution = (- b - mathlib.sq_rt(discriminant)) / (2 * a)
	second_solution = (- b + mathlib.sq_rt(discriminant)) / (2 * a)
	first_solution = mathlib.float_check(first_solution)
	second_solution = mathlib.float_check(second_solution)
	print(mathlib.number_round(first_solution))
	print(mathlib.number_round(second_solution))

def discriminant_negative(a, b, discriminant):
	delta_symbol = u"\u0394".encode('utf8')
	sqrt_symbol = u"\u221A".encode('utf8')
	solution_one = '(- b - i{}-{}) / 2a'.format(sqrt_symbol, delta_symbol)
	print("First complex solution " + solution_one + " :")
	if b < 0:
		neg = ''
	else:
		neg = '-' 
	b = mathlib.absolute(b)
	first_solution = '({} {} - i{}{}) / {}'.format(neg, mathlib.float_check(b), sqrt_symbol, mathlib.float_check(discriminant), 2 * mathlib.float_check(a))
	print(first_solution + '\n')
	solution_two = '(- b + i{}-{}) / 2a'.format(sqrt_symbol, delta_symbol)
	print('Second complex solution ' + solution_two + " :")
	second_solution = '({} {} + i{}{}) / {}'.format(neg, mathlib.float_check(b), sqrt_symbol, mathlib.float_check(discriminant), 2 * mathlib.float_check(a))
	print(second_solution)

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