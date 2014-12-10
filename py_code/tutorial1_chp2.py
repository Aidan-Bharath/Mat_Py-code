### -------------------------------------------
#   This is a python script emulating specific questions
#   from tutorial 1 Exercises. Can be run using the opensource Anaconda
#   python package.
#
#   Author: Aidan Bharath
#           Aidan.Bharath@utas.edu.au
#
### ------------------------------------------

# initial package imports

import timeit as tt
import numpy as np


if __name__ == "__main__":

    #### Chapter 2: array creation.

    # Basic array creation using the numpy package is straight forward using
    # np.array([]). It is import however to understand what types of array
    # structures are being used. There are 3 basic types: lists, array, dict.
    l = []  # a list
    a = np.array([]) # a numpy array
    d = {} # a dict

    # notice a numpy array is made from a list. As an example,
    l = [i for i in range(10)]
    a = np.array(l)
    print l, a

    # The np.arange command gives an array of integer spaced values.
    print np.arange(0,9)

    # or specified intervals.
    print np.arange(0,9,2)

    # Question 9
    print np.arange(38.5,-3.5,-3.5)

    # we also have the linspace command as does matlab and handles the enpoints
    # and intervals of the created array differently than arange()
    print np.linspace(0,9,10)
    print np.linspace(0,9,5)

    # can make arrays from arrays.
    print np.array(np.linspace(1,10,10))

    # Question 8
    print np.linspace(81,12,9)

    # Constant arrays can be created by utilising the broadcasting methods of
    # numpy. First creating an zero array and then filling it.
    print np.full(10,10)

    # this can come in handy if you wish to build an array based on a function.
    x = np.linspace(0,9,10)
    y = np.array(x**3)
    print y

    # Notice that the same operation does no work with a list object.
    # y= np.array(l**3)

    # Functions such as cubing cannot be broadcast accross list objects and
    # the function must be applied term by term.
    y = np.array([l[i]**3 for i in range(len(l))])
    print y

    # Effectively the list must be created first and then build into an array.
    # this can be a time consuming process giving a very large dataset.
    array = '''
    import numpy as np
    a = np.array(np.sqrt(np.linspace(1,10000,10000)))
    '''
    print min(tt.Timer(array).repeat(1,10))

    lists = '''
    import numpy as np
    a = np.array([np.sqrt(i) for i in range(10000)])
    '''
    print min(tt.Timer(lists).repeat(1,10))


    # to check the dimensionality of an array we use the shape command.

    # c then would be a row vector with 100 elements. This can be transposed into
    # a column vector by transposing.



