# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 10:15:02 2026
@author: andrearaaschou

Task 3: Implicit functions
"""
import numpy as np
import  matplotlib.pyplot as plt
from scipy.optimize import fsolve
import task2 as t2
import task1 as t1

DEBUG = False
PLOT_GRAPHS = True

def f(x, y, z):
    return x + 2*y + z + np.e**(2*z) - 1


def plot_3D_surface(x, y, z, title):
    '''
    takes as arguments the list of x values, y values,
    and marix of z values and the title
    plots the surface. works best for functions of x and y
    '''
    fig = plt.figure(figsize=(12, 5))
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_surface(x, y, z)
    ax1.set_title(title)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    fig.show()
    
def calculate_z(f, x, y):
    return fsolve(f, 0, args = (x, y))

def evaluate_z(x_start, x_stop, y_start, y_stop):
    '''
    evaluate z for 10 thousand evenly spaced points
    between the start and stop values,
    only works for specifically this z.
    returns the X, Y, and Z arrays (z is a matrix) 
    '''
    x = np.linspace(x_start, x_stop, 100)
    y = np.linspace(y_start, y_stop, 100)
    X, Y = np.meshgrid(x, y)
    
    root = []
    for x_i in x:
        for y_i in y:
            root.append(calculate_z(f, x_i,y_i))
    root = np.reshape(np.array(root), (100, 100))
    return (X, Y, root)


def taylor_coefficients(f, point=(0, 0)):
    '''
    finds the gradiant and hessian by using functions from task 2
    it uses fsolve from scipy from calculate_z to find a function
    for z. returns a function that is the taylor polynomial.
    '''
    # gradiant only work with 2 variable functions so have to simplify
    z_func = lambda x, y: calculate_z(f, x, y)
    if DEBUG:
        print("constant coefficient:        ", z_func(*point))
        print("first order x coefficient:   ", t2.numerical_gradient(z_func)(*point)[0][0])
        print("first order y coefficient:   ", t2.numerical_gradient(z_func)(*point)[1][0])
        print("second order x coefficient:  ", t2.numerical_hessian(z_func)(*point)[0][0][0]/2)
        print("second order mixed coefficient:  ", t2.numerical_hessian(z_func)(*point)[1][0][0])
        print("second order y coefficient:  ", t2.numerical_hessian(z_func)(*point)[1][1][0]/2)
    polynomial = lambda x, y: (z_func(*point)[0]
    + x * t2.numerical_gradient(z_func)(*point)[0][0]
    + y * t2.numerical_gradient(z_func)(*point)[1][0]
    + x **2 * t2.numerical_hessian(z_func)(*point)[0][0][0]/2
    + x * y * t2.numerical_hessian(z_func)(*point)[1][0][0]
    + y **2 * t2.numerical_hessian(z_func)(*point)[1][1][0]/2 )
    return(polynomial)
 
def taylor_error(Z, Taylor_Z):
    error = np.abs(Z - Taylor_Z)
    return error

if DEBUG:
    a = taylor_coefficients(f)

    
# Make plots
bounds = (-1, 1, -1, 1)

if PLOT_GRAPHS:
    plot_3D_surface(*evaluate_z(*bounds), 
                    'Z surface plot')
    
    plot_3D_surface(*t1.create_xyz(taylor_coefficients(f, point = (0,0)), *bounds),
                 'Surface plot of second order Taylor polynomial')
    
    plot_3D_surface(t1.create_xyz(taylor_coefficients(f, point = (0,0)), *bounds)[0],
                    t1.create_xyz(taylor_coefficients(f, point = (0,0)), *bounds)[1],
                    taylor_error(evaluate_z(*bounds)[2], 
                                t1.create_xyz(taylor_coefficients(f, point = (0,0)), *bounds)[2]),
                    'Surface plot of error for Taylor approximation')



