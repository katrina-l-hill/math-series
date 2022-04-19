from test_series import test_fibonacci

def fibonacci():
    pass

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

print(lucas(3))

def sum_series(n, first_param=0, second_param=1):
    print(n, first_param, second_param)
