from checkpy import *
from _basics import *
from _static_analysis import *

import ast

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert defines_function("special_sort")

@t.passed(has_functions)
def test_special_sort(test):
    """functie `special_sort` werkt correct"""
    assert getFunction("special_sort")([1,2,3]) == [1,2,3]
    assert getFunction("special_sort")([3,2,1]) == [1,2,3]
    assert getFunction("special_sort")([]) == []
    assert getFunction("special_sort")([[1],[3],[2]]) == [[1],[2],[3]]
