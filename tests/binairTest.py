from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """functie `convert` is aanwezig"""
    assert defines_function("convert")

@passed(has_functions)
def test_convert(test):
    """functie `convert` werkt correct"""
    convert = getFunction("convert")
    assert_no_input_output(convert)
    assert_return(4, convert, 0, 1, 0, 0)
    assert_return(15, convert, 1, 1, 1, 1)
    assert_return(5, convert, 0, 1, 0, 1)
    assert_return(0, convert, 0, 0, 0, 0)

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer (0111)"""
    assert_output(run(0, 1, 1, 1).number(), "7")
