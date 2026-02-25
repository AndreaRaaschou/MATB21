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

w = f(0,0,0)

#root = fsolve(func, 0)
root = fsolve(f, 0, args = (0,0))