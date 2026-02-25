#Chapter 3

#libraries 
import math
import numpy as np 
import matplotlib.pyplot as plt

#Example 1


x = np.linspace(-4,4, 100) 
l = 3 * np.sin(x) + 9
r = x**2 - np.cos(x)

fig, axes = plt.subplots(nrows = 1, ncols = 2)

axes[0].plot(x, l, 'b-.', label=r"$3\sin(x)+9$")
axes[0].plot(x, r, 'r-', label=r"$x^2-\cos(x)$")
axes[0].grid()
axes[0].legend()
axes[0].set_title(r"$3\sin(x)+9 = x^2-\cos(x)$")

axes[1].plot(x, l-r, 'g:', label=r"(3\sin(x)+9) - (x^2-\cos(x))")
axes[1].plot(x, np.zeros(100), 'k-')
axes[1].grid()
axes[1].legend()
axes[1].set_title(r"$(3\sin(x)+9) - (x^2-\cos(x))=0$")

fig.tight_layout()
plt.show()

#3.2.2
#Bisection method function

def bisection(f, a, b, tol=1e-5):
    """
    Find a root of f(x) in the interval [a, b] using the bisection method.

    a and b can not be roots for this function to be accurate.

    Parameters:
        f   : function, the function for which we seek a root
        a   : float, left endpoint of the interval
        b   : float, right endpoint of the interval
        tol : float, stopping tolerance

    Returns:
        float: approximate root of f(x)
    """

    # quick checks:
    # a the root?
    # b the root?
    # a and b have opposite sign 
 
    if np.sign(f(a)) == np.sign(f(b)) or b < a:
        raise ValueError('There is not exactly one root in this interval, adapt domain a or b and ensure b > a')

    #midpoint
    m = (a+b)/2

    while (b - a) > 2 * tol:
        if f(m) == 0:
            break

        elif f(a) * f(m) > 0: #in interval (m,b)
            a = m
            m = (a + b) / 2
            
        elif f(a) * f(m) < 0: # in interval (a,m)
            b = m 
            m = (a + b) / 2
    
    return m

#perfecto
print(bisection( lambda x: (x**2) - 2, 0, 2)) # spot on 

print(bisection(lambda x: np.sin(x) + (x ** 2) - ( 2 * np.log(x)) - 5, 1, 5)) # this is off by 0.29. which is too much. why

print(bisection( lambda x: (3 * np.sin(x)) + 9 - (x ** 2) - np.cos(x), 1, 5 ))

#%% ------------------------------
# Exercise 3.14 
# input number of iterations instead of a given tolerance

def bisection_n(f, a, b, n):
    """
    Find a root of f(x) in the interval [a, b] using the bisection method.

    a and b can not be roots for this function to be accurate.

    Parameters:
        f   : function, the function for which we seek a root
        a   : float, left endpoint of the interval
        b   : float, right endpoint of the interval
        n : integer > 0 , number of iterations

    Returns:
        float: approximate root of f(x)
    """

    # quick checks:
    # a the root?
    # b the root?
    # a and b have opposite sign 
 
    if np.sign(f(a)) == np.sign(f(b)) or b < a:
        raise ValueError('There is not exactly one root in this interval, adapt domain a or b and ensure b > a')

    #midpoint
    m = (a+b)/2

    for i in range(1, n+1):
        if f(m) == 0:
            break

        elif f(a) * f(m) > 0: #in interval (m,b)
            a = m
            m = (a + b) / 2
            
        elif f(a) * f(m) < 0: # in interval (a,m)
            b = m 
            m = (a + b) / 2
    
    return m

print(bisection_n( lambda x: (x**2) - 2, 0, 2, 20))

