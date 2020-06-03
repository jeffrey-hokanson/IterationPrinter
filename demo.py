from iterprinter import *


def bisection(f, a, b):
	r""" Compute a root of on [a,b] using the bisection method
	
	NOTE: This is purely a toy example to demonstrate the IterationPrinter.
	Use scipy's bisection instead!
	"""

	fa = f(a)
	fb = f(b) 	
	assert fa*fb < 0, "f(a) and f(b) must have different signs"

	# We initialize the class by passing the format for the values that will appear.
	# Note the rows will appear in the order provided here.
	printer = IterationPrinter(it = '4d', width = '10.3e', fc = '10.3e', a = '16.10e', b = '16.10e')
	# We then print a header message, providing information on what these variables are
	printer.print_header(it = 'iter', width = 'b - a', fc = 'f(c)', a = 'a', b = 'b')

	for it in range(50):
		c = (a + b)/2.
		fc = f(c)

		# This will then print an iteration message aligned with the header.
		printer.print_iter(it = it, width = b - a, fc = fc, a = a, b = b)

		if fc*fa > 0:
			a = c
			fa = fc
		elif fc*fb > 0:
			b = c
			fb = fc
		else:
			return c
		
		if b - a < 1e-15:
			break

	return c

if __name__ == '__main__':
	# Compute the square root of two
	f = lambda x: x**2 - 2.
	bisection(f, 0, 4)	
