# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 13:36:51 2026
@author: andrearaaschou

Task 1: Visualize all functions using plot_surface() and contourf() 
"""
import numpy as np
import  matplotlib.pyplot as plt
from matplotlib import ticker

MAKE_PLOTS = True


# defining all the functions so that we don't get divby0 errors
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


def create_xyz(f, x_start, x_stop, y_start, y_stop):
    """
    take in a function and boundarys,
    return a list with
    - a list with enenly spaced x values
    - a list with enenly spaced y values
    - a matrix with the f(x, y) values where x and why are at
    corresponding indecies
    """
    x = np.linspace(x_start, x_stop, 100)
    y = np.linspace(y_start, y_stop, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    return (X, Y, Z)


def create_surface_and_contour_plot(X, Y, Z, title):
    """
    Creates a figure with two sublots (one contour plot and one surface plot)
    """
    
    # surface plot
    fig = plt.figure(figsize=(12, 5))
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_surface(X, Y, Z)
    ax1.set_title(f'{title} surface plot')
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
        ax2.set_title(f'{title} contour plot')
       
    else: # add valuescale
        cs = ax2.contourf(X, Y, Z, locator = ticker.LogLocator())
        plt.colorbar(cs)
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_title(f'{title} contour plot')
        
    return(fig, ax1, ax2)
    
# Create plots for all functions
if MAKE_PLOTS:
    fig1, ax11, ax12 = create_surface_and_contour_plot(*create_xyz(f1, 0, 2, 0, 2), 'f1')
    fig2, ax21, ax22 = create_surface_and_contour_plot(*create_xyz(f2, -1, 1, -1, 1), 'f2')
    fig3, ax31, ax32 = create_surface_and_contour_plot(*create_xyz(f3, -1, 1, -2, 0), 'f3')
    fig4, ax41, ax42 = create_surface_and_contour_plot(*create_xyz(f4, -3, 5, -3, 7), 'f4')
    fig5, ax51, ax52 = create_surface_and_contour_plot(*create_xyz(f5, -3, 3, -3, 3), 'f5')
    
    plt.show()




