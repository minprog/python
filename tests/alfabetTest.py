from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `compare` is aanwezig"""
    assert function_defined_in_module("compare")

@passed(has_functions)
def test_comes_before(test):
    """functie `compare` werkt correct"""
    compare = get_function("compare")
    assert compare('Taylor', 'Lana') == 1
    assert compare('shark', 'sWoRd') == -1
    assert compare('Daantje', 'Daan') == 1
    if compare('amanda', 'Amanda') != 0:
        raise AssertionError("de functie moet 0 geven als de woorden gelijk zijn")

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert_output(run('Taylor', 'Lana'), "Lana first\n")
    assert_output(run('Lana', 'Taylor'), "Lana first\n")
    assert_output(run('amanda', 'Amanda'), "No need to decide!\n")
