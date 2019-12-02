def change_sign(value):
    return -value

def absolute(number):
	if number < 0:
		return -number
	return number

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
