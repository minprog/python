from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """functie `is_acidic` is aanwezig"""
    assert defines_function("is_acidic")

@passed(has_functions)
def test_function(test):
    """functie `is_acidic` werkt correct"""
    is_acidic = get_function("is_acidic")
    assert is_acidic(10.0) == False
    assert is_acidic(5.0) == True
    assert is_acidic(4.9) == True
    assert is_acidic(7.1) == False

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert_output(run(3), "Het is een zuur\n")
    assert_output(run(8), "Het is een base\n")
