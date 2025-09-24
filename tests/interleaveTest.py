from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `interleave` is aanwezig"""
    assert defines_function("interleave")
    assert not_in_code(ast.Set)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

@passed(has_functions)
def test_function_1(test):
    """functie `interleave` werkt correct voor twee lijsten met gelijke lengte"""
    interleave = get_function("interleave")
    assert interleave([0, 1], [2, 3], False) == [0, 2, 1, 3]
    assert interleave([0, 1], [0, 1], False) == [0, 0, 1, 1]
    assert interleave([0], [1], False)       == [0, 1]
    assert interleave([], [], False)         == []
    # keep=True maar lengte is toch gelijk dus moet niet uitmaken
    assert interleave([0, 1], [2, 3], True)  == [0, 2, 1, 3]

@passed(has_functions)
def test_function_2(test):
    """functie `interleave` werkt correct voor twee lijsten met verschillende lengte"""
    interleave = get_function("interleave")
    assert interleave([0], [1, 2], False)    == [0, 1]
    assert interleave([0], [1, 2], True)     == [0, 1, 2]
    assert interleave([0, 1], [2], False)    == [0, 2]
    assert interleave([0, 1], [2], True)     == [0, 2, 1]
    assert interleave([], [1, 2], False)     == []
    assert interleave([], [1, 2], True)      == [1, 2]
    assert interleave([1, 3, 5], [2, 4, 6, 7], True) == [1, 2, 3, 4, 5, 6, 7]

@passed(has_functions)
def test_no_changes_to_list(test):
    """functie `interleave` doet geen aanpassing aan originele lijst"""
    arg1 = HistoryList([1, 1, 1, 1])
    arg2 = HistoryList([2, 2, 2])
    result = getFunction("interleave")(arg1, arg2, True)
    if len(arg1.history) > 1 or len(arg2.history) > 1:
        raise AssertionError("originele lijst is toch aangepast")
