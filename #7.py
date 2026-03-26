#7.1 - Ode part 1 
import numpy as np
import matplotlib.pyplot as plt 

def euler_1d(f, x0, t0, tmax, dt):
    """
    Solves a first-order ordinary differential equation using the Euler method.

    Parameters:
        f    : function, the function defining the differential equation. It should
               take two arguments, the independent variable t and the dependent
               variable x, and return the derivative of x with respect to t.
        x0   : float, the initial value of the dependent variable.
        t0   : float, the initial value of the independent variable.
        tmax : float, the maximum value of the independent variable.
        dt   : float, the time step.

    Returns:
       tuple containing two numpy arrays:
            - t : vector of time values.
            - x : vector of solution values at each time value.
    """
    # We need an integer number of steps so we round the number of steps
    # and then adjust dt to match.
    N = round((tmax - t0)/dt)
    dt = (tmax - t0)/N

    # Set up the time grid
    t = np.linspace(t0, tmax, N+1)
    # set up an array for x that is the same size as t
    x = np.zeros(len(t))

    # initial condition
    x[0] = x0

    for n in range(N): 
        x[n+1] = x[n] + dt * (f(t[n], x[n]))
    return t, x

f = lambda t, x: -x + np.sin(t/2)
x0 = 1
t0 = 0 
tmax = 10 
dt = 1
print(euler_1d(f,x0,t0,tmax,dt))


#Test the above code by visualising it

# Define the function giving x' in terms of t and x
f = lambda t, x : -(1/3) * x + np.sin(t)
x0 = 1   # initial condition
t0 = 0   # initial time
tmax = 10 # final time
dt = 0.1   # time step (your choice, but make it small)
t, x = euler_1d(f, x0, t0, tmax, dt)
plt.plot(t, x, 'b-', label='Euler')

# Actual analytic solution
x_exact = lambda t: (1/10) * (19 * np.exp(-t / 3) + 3* np.sin(t) - 9 * np.cos(t))
# plot the exact solution at a higher resolution
t_highres = np.linspace(t0, tmax, 100)
plt.plot(t_highres, x_exact(t_highres), 'r--', label='Exact')
plt.grid()
plt.show()


#Calculate errors: 

# Create vector with different step sizes
dt = 10**(-np.linspace(0, 4, 50))
# Create vector with the same size as dt for holding the errors
errors = np.zeros_like(dt)
# Loop over the different step sizes to calculate the errors
for i in range(len(dt)):
    # Approximate the solution with Euler's method
    t, x = euler_1d(f, x0, t0, tmax, dt[i])
    errors[i] = np.max(np.abs(x - x_exact(t))) # Calculate maximum absolute error

# Plot the errors with logarithmic axes
plt.loglog(dt, errors)
plt.xlabel('Step size')
plt.ylabel('Maximum error')
plt.grid()





#---------CHAPTER 7.2--------------

def euler(F, x0, t0, tmax, dt):
    """
    Solves a system of first-order ordinary differential equations
    using the Euler method.

    Parameters:
        F : function, the function defining the system of differential equations.
            It should take two arguments, the independent variable t and the
            dependent variable x (as a 1D numpy array), and return the
            derivative of x with respect to t (as a 1D numpy array).
        x0 : numpy vector, the initial values of the dependent variables.
        t0 : float, the initial value of the independent variable.
        tmax : float, the maximum value of the independent variable.
        dt : float, the time step.

    Returns:
        tuple containing two numpy arrays:
            - t : vector of time values.
            - x : array of solutions at each time value. Each column of x
                  corresponds to a different dependent variable.
    """

    N = round((tmax - t0)/dt)
    dt = (tmax - t0)/N
    # Set up the time grid
    t = np.linspace(t0,tmax,N+1)
    # set up an array for x with one row for each dependent variable and one column
    # for each grid point
    x = np.zeros((len(t), len(x0)))
    # store the initial condition in the first row of x
    x[0, :] = x0
    # loop over the different time steps
    for n in range(N):
        x[n+1, :] = x[n, :] + dt * F(t[n], x[n, :])
    return t, x

m = 2
b = 4
k = 128
F = lambda t, x: np.array([x[1], -(b/m)*x[1] - (k/m)*x[0]])
x0 = [-0.2, 0.6] # initial conditions
t0 = 0
tmax = 5  
dt = 0.001
t, x = euler(F, x0, t0, tmax, dt)

plt.plot(t, x[:, 0], 'b-', t, x[:, 1], 'r--')
plt.grid()
plt.title('Time Evolution of Position and Velocity')
plt.legend(['position','velocity'])
plt.xlabel('time')
plt.ylabel('position and velocity')
plt.show()

plt.plot(x[:, 0], x[:, 1])
plt.grid()
plt.title('Phase Plot')
plt.xlabel('position')
plt.ylabel('velocity')
plt.show()





