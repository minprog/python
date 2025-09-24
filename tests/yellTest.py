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
    yell = get_function("yell")
    assert yell("Can't shake it off of me!") == "Can't shake it off of me!!"
    assert yell("Who the hell put the muffins the freezer?") == "Who the hell put the muffins the freezer??"
    assert yell("Cringe? CRINGE!") == "Cringe?? CRINGE!!"
    assert yell("OK!") == "OK!!"
    assert yell("?!") == "??!!"

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert_output(run("OK!"), "OK!!\n")
    assert_output(run("??!!"), "????!!!!\n")
