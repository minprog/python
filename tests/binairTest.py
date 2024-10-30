from checkpy import *
from _static_analysis import *

from _basics_no_listcomp import *
from _check_doctests import require_doctests_for_all_functions

@t.passed(doctest_ok)
def has_functions():
    """functie `convert` is aanwezig"""
    assert defines_function("convert")

@t.passed(has_functions)
def test_convert(test):
    """functie `convert` werkt correct"""
    assert getFunction("convert")(0, 1, 0, 0) == 4
    assert getFunction("convert")(1, 1, 1, 1) == 15
    assert getFunction("convert")(0, 1, 0, 1) == 5
    assert getFunction("convert")(0, 0, 0, 0) == 0

@t.passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer (0111)"""
    assert outputOf(stdinArgs=[0, 1, 1, 1], overwriteAttributes=[("__name__", "__main__")]) == "7\n"
