from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `compare` is aanwezig"""
    assert defines_function("compare")

@passed(has_functions)
def test_comes_before(test):
    """functie `compare` werkt correct"""
    compare = getFunction("compare")
    assert_return(1, compare, 'Taylor', 'Lana')
    assert_return(-1, compare, 'shark', 'sWoRd')
    assert_return(1, compare, 'Daantje', 'Daan')
    if compare('amanda', 'Amanda') != 0:
        raise AssertionError("de functie moet 0 geven als de woorden gelijk zijn")

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert_output(run('Taylor', 'Lana'), "Lana first\n")
    assert_output(run('Lana', 'Taylor'), "Lana first\n")
    assert_output(run('amanda', 'Amanda'), "No need to decide!\n")
