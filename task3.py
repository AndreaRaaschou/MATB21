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

def taylor_polynomial(z, point=(0, 0) , degree=2):
    def polynomial_return(x, y):
        for i in range(0, degree+1):
            for j in range(0, degree+1-i):
                eee +=1
    return(polynomial_return)

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
    X, Y = np.meshgrid(x, y)
    fig = plt.figure(figsize=(12, 5))
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_surface(X, Y, root)
    ax1.set_title(title)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    fig.show()
    
   
# approximate z
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)

root = []
for x_i in x:
    for y_i in y:
        root.append(fsolve(f, 0, args = (x_i,y_i)))
root = np.reshape(np.array(root), (100, 100))
plot_3D_surface(x, y, root, 'Z surface plot')