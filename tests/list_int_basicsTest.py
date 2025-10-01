from checkpy import *
from _pyprog_tools import *
from _list_tracking import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functies `list_count_even`, `list_check_all_even`, `list_get_even` zijn aanwezig"""
    assert function_defined_in_module("list_get_even")
    assert function_defined_in_module("list_check_all_even")
    assert function_defined_in_module("list_count_even")
    assert construct_in_ast(ast.For)
    assert construct_not_in_ast(ast.Slice)
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()
    assert no_string_methods_used()

@passed(has_functions)
def test_function2(test):
    """functie `list_check_all_even` werkt correct"""
    list_check_all_even = get_function("list_check_all_even")
    assert list_check_all_even([2, 4, 6, 1000]) == True
    assert list_check_all_even([1, 2, 3, 4]) == False
    assert list_check_all_even([4, 3, 2, 1]) == False
    assert list_check_all_even([0, 1, 2, 3]) == False
    assert list_check_all_even([1, 1, 1, 1]) == False
    assert list_check_all_even([2, 2, 2, 2]) == True
    assert list_check_all_even([2]) == True
    assert list_check_all_even([]) == True

@passed(has_functions)
def test_function3(test):
    """functie `list_count_even` werkt correct"""
    list_count_even = get_function("list_count_even")
    assert list_count_even([2, 4, 6, 1000]) == 4
    assert list_count_even([1, 2, 3, 4]) == 2
    assert list_count_even([4, 3, 2, 1]) == 2
    assert list_count_even([0, 1, 2, 3]) == 2
    assert list_count_even([1, 1, 1, 1]) == 0
    assert list_count_even([2, 2, 2, 2]) == 4
    assert list_count_even([2]) == 1
    assert list_count_even([]) == 0

@passed(has_functions)
def test_function1(test):
    """functie `list_get_even` werkt correct"""
    list_get_even = get_function("list_get_even")
    assert list_get_even([1, 2, 3, 4]) == [2, 4]
    assert list_get_even([4, 3, 2, 1]) == [4, 2]
    assert list_get_even([0, 1, 2, 3]) == [0, 2]
    assert list_get_even([1, 1, 1, 1]) == []
    assert list_get_even([2]) == [2]
    assert list_get_even([]) == []

@passed(has_functions)
def test_no_changes_to_list(test):
    """functie `list_get_even` doet geen aanpassing aan originele lijst"""
    arg = HistoryList([1, 2])
    result = getFunction("list_get_even")(arg)
    if len(arg.history) > 1:
        raise AssertionError("originele lijst is toch aangepast")
