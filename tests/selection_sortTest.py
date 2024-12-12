from checkpy import *
from _basics import *
from _static_analysis import *

import ast

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert defines_function("selection_sort")

@t.passed(has_functions)
def test_selection_sort(test):
    """functie `selection_sort` werkt correct"""
    assert getFunction("selection_sort")([1,2,3]) == [1,2,3]
    assert getFunction("selection_sort")([3,2,1]) == [1,2,3]
    assert getFunction("selection_sort")([1,3,2,4]) == [1,2,3,4]
    assert getFunction("selection_sort")([]) == []:
    
