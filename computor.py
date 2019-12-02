#!/usr/bin/env python
import sys
import input
import equationlib

if len(sys.argv) == 2:
	equation = input.parse_input(sys.argv[1])
	equationlib.process_equation(equation)
else:
	exit()