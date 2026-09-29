from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("stretch")
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)

@passed(has_functions)
def test_function_stretch(test):
    """functie `stretch` werkt correct"""
    stretch = get_function("stretch")
    assert stretch("abc") == "abbccc"
    assert stretch("Hoi!") == "Hooiii!!!!"
    assert stretch("!") == "!"
    assert stretch("") == ""
