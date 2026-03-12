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

DEBUG = True

def f(x, y, z):
    return x + 2*y + z + np.e**(2*z) - 1

def factorial(x):
    if x == 0:
        return(1)
    return(x*factorial(x-1))

# note: we have to modify our partial codes so we can't just import them from previous tasks
def numerical_partial_wrt_x(f, h=10**(-7)):
    '''
    takes in function and precision and returns function of partial derivative with respect to x 
    '''
    def return_function(x, y, z):
        return((f(x+h, y, z) - f(x,y, z))/h)
    return(return_function)


def numerical_partial_wrt_y(f, h=10**(-7)):
    '''
    takes in function and precision and returns function of partial derivative with respect to y 
    '''
    def return_function(x, y, z):
        return((f(x, y+h, z) - f(x,y, z))/h)
    return(return_function)

def numerical_partial_wrt_z(f, h=10**(-7)):
    '''
    takes in function and precision and returns function of partial derivative with respect to z 
    '''
    def return_function(x, y, z):
        return((f(x, y, z+h) - f(x,y, z))/h)
    return(return_function)

def plot_3D_surface(x, y, z, title):
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
    x = np.linspace(x_start, x_stop, 100)
    y = np.linspace(y_start, y_stop, 100)
    X, Y = np.meshgrid(x, y)
    
    root = []
    for x_i in x:
        for y_i in y:
            root.append(calculate_z(f, x_i,y_i))
    root = np.reshape(np.array(root), (100, 100))
    return (X, Y, root)





''' #anything past this point is just wrong and bad
def partial_multiindex(f, alpha = (0,0,0)):
    temp = f
    for i in range(alpha[0]):
        temp = numerical_partial_wrt_x(temp)
    for i in range(alpha[1]):
        temp = numerical_partial_wrt_y(temp)
    for i in range(alpha[2]):
        temp = numerical_partial_wrt_z(temp)
    return(temp)

def partial_of_z_multiindex(f, alpha):
    # what we want is the formula dz/dx = - df/dx / df/dz ball (x, y, z(x, y))
    
    return(0)

def taylor_polynomial(f, point = (0, 0), degree = 2):
    list_of_functions = []
    for i in range(0, degree):
        for j in range(0, degree-i):
            list_of_functions.append(0)
    def  return_function(x, y):
        for i in list_of_functions:
            sum += i(x, y)
        return(sum)
    
    return(return_function)

 #this shit is functional and too wacky
def taylor_polynomial_of_z(f, point=(0, 0) , degree=2):
    def x_partials(temp, i = 0):
        if i > degree:
            return(temp)
        def y_partials(temp, j = 0):
            if i+j > degree:
                return(temp)
        return(y_partials(
    return(return_polynomial)

def onevartaylorfunctional(f, x = 0, degree = 0, max = 2):
    if degree == max:
        return(f)
    return(lambda x, y, z :
        numerical_partial_wrt_x(
            onevartaylorfunctional(f, x, degree+1)
            , h = 10**(-3))(x, y, z)
        /factorial(degree)
        + f(x, y, z))

def twovartaylorfunctional(f, point = (0, 0), degree = 0, max= 2):
    if degree == max:
        return(f)
    return(
        lambda x, y, z :
        numerical_partial_wrt_x(onevartaylorfunctional(f, x, degree+1), h = 10**(-3))(x, y, z)
        /factorial(degree))

#print(onevartaylorfunctional(lambda x, y, z : np.exp(x), degree = 1)(0.2, 0, 0))
'''


def taylor_coefficients(f, point=(0, 0)):
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

plot_3D_surface(*evaluate_z(*bounds), 
                'Z surface plot')

plot_3D_surface(*t1.create_xyz(taylor_coefficients(f, point = (0,0)), *bounds),
    'Surface plot of second order Taylor polynomial')

plot_3D_surface(t1.create_xyz(taylor_coefficients(f, point = (0,0)), *bounds)[0],
                t1.create_xyz(taylor_coefficients(f, point = (0,0)), *bounds)[1],
                taylor_error(evaluate_z(*bounds)[2], 
                             t1.create_xyz(taylor_coefficients(f, point = (0,0)), *bounds)[2]),
                'Surface plot of error for Taylor approximation')



