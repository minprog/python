from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `shout` is aanwezig"""
    assert function_defined_in_module("shout")
    assert construct_in_ast(ast.For)
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()
    assert no_string_methods_used()

@passed(has_functions)
def test_function(test):
    """functie `shout` werkt correct"""
    shout = get_function("shout")
    assert shout("Who the hell put the muffins the freezer?") == "WHO THE HELL PUT THE MUFFINS THE FREEZER?"
    assert shout("") == ""
    assert shout("let it all out...") == "LET IT ALL OUT..."

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert_output(
        run("Who the hell put the muffins the freezer?"),
        "WHO THE HELL PUT THE MUFFINS THE FREEZER?\n")
