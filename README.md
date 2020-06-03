# IterPrinter: A simple iteration history printer

When using iterative numerical algorithms it is common
to print after each iteration a message so that a user
can monitor convergence and catch any bugs.
As an example, `demo.py` implements a simple bisection algorithm
for computing the square root of two. 
The following is the output using this library:

```
 iter │   b - a    │    f(c)    │        a         │        b         │
──────┼────────────┼────────────┼──────────────────┼──────────────────┤
    0 │  4.000e+00 │  2.000e+00 │ 0.0000000000e+00 │ 4.0000000000e+00 │
    1 │  2.000e+00 │ -1.000e+00 │ 0.0000000000e+00 │ 2.0000000000e+00 │
    2 │  1.000e+00 │  2.500e-01 │ 1.0000000000e+00 │ 2.0000000000e+00 │
    3 │  5.000e-01 │ -4.375e-01 │ 1.0000000000e+00 │ 1.5000000000e+00 │
    4 │  2.500e-01 │ -1.094e-01 │ 1.2500000000e+00 │ 1.5000000000e+00 │
    5 │  1.250e-01 │  6.641e-02 │ 1.3750000000e+00 │ 1.5000000000e+00 │
    6 │  6.250e-02 │ -2.246e-02 │ 1.3750000000e+00 │ 1.4375000000e+00 │
    7 │  3.125e-02 │  2.173e-02 │ 1.4062500000e+00 │ 1.4375000000e+00 │
    8 │  1.562e-02 │ -4.272e-04 │ 1.4062500000e+00 │ 1.4218750000e+00 │
    9 │  7.812e-03 │  1.064e-02 │ 1.4140625000e+00 │ 1.4218750000e+00 │
   10 │  3.906e-03 │  5.100e-03 │ 1.4140625000e+00 │ 1.4179687500e+00 │
   11 │  1.953e-03 │  2.336e-03 │ 1.4140625000e+00 │ 1.4160156250e+00 │
``` 

