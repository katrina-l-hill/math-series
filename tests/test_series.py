from math_series.series import fibonacci, lucas, sum_series

def test_fib_10():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected

def test_fib_20():
    actual = fibonacci(20)
    expected = 6765
    assert actual == expected

def test_lucas_10():
    actual = lucas(10)
    expected = 123
    assert actual == expected

def test_lucas_20():
    actual = lucas(20)
    expected = 15127
    assert actual == expected

def test_sum_series_fib_10():
    actual = sum_series(10)
    expected = 55
    assert actual == expected

def test_sum_series_lucas_10():
    actual = sum_series(10, 2, 1)
    expected = 123
    assert actual == expected

def test_func_equivalence_fib():
    assert fibonacci(10) == sum_series(10)

def test_func_equivalence_lucas():
    assert lucas(10) == sum_series(10,2,1)
