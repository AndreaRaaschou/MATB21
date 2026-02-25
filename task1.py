# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 13:36:51 2026
@author: andrearaaschou

Task 1: Visualize all functions using plot_surface() and contourf() 
"""
import numpy as np
import  matplotlib.pyplot as plt
from matplotlib import ticker

def f1(x, y):
    with np.errstate(divide='ignore', invalid='ignore'):
        z = (x**2 - x*y) / (x**2 - y**2)
    return z

def f2(x, y):
    with np.errstate(divide='ignore', invalid='ignore'):
        z = (x**2 + y**2)/ (x**2 + x*y + y**2)
    return z

def f3(x, y):
    with np.errstate(divide='ignore', invalid='ignore'):
        z = (np.sin(x + x*y) - x - x*y)/ (x**3*(y + 1)**3)
    return z
    
def f4(x, y):
    return 8*x*y - 4*x**2*y - 2*x*y**2 + x**2*y**2
    
def f5(x, y):
    return (x**2 + 3*x**2)*np.e**(-x**2 - y**2)

def plot_function(f, x_start, x_stop, y_start, y_stop):
    """
    Creates a figure with two sublots (one contour plot and one surface plot)
    """
    # create x, y and z-values
    x = np.linspace(x_start, x_stop, 100)
    y = np.linspace(y_start, y_stop, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    
    # surface plot
    fig = plt.figure(figsize=(12, 5))
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_surface(X, Y, Z)
    ax1.set_title(f'{f.__name__} Surface plot')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    
    # contour plot
    ax2 = fig.add_subplot(122)

    
    if np.any(Z <= 0): # if any values are 0 or negative - do not add valuescale
        Z = np.where(np.isfinite(Z), Z, np.nan)
        cs = ax2.contourf(X, Y, Z)
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_title(f'{f.__name__} contour plot')
       
    else: # add valuescale
        cs = ax2.contourf(X, Y, Z, locator = ticker.LogLocator())
        plt.colorbar(cs)
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_title(f'{f.__name__} contour plot')
            
        
    fig.show()
    
# Create plots for all functions
plot_function(f1, 0, 2, 0, 2)
plot_function(f2, -1, 1, -1, 1)
plot_function(f3, -1, 1, -2, 0)
plot_function(f4, -3, 5, -3, 7)
plot_function(f5, -3, 3, -3, 3)



