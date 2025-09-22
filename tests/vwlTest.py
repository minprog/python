from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `remove_vowels` is aanwezig"""
    assert defines_function("remove_vowels")
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

@passed(has_functions)
def test_function(test):
    """functie `remove_vowels` werkt correct"""
    remove_vowels = getFunction("remove_vowels")
    assert_return("jst sttng p my twttr",
        remove_vowels, "just setting up my twitter")
    assert_return("twp",
        remove_vowels, "tweep")
    assert_return("scl md",
        remove_vowels, "social media")

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert_output(run("social media"), "scl md\n")
