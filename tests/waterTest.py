from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `hoeveelheid_water` is aanwezig"""
    assert defines_function("hoeveelheid_water")

@passed(has_functions)
def test_hoeveelheid_water(test):
    """functie `hoeveelheid_water` werkt correct"""
    hoeveelheid_water = getFunction("hoeveelheid_water")
    assert_no_input_output(hoeveelheid_water)
    assert_return(12, hoeveelheid_water, 1)
    assert_return(120, hoeveelheid_water, 10)
    assert_return(240, hoeveelheid_water, 20)
    assert_return(0, hoeveelheid_water, 0)

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer (21 minuten)"""
    assert_output(run(21).number(), "252")
