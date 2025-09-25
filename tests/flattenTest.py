from checkpy import *
from _static_analysis import *
from _list_tracking import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `flatten` is aanwezig"""
    assert function_defined_in_module("flatten")
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()
    assert no_string_methods_used()

@passed(has_functions)
def test_function(test):
    """functie `flatten` werkt correct"""
    flatten = get_function("flatten")
    assert flatten([[0]]) == [0]
    assert flatten([[1]]) == [1]
    assert flatten([[1,2]]) == [1,2]
    assert flatten([[1],[2]]) == [1,2]
    assert flatten([[2],[1]]) == [2,1]
    assert flatten([[2],[1,0]]) == [2,1,0]
    assert flatten([[]]) == []

@passed(has_functions)
def test_no_changes_to_list(test):
    """functie `flatten` doet geen aanpassing aan originele lijst"""
    arg = HistoryList([[1]])
    result = getFunction("flatten")(arg)
    if len(arg.history) > 1:
        raise AssertionError("originele lijst is toch aangepast")
