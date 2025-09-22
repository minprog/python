from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `yell` is aanwezig"""
    assert defines_function("yell")
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

@passed(has_functions)
def test_function(test):
    """functie `yell` werkt correct"""
    yell = getFunction("yell")
    assert_return("Can't shake it off of me!!",
        yell, "Can't shake it off of me!")
    assert_return("Who the hell put the muffins the freezer??",
        yell, "Who the hell put the muffins the freezer?")
    assert_return("Cringe?? CRINGE!!",
        yell, "Cringe? CRINGE!")
    assert_return("OK!!",
        yell, "OK!")
    assert_return("??!!",
        yell, "?!")

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert_output(run("OK!"), "OK!!\n")
    assert_output(run("??!!"), "????!!!!\n")
