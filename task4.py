# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:49:42 2026
@author: andrearaaschou

Task 4: Application: Optimization of Himmelblau’s Function
"""
import numpy as np
import matplotlib.pyplot as plt
import task1 as t1
import task2 as t2

def himmelblau_func(x, y):
    return((x**2 + y - 11)**2 + (x + y**2 - 7)**2)

def gradient_descent_alg(f, x1, y1, alpha = 0.01):
    """
    Implements the gradient descent algorithm
    Starts at initial guess (x1, y1)
    Goes towards local minima for 20 steps
    """
    x = []
    y = []
    x.append(x1)
    y.append(y1)
    
    for i in range(20):
        grad_x, grad_y = t2.numerical_gradient(f)(x[i], y[i])
        x.append(x[i] - alpha * grad_x)
        y.append(y[i] - alpha * grad_y)
        
    return(x, y)

  
fig, ax1, ax2 = t1.create_surface_and_contour_plot(*t1.create_xyz(himmelblau_func, -5, 5, -5, 5), 
                                                   "Himmelblau's function")

# Perform the gradient descent for two different starting points
x1, y1 = gradient_descent_alg(himmelblau_func, 0, 0)
x2, y2 = gradient_descent_alg(himmelblau_func, 1/5, -4)

# Add the gradient descent path to the contour plot
ax2.plot(x1, y1, 'r', label='Starting point (0,0)')
ax2.plot(x2, y2, 'b', label='Starting point (0.2,-4)')
ax2.plot(x1[0], y1[0], 'r*', markersize=12)
ax2.plot(x2[0], y2[0], 'b*', markersize=12)
ax2.legend()
plt.show()


# Compute and print gradient and hessian of the finish points for both cases
print("\nApproximated gradient for starting point (0, 0):")
print ((
    float(t2.numerical_gradient(himmelblau_func)(x1[-1], y1[-1])[0]), 
    float(t2.numerical_gradient(himmelblau_func)(x1[-1], y1[-1])[1])
))

print("\nApproximated gradient for starting point (0.2,-4):")
print ((
    float(t2.numerical_gradient(himmelblau_func)(x2[-1], y2[-1])[0]), 
    float(t2.numerical_gradient(himmelblau_func)(x2[-1], y2[-1])[1])
))

hessian1 = t2.numerical_hessian(himmelblau_func)(x1[-1], y1[-1])
hessian2 = t2.numerical_hessian(himmelblau_func)(x2[-1], y2[-1])

print("\nApproximated Hessian for starting point (0, 0):")
print(f'{hessian1[0][0]}  {hessian1[0][1]}')
print(f'{hessian1[1][0]}  {hessian1[1][1]}')

print("\nEigenvalues for starting point (0.2,-4):")
print(np.linalg.eigvals(hessian1))

print("\nApproximated Hessian for starting point (0.2,-4):")
print(f'{hessian2[0][0]}  {hessian2[0][1]}')
print(f'{hessian2[1][0]}  {hessian2[1][1]}')

print("\nEigenvalues for starting point (0.2,-4):")
print(np.linalg.eigvals(hessian2))












