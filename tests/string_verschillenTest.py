from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("is_different")
    assert function_defined_in_module("count_difference")

    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert construct_not_in_ast(ast.In)

@passed(has_functions)
def test_function_is_different(test):
    """functie `is_different` werkt correct"""
    is_different = get_function("is_different")
    assert is_different("dance", "night") == True
    assert is_different("dance", "dance") == False
    assert is_different("a", "e") == True
    assert is_different("a", "a") == False
    assert is_different("A", "a") == True
    assert is_different("jumpstyle", "hakken") == True
    assert is_different("piano", "pianissimo") == True
    assert is_different("", "mamba") == True
    assert is_different("mamba", "") == True
    assert is_different("", "") == False

@passed(has_functions)
def test_function_count_difference(test):
    """functie `count_difference` werkt correct"""
    count_difference = get_function("count_difference")
    assert count_difference("dance", "night") == 5
    assert count_difference("dance", "dance") == 0
    assert count_difference("a", "e") == 1
    assert count_difference("a", "a") == 0
    assert count_difference("A", "a") == 1
    assert count_difference("jumpstyle", "hakken") == 9
    assert count_difference("piano", "pianissimo") == 6
    assert count_difference("", "mamba") == 5
    assert count_difference("mamba", "") == 5
    assert count_difference("", "") == 0
