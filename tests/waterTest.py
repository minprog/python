from checkpy import *
from _basics_no_listcomp import *
from _static_analysis import *

@t.passed(doctest_ok)
def has_functions():
    """functie `hoeveelheid_water` is aanwezig"""
    assert defines_function("hoeveelheid_water")

@t.passed(has_functions)
def test_hoeveelheid_water(test):
    """functie `hoeveelheid_water` werkt correct"""
    assert getFunction("hoeveelheid_water")(1) == 12
    assert getFunction("hoeveelheid_water")(10) == 120
    assert getFunction("hoeveelheid_water")(20) == 240
    assert getFunction("hoeveelheid_water")(0) == 0

@t.passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert outputOf(stdinArgs=[21], overwriteAttributes=[("__name__", "__main__")]) == "240\n"
