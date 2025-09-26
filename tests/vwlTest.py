from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `remove_vowels` is aanwezig"""
    assert function_defined_in_module("remove_vowels")
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()
    assert no_string_methods_used()

@passed(has_functions)
def test_function(test):
    """functie `remove_vowels` werkt correct"""
    remove_vowels = get_function("remove_vowels")
    assert remove_vowels("just setting up my twitter") == "jst sttng p my twttr"
    assert remove_vowels("tweep") == "twp"
    assert remove_vowels("social media") == "scl md"

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert run("social media") == "scl md\n"
