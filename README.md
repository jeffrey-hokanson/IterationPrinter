# IterPrinter: A simple iteration history printer

When using iterative numerical algorithms it is common
to print after each iteration a message so that a user
can monitor convergence and catch any bugs.
For example, in the demo.py file 

<p align="center"><img src="/demo.gif?raw=true"/></p>


# Usage 

```python
from iterprinter import IterationPrinter

# Initialize the printer by passing formatting information each column
printer = IterationPrinter(it = '4d', obj = '16.6e')

# Print a header for the table
printer.print_header(it = 'iter', obj = 'objective')

# Print a normal line of history
printer.print_iter(it = 0, obj = 5e3 )

# If a particular field is not provided, the column is left empty
printer.print_iter(it = 1)

```

For a more complete example, see `demo.py`.
