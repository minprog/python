from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `weeks_elapsed` is aanwezig"""
    assert defines_function("weeks_elapsed")

@passed(has_functions)
def test_weeks_elapsed(test):
    """functie `weeks_elapsed` werkt correct"""
    weeks_elapsed = getFunction('weeks_elapsed')
    assert_no_input_output(weeks_elapsed)
    assert_return(2, weeks_elapsed, 3, 20)
    assert_return(2, weeks_elapsed, 20, 3)
    assert_return(0, weeks_elapsed, 1, 1)

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert_output(run(3, 20), "Er zijn 2 volle weken verstreken.\n")
