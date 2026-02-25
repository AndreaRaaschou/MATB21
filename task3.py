# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 10:15:02 2026
@author: andrearaaschou

Task 3: Implicit functions
"""
import numpy as np
import  matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x, y, z):
    return x + 2*y + z + np.e**(2*z) - 1

def func(z):
    dzdx = - 1 / (1 + 2*np.e**(2*z))
    dzdy = - 2 / (1 + 2*np.e**(2*z))
    return [dzdx, dzdy]

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

#root = fsolve(func, 0)
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)


root = []
for x_i in x:
    for y_i in y:
        root.append(fsolve(f, 0, args = (x_i,y_i)))
root = np.array(root)
root = np.reshape(root, (100, 100))


# surface plot for z(x,y)
fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, root)
ax1.set_title(f'Z surface plot')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

