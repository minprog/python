from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert defines_function("count_occurrences")
    assert defines_function("has_O")
    assert defines_function("find")
    assert defines_function("has_up_and_down")

@passed(has_functions)
def test_count_occ(test):
    """functie `count_occurrences` werkt correct"""
    coin = getFunction("count_occurrences", test.fileName)
    assert_return(0, count_occurrences, 'lllll', 'a')
    assert_return(1, count_occurrences, 'no', 'n')
    assert_return(1, count_occurrences, 'no', 'o')
    assert_return(3, count_occurrences, 'nanana', 'n')
    assert_return(0, count_occurrences, '', 'n')

@passed(has_functions)
def test_has_o(test):
    """functie `has_O` werkt correct"""
    has_O = getFunction("has_O", test.fileName)
    assert_return(False, has_O, '')
    assert_return(False, has_O, 'other')
    assert_return(False, has_O, 'nm')
    assert_return(False, has_O, 'l')
    assert_return(True, has_O, 'O')
    assert_return(True, has_O, 'Other')
    assert_return(True, has_O, 'lO')
    assert_return(True, has_O, 'kOm')
    assert_return(True, has_O, 'kOO')

@passed(has_functions)
def test_find(test):
    """functie `find` werkt correct"""
    find = getFunction("find", test.fileName)
    assert_return(False, find, '')
    assert_return(False, find, 'other')
    assert_return(False, find, 'nm')
    assert_return(False, find, 'l')
    assert_return(True, find, 'O')
    assert_return(True, find, 'Other')
    assert_return(True, find, 'lO')
    assert_return(True, find, 'kOm')
    assert_return(True, find, 'kOO')

@passed(has_functions)
def test_has_up_and_down(test):
    """functie `has_up_and_down` werkt correct"""
    find = getFunction("has_up_and_down", test.fileName)
    assert_return(False, has_up_and_down, '')
    assert_return(False, has_up_and_down, 'other')
    assert_return(False, has_up_and_down, 'nm')
    assert_return(False, has_up_and_down, 'l')
    assert_return(False, has_up_and_down, 'O')
    assert_return(True, has_up_and_down, 'Other')
    assert_return(True, has_up_and_down, 'lO')
    assert_return(True, has_up_and_down, 'kOm')
    assert_return(True, has_up_and_down, 'kOO')
    assert_return(True, has_up_and_down, 'OO')
    assert_return(True, has_up_and_down, 'OmO')
    assert_return(True, has_up_and_down, 'OOm')
