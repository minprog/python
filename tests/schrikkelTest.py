from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """functie `is_schrikkel` is aanwezig"""
    assert defines_function("is_schrikkel")

@passed(has_functions)
def test_weeks_elapsed(test):
    """functie `is_schrikkel` werkt correct"""
    is_schrikkel = getFunction("is_schrikkel")
    assert_no_input_output(is_schrikkel)
    assert_return(False, is_schrikkel, 2001)
    assert_return(True, is_schrikkel, 2000)
    assert_return(False, is_schrikkel, 1463)
    assert_return(True, is_schrikkel, 2020)
    assert_return(False, is_schrikkel, 2100)
    assert_return(False, is_schrikkel, 1900)

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert_output(run(2001), "2001 is geen schrikkeljaar\n")
    assert_output(run(2000), "2000 is een schrikkeljaar\n")
