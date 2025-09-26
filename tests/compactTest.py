import typing

from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `compact` is aanwezig"""
    assert function_defined_in_module("compact")
    if string_in_module("import Any", "[Any]"):
        raise AssertionError("gebruik geen Any als type in deze opdracht")
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()
    assert no_string_methods_used()
    assert construct_not_in_ast(typing.Any)

@passed(has_functions)
def test_function(test):
    """functie `compact` werkt correct"""
    compact = get_function("compact")
    l = [0]; compact(l); assert l == []
    l = [False]; compact(l); assert l == []
    l = ['']; compact(l); assert l == []
    l = [[]]; compact(l); assert l == []
    l = [2, 0, False, '']; compact(l); assert l == [2]
    l = [0, False, '']; compact(l); assert l == []
    l = [1, 2, 3, 4]; compact(l); assert l == [1, 2, 3, 4]
    # assert compact([1]]) == [1]
    # assert compact([1,2]]) == [1,2]
    # assert compact([1],[2]]) == [1,2]
    # assert compact([2],[1]]) == [2,1]
    # assert compact([2],[1,0]]) == [2,1,0]
    # assert compact([]]) == []
