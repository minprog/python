from checkpy import *
from _basics_no_listcomp import *
from _static_analysis import *

@t.passed(doctest_ok)
def has_functions():
    """functie `is_acidic` is aanwezig"""
    assert defines_function("is_acidic")

@t.passed(has_functions)
def test_weeks_elapsed(test):
    """functie `is_acidic` werkt correct"""
    assert getFunction("is_acidic")(10.0) == False
    assert getFunction("is_acidic")(5.0) == True
    assert getFunction("is_acidic")(4.9) == True
    assert getFunction("is_acidic")(7.1) == False

@t.passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert outputOf(stdinArgs=[3], overwriteAttributes=[("__name__", "__main__")]) == "Het is een zuur\n"
