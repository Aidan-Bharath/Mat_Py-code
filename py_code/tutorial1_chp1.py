### -------------------------------------------
#   This is a python script emulating specific questions
#   from tutorial 1 Exercises. Can be run using the opensource Anaconda
#   python package.
#
#   Author: Aidan Bharath
#           Aidan.Bharath@utas.edu.au
#
### ------------------------------------------

# initial package imports. Python itself is built up of several packages which
# extend the basic functionality of the language. To use then in a script they
# must first be imported similar to C. The statement 'import numpy as np' means
# that we are importing the entire numpy package and specifying np as the
# package name. np is then used to specify what package a function is coming
# from.

from __future__ import division
import sympy as sp
import numpy as np


if __name__ == "__main__":

    # Question 11: Symbolic equation handling. To demostrate function
    # and variable expressions using SymPy a symbolic math package.

    # First variables must be defined as a symbol and the a function
    # may be defined in terms of the symbols/variables.

    a, b = sp.symbols('a b')
    P = 2*sp.pi*sp.sqrt(0.5*(a**2+b**2))
    print P

    # Next assigning a value to a and b. and notice that the function is
    # not fully solved but a pi factor remains.
    print P.subs([(a,9),(b,3)])

    #we get around this using a evalf function.
    print P.evalf(subs={a: 9,b: 3})

    # Notice P, a or b are redefined
    print P,a,b

    # Cool now lets do b.
    P = 2*sp.pi*sp.sqrt(0.5*(a**2+b**2))-20
    b = sp.solve(P.subs(a,b/2),b)

    # here is a work around to solve the two solutions for a. This comes
    # down to data types.
    a = [b[i]/2 for i in range(len(b))]
    print a,b

    # b is defined as a list type object which does not support
    # broadcasting hence the list loop to iterate the solutions for a. Matlab
    # supports this as well.
    # Python broadcasting/Vectorized calculations are extremely useful though
    # so lets see how this works.
    # Just make b a numpy array.
    b = np.array(b) # Note here b has been redefined

    # division on a numpy array is applied elementwise by default.
    a = b/2
    print a, b

    # The how math is applied accross various data types is a major feature of
    # python. With very large dataset these come in handy. (Note I paid no attention
    # to units)

    ##### Q 15 symoblic integration

    # We can of course set up the integral but like matlab it cannot be solved.
    x = sp.symbols('x')
    integ = sp.Integral(x*sp.exp(0.5*x),(x,1,5))
    print integ

    # lets solve this using numpy array functionality.
    x = np.array([1,5])
    a = 1/2

    # after we define each variable we then build an array of the integral solutions.
    sol = np.exp(a*x)*(x-(1/a))/a
    print sol

    # then solve the integral
    integ = sol[1]-sol[0]
    print integ

    # here we notice that indexing in python starts from 0 unlike Matlab which
    # which starts at 1. Another good point here is the distinction between using
    # numpy and smypy. Numpy does not support symbolic expressions and so all variables
    # must be defined unlike smypy functionality. For sybolic math there are other
    # higher level programs such as mathematica or maple which do these very well
    # and with a much more intuitive syntax. However this does show that it is
    # quite possible to do symbolic math in python.



