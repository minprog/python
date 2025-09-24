from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `yell` is aanwezig"""
    assert function_defined_in_module("yell")
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()
    assert no_string_methods_used()

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
    assert run("OK!") == "OK!!\n"
    assert run("??!!") == "????!!!!\n"
