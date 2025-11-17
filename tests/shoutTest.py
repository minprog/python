from ast import Assert
from checkpy import *
from _pyprog_tools import *

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

class SafeString(str):
    def lower(self):
        raise AssertionError("je mag geen lower gebruiken voor de hele string!")
    def upper(self):
        raise AssertionError("je mag geen upper gebruiken voor de hele string!")

@passed(has_functions)
def test_function():
    """functie `shout` werkt correct"""
    shout = get_function("shout")
    assert shout("Who the hell put the muffins the freezer?") == \
                 "WHO THE HELL PUT THE MUFFINS THE FREEZER?"
    assert shout("") == ""
    assert shout("let it all out...") == "LET IT ALL OUT..."
    try:
        assert shout(SafeString("hoi")) == "HOI"
    except BaseException as e:
        raise AssertionError("je mag geen upper/lower gebruiken voor de hele string, wel voor 1 teken")

@passed(has_functions)
def test_program():
    """het programma werkt correct met invoer en uitvoer"""
    assert run("Who the hell put the muffins the freezer?") == \
               "WHO THE HELL PUT THE MUFFINS THE FREEZER?\n"
