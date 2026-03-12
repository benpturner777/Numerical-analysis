#Chapter 5.2 - Calculus - Differentiation with finite differences


plot_
#%%

#Libraries
import numpy as np
import matplotlib.pyplot as plt

#Exercise 5.11 - Approximate f'x - outputs errors as h gets smaller using the delta_f function
    
#the following table shows errors from approximation to actual
f = lambda x: np.sin(x) * (1 - x)
exact = -np.sin(1)
delta_f = lambda h: (f(1 + h) - f(1)) / h

#table of errors with the approximation
# Create table header
hdr1 = "h"
hdr2 = "Δf(1)"
hdr3 = "|f'(1) - Δf(1)|"
hdr4 = "Error reduction factor"
print(f"{hdr1:<20} | {hdr2:<18} | {hdr3:<18} | {hdr4:<18}")
print("-" * 82)
    
# Fill in n=1 row
h = 2**(-1)
h_str = f"2^-1 = {h:g}"
error = abs(exact - delta_f(h))
print(f"{h_str:<20} | {delta_f(h):<18.15f} | {error:<18.15f} |")
    
# Fill in n=2 row
h = 2**(-2)
h_str = f"2^-2 = {h:g}"
error_prev = error
error = abs(exact - delta_f(h))
print(f"{h_str:<20} | {delta_f(h):<18.15f} | {error:<18.15f} | {error_prev/error:<18.15f}")

for i in range(3,11):
    h = 2**i 
    error_prev = error
    error = abs(exact - delta_f(h))
    print(f"{h_str:<20} | {delta_f(h):<18.15f} | {error:<18.15f} | {error_prev/error:<18.15f}")


#------------------------------------

#Plot error of approximation vs h (5.11) 
def plot_forward_difference_errors(f, x, exact, H):
    """
    Plot the absolute error in the finite difference approximation

    Parameters:
        f (function): Function whose derivative we approximate
        x (float): The point at which we want the derivative
        exact (float): The exact value of f'(x)
        H (vector): We will calculate the error at each of the
                    entries of this vector
    Returns:
        A plot with the stepsizes on the x axis and the 
        absolute error on the y axis
    """

    # Create list of errors
    AbsError = [] # start off with a blank list of errors
    for h in H:
        approx = (f(x+h) - f(x))/h
        AbsError.append(abs(approx - exact))

    # Make a loglog plot
    plt.loglog(H, AbsError, 'b*')
    plt.xlabel("h")
    plt.ylabel("Absolute Error")
    plt.title("Absolute Error vs. h - exercise 5.11")
    plt.grid()
    return(plt)


#Using the above function to plot:
# Setup function and exact derivative
f = lambda x: np.sin(x) * (1 - x)
x = 1
exact = -np.sin(x)
H = [2**(-n) for n in range(1, 11)] #where we want to calculate the error

# Plot the absolute error
plot_forward_difference_errors(f, x, exact, H)



#%% 
# forward difference approximation at every point on a number line (equal intervals)

# Exercise 5.13 - Function to create vector of forward differences:
def ForwardDiff(f,a,b,N):
    x = np.linspace(a,b,N+1) 
    h = x[1] - x[0] 
    y = f(x) 
    df = (y[1:] - y[:-1]) / h 
    return df

#using the above function
f = lambda x: np.sin(x) #f(x) real 
exact_df = lambda x: np.cos(x) #f'(x) real
a = 0
b = 2 * np.pi
N = 1000 #N intervals  
df = ForwardDiff(f,a,b,N) 


#Visual evaluation of Forward differences function.
x = np.linspace(a,b,N+1) # N intervals requires N + 1 points.
plt.plot(x,f(x),'b',x,exact_df(x),'r--',x[0:-1], df, 'k-.')
plt.grid()
plt.legend(['f(x) = sin(x)',
            'exact first deriv',
            'approx first deriv'])
plt.show()


#Exercise 5.15. Using above function 
# to plot a first order approximation of derivative of f(x) = sin(x)(1-x) (RHS)
# And the absolute errors (LHS)
f = lambda x: np.sin(x) * (1 - x)
a = 0
b = 15
N = 1000
x = np.linspace(a,b,N+1) #x values (actual)
y = f(x) # y values (actual)
df = ForwardDiff(f,a,b,N) #vector of finite differences

#left plot: function vs finite difference
fig, ax = plt.subplots(1,2) 
ax[0].plot(x,y,'b',x[0:-1],df,'r--') 
ax[0].grid()
ax[0].set_title("Function vs Finite Difference Approximation")
ax[0].set_xlabel("x")
ax[0].set_ylabel("y")
fig.suptitle("Forward Difference Approximation")

#right plot - absolute errors
exact = lambda x: - np.sin(x) + (1-x) * np.cos(x) #actual derivative
ax[1].semilogy(x[0:-1],abs(exact(x[0:-1]) - df))
ax[1].grid()
ax[1].set_title("Absolute Error")
ax[1].set_xlabel("x")
ax[1].set_ylabel("Error")
fig

#%%
#Exercise 5.16 
# 
# a) first derivative approx
approx = ForwardDiff(f,0,15,150)

# b) absolute difference between approx first derivative and actual
f_prime = lambda x: - np.sin(x) + (1-x) * np.cos(x)
actual = f_prime(np.linspace(0, 15, 150))
difference = np.abs(approx - actual)

# c) find max difference
max = np.max(difference)
print(max)







def plot_max_forward_difference_errors(f, f_prime, a, b, H):
    """
    Plot the maximum absolute error in the forward difference 
    approximation for the first derivative of f on the interval [a,b]
    """
    #H is a list of step sizes

    MaxError = []  # list to store maximum errors

    for h in H:

        N = int((b - a) / h)            # number of steps
        x = np.linspace(a, b, N+1)      # grid points

        df = ForwardDiff(f, a, b, N)    # numerical derivative
        exact = f_prime(x[0:-1])        # exact derivative (exclude right endpoint)

        error = abs(exact - df)         # pointwise absolute error
        MaxError.append(np.max(error))  # store maximum error for this h

    # log-log plot (same style as previous function)
    plt.loglog(H, MaxError, 'b*')
    plt.xlabel("h")
    plt.ylabel("Maximum Absolute Error")
    plt.title("Maximum Forward Difference Error")
    plt.grid()

    return(plt)


H = [2**(-n) for n in range(1, 11)] #list of step sizes

plot_max_forward_difference_errors(f,f_prime, 0,15, H)





    

#%%
