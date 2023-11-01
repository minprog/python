from checkpy import *
from _basics_no_listcomp import *
from _static_analysis import *

import ast

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert defines_function("same_first_last")
    assert defines_function("is_longer")
    assert not_in_code(ast.While)
    assert not_in_code(ast.For)

@t.passed(has_functions)
def test_same_first_last(test):
    """functie `same_first_last` werkt correct"""
    assert getFunction("same_first_last")([3, 4, 2, 8, 3]) == True
    assert getFunction("same_first_last")(['apple', 'banana', 'pear']) == False
    assert getFunction("same_first_last")([4.0, 4.5]) == False

@t.passed(has_functions)
def test_is_longer(test):
    """functie `is_longer` werkt correct"""
    assert getFunction("is_longer")([1, 2, 3], [4, 5]) == True
    assert getFunction("is_longer")(['abcdef'], ['ab', 'cd', 'ef']) == False
    assert getFunction("is_longer")(['a', 'b', 'c'], [1, 2, 3]) == False
