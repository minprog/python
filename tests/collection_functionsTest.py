from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
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

@passed(has_functions)
def test_find_dups():
    """functie `find_dups` werkt correct"""
    assert get_function("list_duplicates")([3, 5, 6, 2, 2, 3, 3, 1]) == {2, 3}
    assert get_function("list_duplicates")([1]) == set()
    assert get_function("list_duplicates")([]) == set()

@passed(has_functions)
def test_mating_pairs():
    """functie `mating_pairs` werkt correct"""
    result = getFunction("mating_pairs")({1, 2, 3}, {4, 5, 6})
    assert sorted(list(map(lambda x: x[0], result))) == [1, 2, 3]
    assert sorted(list(map(lambda x: x[1], result))) == [4, 5, 6]

@passed(has_functions)
def test_count_values():
    """functie `count_values` werkt correct"""
    assert get_function("count_values")({'red': 1, 'green': 1, 'blue': 2}) == 2

@passed(has_functions)
def test_minst_voorkomende():
    """functie `minst_voorkomende` werkt correct"""
    assert get_function("minst_voorkomende")({'biefstukzwam': 5, 'gewone oesterzwam': 12, 'gewoon eekhoorntjesbrood': 2, 'porseleinzwam': 22, 'judasoor': 4}) == 'gewoon eekhoorntjesbrood'
    assert get_function("minst_voorkomende")({'biefstukzwam': 5}) == 'biefstukzwam'

@passed(has_functions)
def test_tel_dubbele():
    """functie `tel_dubbele` werkt correct"""
    assert get_function("tel_dubbele")({'raar': 'bn', 'tafel': 'zn', 'woord': 'zn', 'ruimte': 'zn', 'erg': 'bw', 'aardig': 'bn'}) == 2
    assert get_function("tel_dubbele")({}) == 0

@passed(has_functions)
def test_is_balanced():
    """functie `is_normal` werkt correct"""
    assert get_function("is_normal")({'R': 0.2, 'G': 0.4, 'B': 0.4}) == True
    assert get_function("is_normal")({'R': 0.0}) == False

@passed(has_functions)
def test_dict_intersect():
    """functie `dict_intersect` werkt correct"""
    assert get_function("dict_intersect")({'on': 'zin', 'waar': 'heid'}, {}) == {}
    assert get_function("dict_intersect")({'on': 'zin', 'waar': 'heid'}, {'on': 'zin'}) == {'on': 'zin'}
    assert get_function("dict_intersect")({'on': 'zin', 'waar': 'heid'}, {'roos': 'kleurig'}) == {}

@passed(has_functions)
def test_get_valuable_letters():
    """functie `get_valuable_letters` werkt correct"""
    assert get_function("get_valuable_letters")(1) == 26
    assert get_function("get_valuable_letters")(10) == 1
    assert get_function("get_valuable_letters")(8) == 3

@passed(has_functions)
def test_get_emmeren():
    """functie `emmeren` werkt correct"""
    assert get_function("emmeren")([[1,2,3], [3,4], [4,5]]) == {3: [[1, 2, 3]], 2: [[3, 4], [4, 5]]}
    assert get_function("emmeren")([[]]) == {}
    assert get_function("emmeren")([[1,2,3]]) == {3: [[1,2,3]]}
