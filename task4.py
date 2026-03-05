# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:49:42 2026
@author: andrearaaschou

Task 4: Application: Optimization of Himmelblau’s Function
"""
import numpy as np
import  matplotlib.pyplot as plt
import task3 as f

def himmelblau_func(x, y):
    (x**2 + y - 11)**2 + (x + y**2 - 7)**2
    
def create_xyz(x_start, x_stop, y_start, y_stop):
    x = np.linspace(x_start, x_stop, 100)
    y = np.linspace(y_start, y_stop, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    
    """
    root = []
    for x_i in x:
        for y_i in y:
            root.append(calculate_z(x_i,y_i))
    root = np.reshape(np.array(root), (100, 100))
    """
    return (x, y, z)