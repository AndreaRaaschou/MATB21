# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:52:29 2026
@author: andrearaaschou
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
        x.append(x[i] + alpha * grad_x)
        y.append(y[i] + alpha * grad_y)
        
    return(x, y)

  
fig, ax1, ax2 = t1.create_surface_and_contour_plot(*t1.create_xyz(himmelblau_func, -5, 5, -5, 5), 
                                                   "Himmelblau's function")

# Perform the gradient descent for two different starting points
x1, y1 = gradient_descent_alg(himmelblau_func, 0, -1.5)
x2, y2 = gradient_descent_alg(himmelblau_func, 1/5, -4)

x1 = np.array(x1)
x2 = np.array(x2)
y1 = np.array(y1)
y2 = np.array(y2)

x1 = np.where((x1 > 5) | (x1 < -5), np.nan, x1)
x2 = np.where((x2 > 5) | (x2 < -5), np.nan, x2)
y1 = np.where((y1 > 5) | (y1 < -5), np.nan, y1)
y2 = np.where((y2 > 5) | (y2 < -5), np.nan, y2)

# Add the gradient descent path to the contour plot
ax2.plot(x1, y1, 'r', label='Starting point (0,0)')
ax2.plot(x2, y2, 'b', label='Starting point (0.2,-4)')
ax2.plot(x1[0], y1[0], 'r*', markersize=12)
ax2.plot(x2[0], y2[0], 'b*', markersize=12)
ax2.legend()
plt.show()

