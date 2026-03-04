#Chapter 4 - Roots 2
#code to format a table: 
def table(f, fprime, x0):
    for i in range(5):
        print(f"{i:<2} | x={x0:<20.10g} | f(x) = {f(x0):<25.10g} | f'(x)={fprime(x0):<25.10g}")
        x0 = x0 - f(x0) / fprime

#libraries
import numpy as np 
import math


#newton method with given tolerance to estimate root:
def newton(f, fprime, x0, tol=1e-10):
    """
    Find root of f(x) using Newton's Method.
    
    Parameters:
        f (function): Function whose root we want to find
        fprime (function): Derivative of f
        x0 (float): Initial guess for the root
        tol (float, optional): Error tolerance. Defaults to 1e-10
        
    Returns:
        float: Approximate root of f(x)
        or error message if method fails
    """
    
    # Set x equal to initial guess x0
    x = x0

    # Loop for maximum of 30 iterations:
    for i in range(31):

        if fprime(x0) == 0:
            return ValueError('fprime(x) equals 0 causing error - adapt x0')

        x_new = x - (f(x) / fprime(x))

        if np.abs(x_new - x) < tol:
            return x_new

        else:
            x = x_new

    return 'function does not converge'

#-----------------------------
f = lambda x: (x**2) - 2
fprime = lambda x: 2 * x
print(newton(f,fprime,1))




#exercise 4.1.4
def newton_with_error_tracking(f, fprime, x0, x_exact, tol = 1e-10):
    #f = function
    #fprime = df/dx
    #x0 = first point to iterate
    #x_exact = exact root 
    #return list of errors 

    #initialise list
    errors = [] 
    x = x0
    x_new = x - (f(x) / fprime(x))

    for i in range(31):
        if np.abs(x - x_new) < tol:
            return errors
        elif fprime(x) == 0:   #ensure derivative non-zero
            return ValueError('fprime(x) equals 0 causing error - adapt x0')
        x = x_new
        error = float(np.abs(x_new - x_exact))
        errors.append(error)
        x_new = x - (f(x) / fprime(x))
    return errors and 'f does not converge within tolerance'



f = lambda x: (x ** 2) - 2 
fprime = lambda x: 2 * x
print(newton_with_error_tracking(f, fprime, 1, np.sqrt(2)))


