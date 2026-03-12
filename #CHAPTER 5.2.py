#CHAPTER 5.2.4 - Central difference

import numpy as np 
import matplotlib as plt

#Ex 5.19 - Central difference approximation of f'(x) (second order)
def CentralDiff(f, a, b, N):
    #f function
    #a,b interval points
    #N = number of sub intervals

    h = (b - a) / N                  #length of each interval 
    x = np.linspace(a, b, N+1)       # grid points
    y = f(x)                         # function values

    # central difference approximation (vectorized, no loops)
    df = (y[2:] - y[:-2]) / (2*h) 

    return df


#Moodle - calculate the accuracy at a single point, and ratio of error when h smaller

# central difference at a single point function
def CentralDiffPoint(f, x, h):
    return (f(x + h) - f(x - h)) / (2*h)

# function and exact derivative
f = lambda x: np.sin(x) * (1 - x)
f_prime = lambda x: np.cos(x) * (1 - x) - np.sin(x)

# step sizes
h1 = 1/8
h2 = 1/16

# numerical derivatives
approx1 = CentralDiffPoint(f, 1, h1)
approx2 = CentralDiffPoint(f, 1, h2)

# absolute errors
error1 = abs(approx1 - f_prime(1))
error2 = abs(approx2 - f_prime(1))

# ratio of errors
ratio = error1 / error2
print(ratio)



#Ex 5.23 CENTRAL DIFFERENCE
#approximate f''(x) of sin(x)(1-x) using central difference
def SecondDiff(f, a, b, N):
    """
    Compute a second-order central difference approximation
    to the SECOND derivative of f on [a,b].

    Returns a vector of length N-1
    """
    h = (b - a) / N                  # step size
    x = np.linspace(a, b, N+1)       # grid points
    y = f(x)                         # function values
    # second derivative approximation (vectorized, no loops)
    d2f = (y[2:] - 2*y[1:-1] + y[:-2]) / h**2

    return d2f

#test above: 
a = 0
b = 15
h = 0.1
N = int((b - a) / h)

x = np.linspace(a, b, N+1)
f = lambda x: np.sin(x) * (1-x)
f_double_prime = lambda x: -np.sin(x) + x * np.sin(x) - 2 * np.cos(x)
d2f_exact = f_double_prime(x[1:-1])
d2f_approx = SecondDiff(f,a,b,N)

# Pointwise absolute errors
errors = np.abs(d2f_approx - d2f_exact)

# Maximum error
max_error = np.max(errors)
print(max_error)


#Chapter 5.2.5 - second derivative estimation
# plots maximum error of the second-difference approximation versus step size.
def plot_max_second_difference_errors(f, f_double_prime, a, b, H):
    """
    Plot the maximum absolute error in the second difference 
    approximation for the second derivative of f on the interval [a,b]
    """
    # H is a list of step sizes

    MaxError = []  # list to store maximum errors

    for h in H:

        N = int((b - a) / h)        # number of steps
        x = np.linspace(a, b, N+1)  # grid points

        d2f = SecondDiff(f, a, b, N)     # numerical second derivative
        exact = f_double_prime(x[1:-1])  # exact second derivative (exclude endpoints)

        error = abs(exact - d2f)         # pointwise absolute error
        MaxError.append(np.max(error))   # store maximum error for this h

    # log-log plot
    plt.loglog(H, MaxError, 'b*')
    plt.xlabel("h")
    plt.ylabel("Maximum Absolute Error")
    plt.title("Maximum Second Difference Error")
    plt.grid()

    return plt


