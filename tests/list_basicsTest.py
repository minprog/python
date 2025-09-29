from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """alle vier de functies zijn aanwezig"""
    assert function_defined_in_module("list_contains_element")
    assert function_defined_in_module("list_contains_no_element")
    assert function_defined_in_module("list_count_element")
    assert function_defined_in_module("list_count_elements")
    assert construct_in_ast(ast.For)
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()
    assert no_string_methods_used()

@passed(has_functions)
def test_function1(test):
    """functie `list_contains_element` werkt correct"""
    list_contains_element = get_function("list_contains_element")
    assert list_contains_element([1, 2, 3, 4], 4) == True
    assert list_contains_element([4, 3, 2, 1], 4) == True
    assert list_contains_element([2], 0) == False
    assert list_contains_element([], 0) == False
    assert list_contains_element([0, 1, 2, 3], -1) == False
    assert list_contains_element([1, 1, 1, 1], 'a') == False
    assert list_contains_element(['a'], 'a') == True
    assert list_contains_element(['a'], 'b') == False

@passed(has_functions)
def test_function1a(test):
    """functie `list_contains_no_element` werkt correct"""
    list_contains_no_element = get_function("list_contains_no_element")
    assert list_contains_no_element([1, 2, 3, 4], 4) == False
    assert list_contains_no_element([4, 3, 2, 1], 4) == False
    assert list_contains_no_element([2], 0) == True
    assert list_contains_no_element([], 0) == True
    assert list_contains_no_element([0, 1, 2, 3], -1) == True
    assert list_contains_no_element([1, 1, 1, 1], 'a') == True
    assert list_contains_no_element(['a'], 'a') == False
    assert list_contains_no_element(['a'], 'b') == True

@passed(has_functions)
def test_function2(test):
    """functie `list_count_element` werkt correct"""
    list_count_element = get_function("list_count_element")
    assert list_count_element([2, 4, 6, 1000], 2) == 1
    assert list_count_element([1, 2, 3, 4], 4) == 1
    assert list_count_element([1, 1], 1) == 2
    assert list_count_element([1, 1], 2) == 0
    assert list_count_element(['a', 'b'], 'a') == 1
    assert list_count_element(['b'], 'a') == 0
    assert list_count_element([], 'a') == 0
    assert list_count_element([], 0) == 0

@passed(has_functions)
def test_function3(test):
    """functie `list_count_elements` werkt correct"""
    list_count_elements = get_function("list_count_elements")
    assert list_count_elements([2, 4, 6, 1000], [2]) == 1
    assert list_count_elements([1, 2, 3, 4], [1, 2]) == 2
    assert list_count_elements([1, 1], [1]) == 2
    assert list_count_elements([1, 1], [2, 3]) == 0
    assert list_count_elements(['a', 'b', 'a'], ['a', 'b']) == 3
    assert list_count_elements(['b'], ['a']) == 0
    assert list_count_elements([], ['a', 'b']) == 0
    assert list_count_elements([], [1000]) == 0
    assert list_count_elements(['a'], []) == 0
