from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `shout` is aanwezig"""
    assert defines_function("shout")
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

@passed(has_functions)
def test_function(test):
    """functie `shout` werkt correct"""
    shout = getFunction("shout")
    assert_return("Who the hell put the muffins the freezer?",
        shout, "WHO THE HELL PUT THE MUFFINS THE FREEZER?")
    assert_return("",
        shout, "")
    assert_return("let it all out...",
        shout, "LET IT ALL OUT...")

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert_output(
        run("Who the hell put the muffins the freezer?"),
        "WHO THE HELL PUT THE MUFFINS THE FREEZER?\n")
