from checkpy import *
from _pyprog_tools import *

from _python_checks import doctest_all

def close(a, b):
    return abs(a - b) < 1e-9

@passed(doctest_all)
def test_square():
    """functie `square` werkt correct"""
    assert function_defined_in_module("square")
    assert get_function("square")(7) == 49
    assert get_function("square")(-3) == 9
    assert get_function("square")(0) == 0

@passed(doctest_all)
def test_cube():
    """functie `cube` werkt correct"""
    assert function_defined_in_module("cube")
    assert get_function("cube")(3) == 27
    assert get_function("cube")(-2) == -8
    assert get_function("cube")(0) == 0

@passed(doctest_all)
def test_avg3():
    """functie `avg3` werkt correct"""
    assert function_defined_in_module("avg3")
    assert get_function("avg3")(1, 2, 6) == 3.0
    assert get_function("avg3")(0, 0, 0) == 0.0
    assert close(get_function("avg3")(1, 1, 2), 4 / 3)

@passed(doctest_all)
def test_celsius_to_fahrenheit():
    """functie `celsius_to_fahrenheit` werkt correct"""
    assert function_defined_in_module("celsius_to_fahrenheit")
    assert close(get_function("celsius_to_fahrenheit")(37), 98.6)
    assert close(get_function("celsius_to_fahrenheit")(-40), -40.0)

@passed(doctest_all)
def test_fahrenheit_to_celsius():
    """functie `fahrenheit_to_celsius` werkt correct"""
    assert function_defined_in_module("fahrenheit_to_celsius")
    assert close(get_function("fahrenheit_to_celsius")(98.6), 37.0)
    assert close(get_function("fahrenheit_to_celsius")(-40), -40.0)

@passed(doctest_all)
def test_is_divisible():
    """functie `is_divisible` werkt correct"""
    assert function_defined_in_module("is_divisible")
    assert get_function("is_divisible")(12, 4) is True
    assert get_function("is_divisible")(12, 5) is False
    assert get_function("is_divisible")(0, 7) is True
    assert get_function("is_divisible")(3, 6) is False

@passed(doctest_all)
def test_is_leap_year():
    """functie `is_leap_year` werkt correct"""
    assert function_defined_in_module("is_leap_year")
    f = get_function("is_leap_year")
    assert f(2024) is True
    assert f(2023) is False
    assert f(1900) is False
    assert f(2000) is True
    assert f(2100) is False
    assert f(1996) is True

@passed(doctest_all)
def test_pythagoras():
    """functie `pythagoras` werkt correct"""
    assert function_defined_in_module("pythagoras")
    assert close(get_function("pythagoras")(8, 15), 17.0)
    assert close(get_function("pythagoras")(1, 1), 2 ** 0.5)
    assert close(get_function("pythagoras")(0, 5), 5.0)

@passed(doctest_all)
def test_is_valid_triangle():
    """functie `is_valid_triangle` werkt correct"""
    assert function_defined_in_module("is_valid_triangle")
    f = get_function("is_valid_triangle")
    assert f(3, 4, 5) is True
    assert f(5, 4, 3) is True
    assert f(4, 5, 3) is True
    assert f(1, 2, 10) is False
    assert f(10, 1, 2) is False
    assert f(2, 10, 1) is False
    assert f(1, 1, 2) is False

@passed(doctest_all)
def test_solve_quadratic():
    """functie `solve_quadratic` werkt correct"""
    assert function_defined_in_module("solve_quadratic")
    f = get_function("solve_quadratic")
    x1, x2 = f(1, -5, 6)
    assert close(x1, 3.0) and close(x2, 2.0)
    x1, x2 = f(2, 0, -8)
    assert close(x1, 2.0) and close(x2, -2.0)
    x1, x2 = f(1, 2, -3)
    assert close(x1, 1.0) and close(x2, -3.0)
