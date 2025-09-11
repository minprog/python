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
    assert getFunction("hoeveelheid_water")(1) == 12
    assert getFunction("hoeveelheid_water")(10) == 120
    assert getFunction("hoeveelheid_water")(20) == 240
    assert getFunction("hoeveelheid_water")(0) == 0

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer (21 minuten)"""
    assert outputOf(stdinArgs=[21], overwriteAttributes=[("__name__", "__main__")]) == "252\n"
