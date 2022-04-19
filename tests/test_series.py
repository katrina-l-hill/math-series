

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def test_fib_10():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected

def test_fib_20():
    actual = fibonacci(20)
    expected = 6765
    assert actual == expected
