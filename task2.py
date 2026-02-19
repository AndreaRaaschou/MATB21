'''
this is the taks 2 task
'''

import numpy as np 
DEBUG = False
SINTEST_GRAD = True
SINTEST_HESSIAN = True

def numerical_partial_wrt_x(f, h=10**(-4)):
    '''
    takes in function and precision and returns function of partial derivative with respect to x 
    '''
    def return_function(x, y):
        return((f(x+h, y) - f(x,y))/h)
    return(return_function)


def numerical_partial_wrt_y(f, h=10**(-4)):
    '''
    takes in function and precision and returns function of partial derivative with respect to x 
    '''
    def return_function(x, y):
        return((f(x, y+h) - f(x,y))/h)
    return(return_function)


def numerical_gradient(f, h=10**(-4)):
    '''
    takes in function and precision and returns function of gradiant at a point
    '''
    def return_function(x, y):
        return((
            numerical_partial_wrt_x(f, h)(x, y),
            numerical_partial_wrt_y(f, h)(x, y)
            ))
    return (return_function)


def numerical_hessian(f, h=10**(-4)):
    '''
    takes in function and precision and reurns the hessian
    '''
    def return_function(x, y):
        return((
            numerical_gradient(numerical_partial_wrt_x(f, h),h)(x, y),
            numerical_gradient(numerical_partial_wrt_y(f, h),h)(x, y)
            ))
    return (return_function)

def sinus_test(x, y):
    return(np.sin(x+y))


if SINTEST_GRAD:
    a, b = np.pi/4, np.pi/4
    print ((
        numerical_gradient(sinus_test, 10**(-10))(a, b)[0]-np.cos(a+b),
        numerical_gradient(sinus_test           )(a, b)[1]-np.cos(a+b)
    ))
    


if SINTEST_HESSIAN:
    a, b = np.pi/4, np.pi/4
    print(numerical_hessian(sinus_test)(a, b)[0][0]+np.sin(a+b))
          

if DEBUG:
    def function_test(x,y):
        return(x**2 + y**2)
    print (numerical_gradient(function_test, 10**(-8))(3, -2))
