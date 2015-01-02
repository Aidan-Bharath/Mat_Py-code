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
    # np.array([]). It is important however to understand how these structures
    # behave. There are several basic types of structures in python but here we
    # will focus on lists, numpy arrays and dict objects.
    l = []  # a list
    a = np.array([]) # a numpy array (or just array)
    d = {} # a dict

    # notice a numpy array is made from a list. As an example,
    l = [i for i in range(10)]
    a = np.array(l)
    print l, a

    # lists are mutable in the sense that their size can change dynamically
    # while an array is immutable meaning that the array size must be
    # known when created. This feature of arrays adds to the speed as which
    # then can handle computations. When created the array is consecutively
    # allocated to memory unlike a list which allows for this.

    # The np.arange command gives an array of integer spaced values.
    print np.arange(0,9)

    # or specified intervals.
    print np.arange(0,9,2)

    # Question 9
    print np.arange(38.5,-3.5,-3.5)

    # we also have the linspace command as does matlab and handles the endpoints
    # and intervals of the created array differently than arange()
    print np.linspace(0,9,10)
    print np.linspace(0,9,5)

    # Question 8
    print np.linspace(81,12,9)

    # Constant arrays can be created with the convenient command np.full().
    print np.full(10,10)

    # can make arrays from arrays.
    print np.array(np.linspace(1,10,10))

    # this can come in handy if you wish to build an array based on a function.
    x = np.linspace(0,9,10)
    y = np.array(x**3)
    print y

    # Notice that the same operation does no work with a list object.
    # y= np.array(l**3)

    # Functions such as cubing cannot be broadcast across list objects meaning
    # that in the previous line python does not know how to apply the function.
    # The function must be applied term by term.
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

    # This is an example of when the memory allocation used in arrays is
    # beneficial. It would seem that lists are a pain, but their use will
    # become apparent in the future. For now we will leave list objects and
    # focus more on arrays.

    # to check the dimensionality of an array we use the shape command.

    x = np.linspace(1,100,100)
    print x.shape
    # x then would be a row vector with 100 elements or an array with 100
    # entries along is first dimension. This can be transposed into
    # a column vector by transposing.

    print x[:,None].T.shape

    # Here we need to be careful with what is happening. matlab will simply
    # use the ' operator after the row vector to transpose it to a column
    # vector but the numpy implementation is slightly involved. Numpy requires
    # us to create to second 'vertical' dimension and then transpose the row
    # into that dimension. This is accomplished with the None or alternatively
    # np.newaxis. It may be thought of as a row vector populating the second
    # dimension (So why make a column vector?).

    # we can join together a number of arrays with numpy stacking commands.

    y = np.linspace(100,1,100)
    z = np.linspace(101,200,100)

    a = np.vstack([x,y,z])
    print a.shape

    # vstack will create and stack row vectors along the second axis. What
    # happens when you vstack two column vectors?

    a = np.hstack([x,y,z])
    print a.shape

    # hstack will stack row vectors in line along the first axis. What happens
    # when you hstack 2 column vectors?

    a = np.dstack([x,y,z])
    print a.shape

    # dstack transposes the rows to column vectors and joins together each
    # column. Notice the output is a three dimensional array. Why?

    # all of these commands are derived from np.concatenate() and can be used
    # to reproduce the same results.

    a = np.concatenate([x[:,None].T,y[:,None].T,z[:,None].T],axis=0)
    b = np.concatenate((x,y,z),axis=0)
    c = np.concatenate([x[:,None].T,y[:,None].T,z[:,None].T],axis=0).T

    print a.shape,b.shape,c.shape





