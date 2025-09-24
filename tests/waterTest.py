from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `hoeveelheid_water` is aanwezig"""
    assert function_defined_in_module("hoeveelheid_water")

@passed(has_functions)
def test_hoeveelheid_water(test):
    """functie `hoeveelheid_water` werkt correct"""
    hoeveelheid_water = get_function("hoeveelheid_water")
    assert no_input_output_in_function(hoeveelheid_water)
    assert hoeveelheid_water(1) == 12
    assert hoeveelheid_water(10) == 120
    assert hoeveelheid_water(20) == 240
    assert hoeveelheid_water(0) == 0

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer (21 minuten)"""
    assert_output(run(21).number(), "252")
