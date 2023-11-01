from checkpy import *
from _basics_no_listcomp import *
from _static_analysis import *

@t.passed(doctest_ok)
def has_functions():
    """functie `weeks_elapsed` is aanwezig"""
    assert defines_function("weeks_elapsed")

@t.passed(has_functions)
def test_weeks_elapsed(test):
    """functie `weeks_elapsed` werkt correct"""
    assert getFunction("weeks_elapsed")(3,20) == 2
    assert getFunction("weeks_elapsed")(20,3) == 2
    assert getFunction("weeks_elapsed")(1,1) == 0

@t.passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert outputOf(stdinArgs=[3,20], overwriteAttributes=[("__name__", "__main__")]) == "Er zijn 2 volle weken verstreken.\n"
