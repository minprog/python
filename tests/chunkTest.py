from checkpy import *
from _pyprog_tools import *
from _list_tracking import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `chunk` is aanwezig"""
    assert function_defined_in_module("chunk")
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()
    assert no_string_methods_used()

@passed(has_functions)
def test_function(test):
    """functie `chunk` werkt correct"""
    chunk = get_function("chunk")
    assert chunk([0, 1, 2, 3], 1) == [[0], [1], [2], [3]]
    assert chunk([0,1,2,3], 1)    == [[0], [1], [2], [3]]
    assert chunk([0,1,2,3], 2)    == [[0, 1], [2, 3]]
    assert chunk([0,1,2,3], 4)    == [[0, 1, 2, 3]]
    assert chunk([0,1,2,3], 5)    == [[0, 1, 2, 3]]
    assert chunk([], 4)           == []

@passed(has_functions)
def test_no_changes_to_list(test):
    """functie `chunk` doet geen aanpassing aan originele lijst"""
    arg = HistoryList([1, 1, 1, 1])
    result = getFunction("chunk")(arg, 1)
    if len(arg.history) > 1:
        raise AssertionError("originele lijst is toch aangepast")
