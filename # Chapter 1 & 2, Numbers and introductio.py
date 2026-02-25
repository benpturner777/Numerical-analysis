# Chapter 1 & 2, Numbers and introduction

# Exercise 1.3
x = 1 / 10
for n in range(50):
    if x < 0.5 and x > 0:
        x = 2 * x
    else:
        x = 2 * x - 1
    print(x)
# improvements: make code break if x_n = x_k for some k < n

# note that python fucks up after 64 bits - floating point error - floating precision

# Exercise 1.14
sum = 0
for num in range(-1, -24, -1):
    sum += 2**num
    print("current sum = ", sum)
print("final sum = ", sum)

print(2**385)

# CHAPTER 1.3
# Exercise 1.18
import numpy as np

print(np.sqrt(5) ** 2 == 5)  # get false due to floating point arithmatic
print(49 * (1 / 49) == 1)  # get false, should be true
print(7 * (1 / 7) == 1)  # get true. why?
print(np.exp(np.log(3)) == 3)  # get false

# CHAPTER 1.4
print(10**10 + 0.123456789 - 10**10)  
# makes error trying to stroes 10000000000.123456789

# exercise 1.21
import math

print(2 * (math.sin(0.0001) ** 2))
print(1 - math.cos(0.0001))

import matplotlib.pyplot as plt
import numpy as np

#EX 2.6 - 2.8

# plt.plot(x,y), x array, y some function
x = np.arange(-1,1,0.1)
exp = np.exp(x)
constant = np.ones_like(x)
#constant = x **0 
linear = 1 + x
quadratic = 1 + x + (x**2)/2 
cubic = 1 + x + (x**2)/2 + (x**3)/6

plt.plot(x,exp, label = 'exp(x)')
plt.plot(x,constant, label = 'degree 1')
plt.plot(x,linear, label = 'degree 2')
plt.plot(x,quadratic,label = 'degree 3')
plt.plot(x,cubic,label = 'degree 4')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximation of exp(x)')
plt.legend()
plt.show()

def exp_approx(x, n):
    """
    Computes the nth order Taylor series approximation of e^x at x=0.

    Parameters:
    x (float): The value at which to evaluate the approximation.
    n (int): The order of the Taylor series expansion.

    Returns:
    float: The nth order Taylor approximation of e^x.
    """
    if n < 0:
        raise ValueError("n must be at least 0")
    # Start with zero-order approximation
    approximation = 1.0
    # Add higher-order terms
    for i in range(1, n + 1):
        approximation += (x ** i)/ np.prod(range(1, i+1))
    return approximation

#exp(-1) approximation

print('exp(-1) order 6 = ', exp_approx(-1, 6))
print('accuracy of function', (np.abs(exp_approx(-1,20) - np.exp(-1))))


#define a new function that is quicker. 


def my_exp_approx(x,n): 
    """
    Computes the nth order Taylor series approximation of e^x at x=0.

    Parameters:
    x (float): The value at which to evaluate the approximation.
    n (int): The order of the Taylor series expansion.

    Returns:
    float: The nth order Taylor approximation of e^x.
    """   
    if n < 0:
        raise ValueError("n must be at least 0")
    approximation = 1.0
    added = x 
    for i in range (2, n + 1):
        approximation += added 
        added = added * (x / i) 
    return approximation

print(my_exp_approx(-1,10))

# %timeit exp_approx(1.5, 100) #runs function multiple times to approximate how quick 
%timeit my_exp_approx(1.5,100) #200x quicker


#Exericse 2.12: approximation of log(x) 
def log_approx(x,n):
    """
    computes the nth order taylor series approximation of log(x) at x = 1 for n atleast 2 

    Parameters:
    x (float): The value at which to evaluate the approximation.
    n (int): The order of the Taylor series expansion.
    Returns
    float: The nth order Taylor approximation of log(x).
    """   
    if n < 0:
        raise ValueError('n must be at least 0')
    if x < 1:
        raise ValueError('x must be greater than or equal to 1 for this function to work')
    approximation = 0.0 #includes log(1) 
    for i in range(1, n + 1):
        term = ((-1) ** (i + 1)) * ((x - 1) ** i) / i
        approximation += term 
    return  approximation  

print(log_approx(1.1, 3)) #perfecto. 

#Notice this does not work for anything where x <=2. This is because it is outside the boundary of convergence. 

#the above took a while to get right. Start with just getting it right, then try to make it quicker. 
# Clarity > Speed


#Exercise 2.13
# Create a table to calculate truncation errors as the order of a taylor series increases 
#Current code is for how close exp(0.1) is to my_exp_approx(0.1) 
# and exp(0.2) is to my_exp_approx(0.2) and how the difference increases for 0.2 quicker.


# Create table header
print(
    f"{'Order n':<8} | {'f_n(0.1)':<15} | {'ε_n(0.1)':<15} | "
    f"{'f_n(0.2)':<15} | {'ε_n(0.2)':<15} "
)
print("-" * 80)

# Fill in n=0 row
f_n = lambda x: 1
e_n = lambda x: abs(np.exp(x) - f_n(x))
print(
    f"{0:<8} | {f_n(0.1):<15.10g} | {e_n(0.1):<15.10g} | "
    f"{f_n(0.2):<15.10g} | {e_n(0.2):<15.10g} "
)

# Fill in n=1 row
f_n = lambda x: 1 + x
e_n = lambda x: abs(np.exp(x) - f_n(x))
print(
    f"{1:<8} | {f_n(0.1):<15.10g} | {e_n(0.1):<15.10g} | "
    f"{f_n(0.2):<15.10g} | {e_n(0.2):<15.10g} "
)

# Fill in more rows.
for n in range(2,6):
    f_n = lambda x: my_exp_approx(x,n)
    e_n = lambda x: abs(exp_approx(x,n) - np.exp(x))
    print(f"{n:<8} | {f_n(0.1):<15.10g} | {e_n(0.1):<15.10g} | {f_n(0.2):<15.10g} | {e_n(0.2):<15.10g} ")

print('     ') #add space between tables 
#truncation errors decrease with n but increase with x. 

#EXERCISE 2.14 - seeing the relationship between e_n:

#header
print(
    f"{'Order n': <8}' | {'ε_n(0.1)': <15} | {'ε_n(0.2)': <15} | {'ε_n(0.2) / ε_n(0.1)'}"
)
#fill in rows 
for n in range(0,6):
    e_n1 = lambda x: abs(exp_approx(x,n) - np.exp(x))
    print(
        f"{n:<8} | {e_n(0.1):<15.10g} | {e_n(0.2):<15.10g} | "
        f"{(e_n(0.2) / e_n(0.1)) :<15.10g} "
    )

#%% EXAM 1





