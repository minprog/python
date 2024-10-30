from checkpy import *
from _basics_no_listcomp import *
from _static_analysis import *

@t.passed(doctest_ok)
def has_functions():
    """functie `comes_before` is aanwezig"""
    assert defines_function("comes_before")

@t.passed(has_functions)
def test_comes_before(test):
    """functie `comes_before` werkt correct"""
    assert getFunction("comes_before")('Taylor', 'Lana') == False
    assert getFunction("comes_before")('shark', 'sWoRd') == True
    assert getFunction("comes_before")('Daantje', 'Daan') == False
    assert getFunction("comes_before")('amanda', 'Amanda') == True, "de functie mag True geven als de woorden gelijk zijn"

@t.passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert outputOf(stdinArgs=['Taylor', 'Lana'], overwriteAttributes=[("__name__", "__main__")]) == "Lana first\n"
    assert outputOf(stdinArgs=['Lana', 'Taylor'], overwriteAttributes=[("__name__", "__main__")]) == "Lana first\n"
    assert outputOf(stdinArgs=['amanda', 'Amanda'], overwriteAttributes=[("__name__", "__main__")]) == "No need to decide!\n"
