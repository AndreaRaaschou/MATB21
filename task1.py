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

