from checkpy import *
from _basics import *
from _static_analysis import *

import ast

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert defines_function("find_dups")
    assert defines_function("mating_pairs")
    assert defines_function("count_values")
    assert in_code(ast.For)

@t.passed(has_functions)
def test_find_dups(test):
    """functie `find_dups` werkt correct"""
    assert getFunction("find_dups")([3, 5, 6, 2, 2, 3, 3, 1]) == {2, 3}
    assert getFunction("find_dups")([1]) == set()
    assert getFunction("find_dups")([]) == set()

@t.passed(has_functions)
def test_mating_pairs(test):
    """functie `mating_pairs` werkt correct"""
    result = getFunction("mating_pairs")({1, 2, 3}, {4, 5, 6})
    assert sorted(list(map(lambda x: x[0], result))) == [1, 2, 3]
    assert sorted(list(map(lambda x: x[1], result))) == [4, 5, 6]

@t.passed(has_functions)
def test_count_values(test):
    """functie `count_values` werkt correct"""
    assert getFunction("count_values")({'red': 1, 'green': 1, 'blue': 2}) == 2
