### -------------------------------------------
#   This is a python script emulating specific questions
#   from tutorial 1 Exercises. Can be run using the opensource Anaconda
#   python package.
#
#   Author: Aidan Bharath
#           Aidan.Bharath@utas.edu.au
#
### ------------------------------------------

from __future__ import division
import numpy as np


if __name__ == "__main__":

    #### Mathematical calculations with arrays.

    # Now that we can build, arrange and slice numpy arrays it is time to begin
    # solving simple problems with them. As we briefly saw in the first
    # tutorial math functions are applied element by element by default on
    # numpy arrays. This tutorial aims to expand on how to use numpy arrays for
    # math. This will also introduce another package in the numpy namespace,
    # linalg.

    # In the tutorial we can look at problem 5 first. We first h = 2, nu =
    # np.sqrt(2*9.81*2) and t = nu/g. Sweet, first we need to find the initial
    # velocity.

    g , h = 9.81 , 2
    nu = np.sqrt(2*g*h)

    # Now we want the times for the first 8 bounces. Well we have our
    # velocities decreasing by 0.85 on each bounce so we can think of the time
    # equation as 8 instances of different velocities. so lets build the n
    # array

    n = np.linspace(1,8,8)
    t = np.array((nu/g)*(0.85*n))
    print np.concatenate([n[:,None].T,t[:,None].T]).T

    # That is pretty easy. Using n as an array in calculating t creates a new
    # array of t values. But who can tell me why the answer is wrong and the
    # names of the theories used to solve this problem.

    # Now we want to do elementwise calculations with 2 vectors like in
    # question 14. Now lets just start with some basic arrays.

    x = np.linspace(1,10,10)[::2]
    y = np.linspace(1,100,100)[::20]

    # Now for element by element calculations theres really nothing to it.

    z = x*y
    print z
    z = (x**3*np.cos(2.5*y))/(2*np.pi*x*y)
    print z

    # Ya!! You can find in the numpy function databases mostly any function you
    # may want. But this is really not that interesting, lets say you want to
    # calculate z = x*y for every combination of x and y? This starts to get a
    # little nasty and begins to get into for loops and filling predefined
    # arrays .... Not!

    print np.outer(x,y)

    # Fun fact about about this calculation is that it's called an outer
    # product and is defined to do exactly what we want in this case. I we want
    # to calculate the second z function we have to be a little more creative.
    # Lets think about what we realy need here, for each x value we want to
    # apply y to the z function, get an array of results back and repeat for
    # the next x. That is the essence of a for loop, and for completeness we
    # can see what that would look like.

    xs = x.shape[0]
    ys = y.shape[0]
    z_ans = np.zeros([xs,ys])
    for i in range(xs):
        for j in range(ys):
            z_ans[i,j] = (x[i]**3*np.cos(2.5*y[j]))/(2*np.pi*x[i]*y[j])

    print z_ans

    # How gross is that. A nested for loop having to calculate each term in
    # z_ans individually. It works however and it is fairly simple to
    # follow how the solution is calculated. It may be beneficial to begin a
    # piece of code using these loops just to make it work, after it can become
    # clear how to use numpy's or matlab's array functionality to improve your
    # code. What we really need for this calculation is an array of the first
    # value of x, y[:] long and then the second and so on. This is easy.

    print np.tile(x,(5,1))

    # Here tile creates 5 rows of x repeated once. Each row is then a copy of
    # x. If we simply transpose this we will have what we want.

    x = np.tile(x,(5,1)).T
    z = (x**3*np.cos(2.5*y))/(2*np.pi*x*y)
    print z

    # And is it the same as the for loop?
    print z == z_ans

    # sure is. Much prettier solution.

    # Now like in Q 23 we want to start summing vectors. Easy enough. We
    # already know how to construct arrays based on functions so lets do that.

    n = np.linspace(1,20,20)
    n_sum = np.array(1/(2**n)).sum()
    print n_sum

    # Now here to get all of the results we want in this question a,b,c,d we
    # would have to go back redefine n and recalculate. First thought would be
    # to find a tricky numpy function that can do it for us (and there are
    # ways) but it is not simple in this case since n is not a constant size.
    # This case here it become easier to use for loops and lists (remember
    # those).

    values = [10,20,30,50]

    # values now here is defined as a list object containing the n we want.
    # Python syntax allows for loops to be constructed in a nice compact
    # concise way.

    n_sums = [np.array(1/(2**np.linspace(1,ns,ns))).sum() for ns in values]
    print n_sums

    # Using the loop here we populate a new list n_sums based on the numbers in
    # values, and solve all of 23 in 2 lines of code. Nice, 9 points, 10 if you can do
    # it in 1.

    # Now one of the most used features of Matlab is it's linear set of
    # equations solver. Guess what, so does numpy. It is part of the linear
    # algebra package which is part of the numpy module, but who really wants
    # to write out np.linalg.solve() all day to solve these problems. I don't
    # and neither should you. so lets make it simpler by just import the
    # function we need.

    from numpy.linalg import solve

    # I believe I will just make random arrays and solve them.

    from numpy.random import random

    # now we are just left to solve the matrix equation ax = b. lets define a
    # and b.

    a = random([5,5])
    b = random(5)

    print a,b

    x = solve(a,b)

    print x

    # Nothing to it. We can also check to see if the solution is correct as
    # before. This time we can use np.allclose() which looks the entire array
    # elementwise and checks to see if they are equal a little cleaner than the
    # method used previously.

    print np.allclose(np.dot(a,x),b)

    # This shows the simplicity of well thought out python code. Many seeming
    # complicated calculations can be handled quickly and efficiently. Python
    # is itself a programming language with numpy an extension so scripting
    # will have a different feel compared to matlab as it was an array handler
    # first and a program language second. The benefits of this will show
    # themselves slowly.
