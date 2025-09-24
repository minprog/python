from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `uniq` is aanwezig"""
    assert defines_function("uniq")
    assert not_in_code(ast.Set)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

@passed(has_functions)
def test_function(test):
    """functie `uniq` werkt correct"""
    uniq = get_function("uniq")
    assert uniq([0, 1, 2, 3]) == [0, 1, 2, 3]
    assert uniq([1, 1]) == [1]
    assert uniq([1, 1, 1]) == [1]
    assert uniq([1, 1, 2, 2]) == [1, 2]
    assert uniq([]) == []

@passed(has_functions)
def test_no_changes_to_list(test):
    """functie `uniq` doet geen aanpassing aan originele lijst"""
    arg = HistoryList([1, 1, 1, 1])
    result = getFunction("uniq")(arg)
    if len(arg.history) > 1:
        raise AssertionError("originele lijst is toch aangepast")
