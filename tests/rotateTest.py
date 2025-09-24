from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `rotate` is aanwezig"""
    assert function_defined_in_module("rotate")
    if string_in_module("import Any", "[Any]"):
        raise AssertionError("gebruik geen Any als type in deze opdracht")
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()
    assert no_string_methods_used()

@passed(has_functions)
def test_function(test):
    """functie `rotate` werkt correct"""
    rotate = get_function("rotate")

    lst = [2,3,1]; rotate(lst);
    if lst != [3,1,2]:
        raise AssertionError(f"l = [2,3,1]; rotate(l): verwachtte [3, 1, 2] maar kreeg {lst}")

    lst = [2,1,3]; rotate(lst);
    if lst != [1,3,2]:
        raise AssertionError(f"l = [2,1,3]; rotate(l): verwachtte [1, 3, 2] maar kreeg {lst}")

    lst = [2,1];   rotate(lst)
    if lst != [1,2]:
        raise AssertionError(f"l = [2,1]; rotate(l): verwachtte [1, 2] maar kreeg {lst}")

    lst = [1,2];   rotate(lst)
    if lst != [2,1]:
        raise AssertionError(f"l = [1,2]; rotate(l): verwachtte [2, 1] maar kreeg {lst}")

    lst = [1];     rotate(lst)
    if lst != [1]:
        raise AssertionError(f"l=[1]; rotate(l): verwachtte [1] maar kreeg {lst}")

    lst = [];      rotate(lst)
    if lst != []:
        raise AssertionError(f"l=[]; rotate(l): verwachtte [] maar kreeg {lst}")
