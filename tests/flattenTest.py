from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `flatten` is aanwezig"""
    assert defines_function("flatten")
    assert not_in_code(ast.Set)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

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
