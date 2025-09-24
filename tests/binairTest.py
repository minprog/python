from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """functie `convert` is aanwezig"""
    assert function_defined_in_module("convert")

@passed(has_functions)
def test_convert(test):
    """functie `convert` werkt correct"""
    convert = get_function("convert")
    assert no_input_output_in_function(convert)
    assert convert(0, 1, 0, 0) == 4
    assert convert(1, 1, 1, 1) == 15
    assert convert(0, 1, 0, 1) == 5
    assert convert(0, 0, 0, 0) == 0

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer (0111)"""
    assert_output(run(0, 1, 1, 1).number(), "7")
