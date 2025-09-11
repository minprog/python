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
    assert getFunction("convert")(0, 1, 0, 0) == 4
    assert getFunction("convert")(1, 1, 1, 1) == 15
    assert getFunction("convert")(0, 1, 0, 1) == 5
    assert getFunction("convert")(0, 0, 0, 0) == 0

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer (0111)"""
    assert outputOf(stdinArgs=[0, 1, 1, 1], overwriteAttributes=[("__name__", "__main__")]) == "7\n"
