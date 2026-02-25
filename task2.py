'''
Task 2: Partial Derivatives, Gradients, and Hessians
'''

import numpy as np 
import matplotlib.pyplot as plt
import task1 as t1

DEBUG = False
SINTEST_GRAD = True
SINTEST_HESSIAN = True
EQTEST_5 = True

def numerical_partial_wrt_x(f, h=10**(-7)):
    '''
    takes in function and precision and returns function of partial derivative with respect to x 
    '''
    def return_function(x, y):
        return((f(x+h, y) - f(x,y))/h)
    return(return_function)


def numerical_partial_wrt_y(f, h=10**(-7)):
    '''
    takes in function and precision and returns function of partial derivative with respect to y 
    '''
    def return_function(x, y):
        return((f(x, y+h) - f(x,y))/h)
    return(return_function)


def numerical_gradient(f, h=10**(-7)):
    '''
    takes in function and precision and returns function of gradiant at a point
    '''
    def return_function(x, y):
        return((
            numerical_partial_wrt_x(f, h)(x, y),
            numerical_partial_wrt_y(f, h)(x, y)
            ))
    return (return_function)


def numerical_hessian(f, h=10**(-7)):
    '''
    takes in function and precision and returns the hessian
    '''
    def return_function(x, y):
        return((
            numerical_gradient(numerical_partial_wrt_x(f, h),h)(x, y),
            numerical_gradient(numerical_partial_wrt_y(f, h),h)(x, y)
            ))
    return (return_function)

def sinus_test(x, y):
    return(np.sin(x+y))

def plot_changing_h(start, stop):
    '''
    takes in first and last h-values and plots the euclidean norm of the error 
    different h-values
    '''
    h = np.logspace(np.log10(start), np.log10(stop), 100)
    a, b = np.pi/4, np.pi/4
    errors = []
    
    for h_i in h:
        error = numerical_gradient(sinus_test, h_i)(a,b)
        error_norm = np.linalg.norm(error)
        errors.append(error_norm)
  
    fig, ax = plt.subplots()
    ax.loglog(h, errors, '.')
    ax.set_xlabel('h')
    ax.set_ylabel('Error (euclidean norm)')
    ax.set_title('What happens with the error when you change h? (a,b) = (pi/4, pi/4)')
    fig.show()




if SINTEST_GRAD:
    a, b = np.pi/4, np.pi/4
    print('\n-------- sin(x + y) -----------')
    print("\nApproximated gradient:")
    print ((
        float(numerical_gradient(sinus_test)(a, b)[0]), 
        float(numerical_gradient(sinus_test)(a, b)[1])
    ))
    
    print("\nAnalytical gradient:")
    print("(0, 0)")
    
    print("\nApproximated gradient error:")
    print ((
        float(numerical_gradient(sinus_test)(a, b)[0]-np.cos(a+b)), 
        float(numerical_gradient(sinus_test)(a, b)[1]-np.cos(a+b))
    ))
    
    plot_changing_h(10**(-9), 10**(-1))

if SINTEST_HESSIAN:
    a, b = np.pi/4, np.pi/4
    hessian = numerical_hessian(sinus_test)(a, b)
    
    print("\nApproximated Hessian:")
    print(f'{hessian[0][0]}  {hessian[0][1]}')
    print(f'{hessian[1][0]}  {hessian[1][1]}')
    
    print("\nAnalytical Hessian:")
    print("-1   -1")
    print("-1   -1")
    
    print("\nApproximated Hessian error (will be same for all entries):")
    print(numerical_hessian(sinus_test)(a, b)[0][0]+np.sin(a+b))
    
    
          
if EQTEST_5:
    # Testing f5 which has critical points at (±1, 0)
    print('\n-------- (x^2 + 3x^2)e^(-x^2 - y^2) -----------')
    a, b = 1, 0
    
    # Gradient
    grad = numerical_gradient(t1.f5)(a, b)
    print("\nApproximated gradient:")
    print(grad)
    
    # Hessian
    hessian = numerical_hessian(t1.f5)(a, b)
    print("\nApproximated Hessian:")
    print(f'{hessian[0][0]}  {hessian[0][1]}')
    print(f'{hessian[1][0]}  {hessian[1][1]}')
    print(f'\nThe eigenvalues of the hessian are {np.linalg.eig(hessian)[0]}')
    print('The hessian is negative definite => local maximum')
    


if DEBUG:
    def function_test(x,y):
        return(x**2 + y**2)
    print (numerical_gradient(function_test, 10**(-8))(3, -2))
