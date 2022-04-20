"""
This function has one parameter, n. It returns the nth value in the fibonacci series. This function is implemented using recursion.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

"""
This function has one parameter, n. It returns the nth value in the lucas series. This function is implemented using recursion.
"""

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

"""
This function has one required parameter and two optional parameters. This function performs recursive addition based upon the inputs given.
"""

def sum_series(n, first_param=0, second_param=1):
    if n == 0:
        return first_param
    elif n == 1:
        return second_param
    else:
        return sum_series(n-2, first_param, second_param) + sum_series(n-1, first_param, second_param)
 

print(sum_series(10))

print(sum_series(10, 2, 1))