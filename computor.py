#!/usr/bin/env python
import sys
argv = "- 13 * X^0 = 1.2 * X^0 + 1 * X^1"

equation = {
    'polynome': {
        'x0': 0,
        'x1': 0,
        'x2': 0
    },
    '=': {
        'x0': 0,
        'x1': 0,
        'x2': 0
    }
}

i = 0
argv_elements = argv.split(' ')
before_equal = True
while i < len(argv_elements):        
    if argv_elements[i] == 'X^0':
        if before_equal:
            equation['polynome']['x0'] = argv_elements[i - 2]
            if argv_elements[i - 3] == '-' or argv_elements[i - 3] == '+':
                equation['polynome']['x0'] = argv_elements[i - 3] + argv_elements[i - 2]
        else:
            equation['=']['x0'] = argv_elements[i - 2]
            if argv_elements[i - 3] == '-' or argv_elements[i - 3] == '+':
                equation['=']['x0'] = argv_elements[i - 3] + argv_elements[i - 2]
    if argv_elements[i] == '=':
        before_equal = False
    i += 1

print argv_elements
print equation


