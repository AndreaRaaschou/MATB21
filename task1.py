# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 13:36:51 2026
@author: andrearaaschou
"""
import numpy as np
import  matplotlib.pyplot as plt

# Task 1

# Visualize all functions using plot_surface() and contourf() 

def f1(x, y):
    (x**2 - x*y)/(x**2 - y**2)

def f2(x, y):
    (x**2 + y**2)/(x**2 + x*y + y**2)

def f3(x, y):
    (np.sin(x + x*y) - x - x*y)/(x**3 (y + 1)**3)
    
def f4(x, y):
    8*x*y - 4*x**2*y - 2*x*y**2 + x**2*y**2
    
def f5(x, y):
    (x**2 + 3*x**2)*np.e**(-x**2 - y**2)

