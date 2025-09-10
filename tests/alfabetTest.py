from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, check_doctests
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, check_doctests)
def has_functions():
    """functie `compare` is aanwezig"""
    assert defines_function("compare")

@passed(has_functions)
def test_comes_before(test):
    """functie `compare` werkt correct"""
    assert getFunction("compare")('Taylor', 'Lana') == 1
    assert getFunction("compare")('shark', 'sWoRd') == -1
    assert getFunction("compare")('Daantje', 'Daan') == 1
    assert getFunction("compare")('amanda', 'Amanda') == 0, "de functie moet 0 geven als de woorden gelijk zijn"

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert outputOf(stdinArgs=['Taylor', 'Lana'], overwriteAttributes=[("__name__", "__main__")]) == "Lana first\n"
    assert outputOf(stdinArgs=['Lana', 'Taylor'], overwriteAttributes=[("__name__", "__main__")]) == "Lana first\n"
    assert outputOf(stdinArgs=['amanda', 'Amanda'], overwriteAttributes=[("__name__", "__main__")]) == "No need to decide!\n"
