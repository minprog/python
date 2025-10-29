from checkpy import *
from _basics import *
from _pyprog_tools import *

import ast

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("list_duplicates")
    assert function_defined_in_module("mating_pairs")
    assert function_defined_in_module("count_values")
    assert function_defined_in_module("minst_voorkomende")
    assert function_defined_in_module("tel_dubbele")
    assert function_defined_in_module("is_normal")
    assert function_defined_in_module("dict_intersect")
    assert function_defined_in_module("get_valuable_letters")
    assert function_defined_in_module("emmeren")

@t.passed(has_functions)
def test_find_dups(test):
    """functie `find_dups` werkt correct"""
    assert getFunction("list_duplicates")([3, 5, 6, 2, 2, 3, 3, 1]) == {2, 3}
    assert getFunction("list_duplicates")([1]) == set()
    assert getFunction("list_duplicates")([]) == set()

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

@t.passed(has_functions)
def test_minst_voorkomende(test):
    """functie `minst_voorkomende` werkt correct"""
    assert getFunction("minst_voorkomende")({'biefstukzwam': 5, 'gewone oesterzwam': 12, 'gewoon eekhoorntjesbrood': 2, 'porseleinzwam': 22, 'judasoor': 4}) == 'gewoon eekhoorntjesbrood'
    assert getFunction("minst_voorkomende")({'biefstukzwam': 5}) == 'biefstukzwam'

@t.passed(has_functions)
def test_tel_dubbele(test):
    """functie `tel_dubbele` werkt correct"""
    assert getFunction("tel_dubbele")({'raar': 'bn', 'tafel': 'zn', 'woord': 'zn', 'ruimte': 'zn', 'erg': 'bw', 'aardig': 'bn'}) == 2
    assert getFunction("tel_dubbele")({}) == 0

@t.passed(has_functions)
def test_is_balanced(test):
    """functie `is_normal` werkt correct"""
    assert getFunction("is_normal")({'R': 0.2, 'G': 0.4, 'B': 0.4}) == True
    assert getFunction("is_normal")({'R': 0.0}) == False

@t.passed(has_functions)
def test_dict_intersect(test):
    """functie `dict_intersect` werkt correct"""
    assert getFunction("dict_intersect")({'on': 'zin', 'waar': 'heid'}, {}) == {}
    assert getFunction("dict_intersect")({'on': 'zin', 'waar': 'heid'}, {'on': 'zin'}) == {'on': 'zin'}
    assert getFunction("dict_intersect")({'on': 'zin', 'waar': 'heid'}, {'roos': 'kleurig'}) == {}

@t.passed(has_functions)
def test_get_valuable_letters(test):
    """functie `get_valuable_letters` werkt correct"""
    assert getFunction("get_valuable_letters")(1) == 26
    assert getFunction("get_valuable_letters")(10) == 1
    assert getFunction("get_valuable_letters")(8) == 3

@t.passed(has_functions)
def test_get_emmeren(test):
    """functie `emmeren` werkt correct"""
    assert getFunction("emmeren")([[1,2,3], [3,4], [4,5]]) == {3: [[1, 2, 3]], 2: [[3, 4], [4, 5]]}
    assert getFunction("emmeren")([[]]) == {}
    assert getFunction("emmeren")([[1,2,3]]) == {3: [[1,2,3]]}
