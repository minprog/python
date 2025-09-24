from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("count_occurrences")
    assert function_defined_in_module("has_O")
    assert function_defined_in_module("find")
    assert function_defined_in_module("has_up_and_down")

@passed(has_functions)
def test_count_occ(test):
    """functie `count_occurrences` werkt correct"""
    coin = get_function("count_occurrences")
    assert count_occurrences('lllll', 'a') == 0
    assert count_occurrences('no', 'n') == 1
    assert count_occurrences('no', 'o') == 1
    assert count_occurrences('nanana', 'n') == 3
    assert count_occurrences('', 'n') == 0

@passed(has_functions)
def test_has_o(test):
    """functie `has_O` werkt correct"""
    has_O = get_function("has_O")
    assert has_O('') == False
    assert has_O('other') == False
    assert has_O('nm') == False
    assert has_O('l') == False
    assert has_O('O') == True
    assert has_O('Other') == True
    assert has_O('lO') == True
    assert has_O('kOm') == True
    assert has_O('kOO') == True

@passed(has_functions)
def test_find(test):
    """functie `find` werkt correct"""
    find = get_function("find")
    assert find('') == False
    assert find('other') == False
    assert find('nm') == False
    assert find('l') == False
    assert find('O') == True
    assert find('Other') == True
    assert find('lO') == True
    assert find('kOm') == True
    assert find('kOO') == True

@passed(has_functions)
def test_has_up_and_down(test):
    """functie `has_up_and_down` werkt correct"""
    find = get_function("has_up_and_down")
    assert has_up_and_down('') == False
    assert has_up_and_down('other') == False
    assert has_up_and_down('nm') == False
    assert has_up_and_down('l') == False
    assert has_up_and_down('O') == False
    assert has_up_and_down('Other') == True
    assert has_up_and_down('lO') == True
    assert has_up_and_down('kOm') == True
    assert has_up_and_down('kOO') == True
    assert has_up_and_down('OO') == True
    assert has_up_and_down('OmO') == True
    assert has_up_and_down('OOm') == True
