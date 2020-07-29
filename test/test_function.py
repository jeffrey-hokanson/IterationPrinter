from iterprinter import IterationPrinter


def test_function():
	r""" Simply check that the library works
	"""

	printer = IterationPrinter(it = '4d', obj = '15.10e')
	printer.print_header(it = 'iter', obj = 'objective')
	printer.print_iter(it = 5, obj = 1e-4)
