from checkpy import *
from _pyprog_tools import *

import ast
from checkpy import static

import _catch_syntax_error
from _catch_syntax_error import no_syntax_error
_catch_syntax_error.MAX_SYNTAX_ERRORS = 2

def defined(name):
    assert function_defined_in_module(name)
    return get_function(name)

def loops_without_search(name):
    """Checks that `name` loops over its list and does not search with `in`, `find` or `index`."""
    assert function_defined_in_module(name)
    tree = ast.parse(static.getSource())
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == name:
            body = list(ast.walk(node))
            if not any(isinstance(n, (ast.For, ast.While)) for n in body):
                raise AssertionError(f"`{name}` moet een loop gebruiken")
            for n in body:
                if isinstance(n, ast.Compare) and any(isinstance(op, (ast.In, ast.NotIn)) for op in n.ops):
                    raise AssertionError(f"`{name}` mag `in` niet gebruiken")
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr in ['find', 'index', 'count']:
                    raise AssertionError(f"`{name}` mag {n.func.attr}() niet gebruiken")
    return True

def loops(name):
    """Checks that `name` loops over its list."""
    assert function_defined_in_module(name)
    tree = ast.parse(static.getSource())
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == name:
            if not any(isinstance(n, (ast.For, ast.While)) for n in ast.walk(node)):
                raise AssertionError(f"`{name}` moet een loop gebruiken")
    return True

@test()
def test_make_list():
    """functie `make_list` werkt correct"""
    f = defined("make_list")
    assert f() == [1, 2, 3]

@test()
def test_first_item():
    """functie `first_item` werkt correct"""
    f = defined("first_item")
    assert f([10, 20, 30]) == 10
    assert f([7]) == 7
    assert f([-4, 8]) == -4

@test()
def test_last_item():
    """functie `last_item` werkt correct"""
    f = defined("last_item")
    assert f([10, 20, 30]) == 30
    assert f([5]) == 5
    assert f([8, -4]) == -4

@test()
def test_first_two():
    """functie `first_two` werkt correct"""
    f = defined("first_two")
    assert f([10, 20, 30, 40]) == [10, 20]
    assert f([1, 2]) == [1, 2]
    assert f([5, 6, 7]) == [5, 6]

@test()
def test_replace_first():
    """functie `replace_first` werkt correct"""
    f = defined("replace_first")
    letters = ["x", "y", "z"]
    assert f(letters, "A").is_(None)
    assert letters == ["A", "y", "z"], "de list is niet aangepast"
    one = ["q"]
    f(one, "r")
    assert one == ["r"], "de list is niet aangepast"

@test()
def test_add_last():
    """functie `add_last` werkt correct"""
    f = defined("add_last")
    numbers = [1, 2]
    assert f(numbers, 3).is_(None)
    assert numbers == [1, 2, 3], "de list is niet aangepast"
    empty = []
    f(empty, 9)
    assert empty == [9], "de list is niet aangepast"

@test()
def test_add_at():
    """functie `add_at` werkt correct"""
    f = defined("add_at")
    letters = ["a", "c"]
    assert f(letters, 1, "b").is_(None)
    assert letters == ["a", "b", "c"], "de list is niet aangepast"
    more = ["b", "c"]
    f(more, 0, "a")
    assert more == ["a", "b", "c"], "de list is niet aangepast"

@test()
def test_remove_first():
    """functie `remove_first` werkt correct"""
    f = defined("remove_first")
    numbers = [1, 2, 3, 2]
    assert f(numbers, 2).is_(None)
    assert numbers == [1, 3, 2], "de list is niet aangepast"
    other = [5, 5, 5]
    f(other, 5)
    assert other == [5, 5], "de list is niet aangepast"

@test()
def test_take_last():
    """functie `take_last` werkt correct"""
    f = defined("take_last")
    numbers = [1, 2, 3]
    assert f(numbers) == 3
    assert numbers == [1, 2], "de list is niet aangepast"
    one = [4]
    assert f(one) == 4
    assert one == [], "de list is niet aangepast"

@test()
def test_combine():
    """functie `combine` werkt correct"""
    f = defined("combine")
    assert f([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert f([], [5]) == [5]
    assert f([5], []) == [5]
    assert f([], []) == []
    a, b = [1], [2]
    f(a, b)
    assert a == [1] and b == [2], "de originele lists zijn aangepast"

@test()
def test_zeros():
    """functie `zeros` werkt correct"""
    f = defined("zeros")
    assert f(3) == [0, 0, 0]
    assert f(0) == []
    assert f(1) == [0]

@test()
def test_has_value():
    """functie `has_value` werkt correct"""
    f = defined("has_value")
    assert f(["a", "b", "c"], "b").is_(True)
    assert f(["a", "b", "c"], "z").is_(False)
    assert f([], "a").is_(False)

@test()
def test_count_value():
    """functie `count_value` werkt correct"""
    f = defined("count_value")
    assert f([1, 2, 2, 3], 2) == 2
    assert f([1, 2, 3], 9) == 0
    assert f([4, 4, 4], 4) == 3
    assert f([], 1) == 0

@test()
def test_position():
    """functie `position` werkt correct"""
    f = defined("position")
    assert f(["a", "b", "c"], "c") == 2
    assert f(["a", "b", "c"], "z") == -1
    assert f(["a", "b", "a"], "a") == 0
    assert f([], "a") == -1

@test()
def test_total():
    """functie `total` werkt correct"""
    f = defined("total")
    assert loops("total")
    assert f([1, 2, 3]) == 6
    assert f([]) == 0
    assert f([-1, 1, 5]) == 5

@test()
def test_biggest():
    """functie `biggest` werkt correct"""
    f = defined("biggest")
    assert loops("biggest")
    assert f([3, 9, 2]) == 9
    assert f([-5, -2, -8]) == -2
    assert f([7]) == 7
    assert f([9, 3, 2]) == 9

@test()
def test_list_count_element():
    """functie `list_count_element` werkt correct"""
    f = defined("list_count_element")
    assert loops("list_count_element")
    assert f([2, 4, 6, 1000], 2) == 1
    assert f([1, 2, 3, 4], 4) == 1
    assert f([1, 1], 1) == 2
    assert f([1, 1], 2) == 0
    assert f(['a', 'b'], 'a') == 1
    assert f(['b'], 'a') == 0
    assert f([], 'a') == 0
    assert f([], 0) == 0

@test()
def test_list_count_even():
    """functie `list_count_even` werkt correct"""
    f = defined("list_count_even")
    assert loops("list_count_even")
    assert f([2, 4, 6, 1000]) == 4
    assert f([1, 2, 3, 4]) == 2
    assert f([4, 3, 2, 1]) == 2
    assert f([0, 1, 2, 3]) == 2
    assert f([1, 1, 1, 1]) == 0
    assert f([2, 2, 2, 2]) == 4
    assert f([2]) == 1
    assert f([]) == 0

@test()
def test_positives():
    """functie `positives` werkt correct"""
    f = defined("positives")
    assert f([-2, 0, 5, 7, -1]) == [5, 7]
    assert f([-1, -2]) == []
    assert f([3, 1, 2]) == [3, 1, 2]
    assert f([]) == []

@test()
def test_multiply_all():
    """functie `multiply_all` werkt correct"""
    f = defined("multiply_all")
    assert f([1, 2, 3], 10) == [10, 20, 30]
    assert f([], 3) == []
    numbers = [1, 2]
    assert f(numbers, 5) == [5, 10]
    assert numbers == [1, 2], "de list die je meekrijgt is aangepast"

@test()
def test_list_get_even():
    """functie `list_get_even` werkt correct"""
    f = defined("list_get_even")
    assert loops("list_get_even")
    assert f([1, 2, 3, 4]) == [2, 4]
    assert f([4, 3, 2, 1]) == [4, 2]
    assert f([0, 1, 2, 3]) == [0, 2]
    assert f([1, 1, 1, 1]) == []
    assert f([2]) == [2]
    assert f([]) == []
    numbers = [1, 2, 3, 4]
    f(numbers)
    assert numbers == [1, 2, 3, 4], "de list die je meekrijgt is aangepast"

@test()
def test_list_count_elements():
    """functie `list_count_elements` werkt correct"""
    f = defined("list_count_elements")
    assert loops("list_count_elements")
    assert f([2, 4, 6, 1000], [2]) == 1
    assert f([1, 2, 3, 4], [1, 2]) == 2
    assert f([1, 1], [1]) == 2
    assert f([1, 1], [2, 3]) == 0
    assert f(['a', 'b', 'a'], ['a', 'b']) == 3
    assert f(['b'], ['a']) == 0
    assert f([], ['a', 'b']) == 0
    assert f([], [1000]) == 0
    assert f(['a'], []) == 0

@test()
def test_is_sorted():
    """functie `is_sorted` werkt correct"""
    f = defined("is_sorted")
    assert f([1, 2, 2, 5]).is_(True)
    assert f([1, 3, 2]).is_(False)
    assert f([]).is_(True)
    assert f([4]).is_(True)
    assert f([3, 2, 1]).is_(False)
    assert f([1, 2, 3, 2]).is_(False)

@test()
def test_list_check_all_even():
    """functie `list_check_all_even` werkt correct"""
    f = defined("list_check_all_even")
    assert loops("list_check_all_even")
    assert f([2, 4, 6, 1000]).is_(True)
    assert f([1, 2, 3, 4]).is_(False)
    assert f([4, 3, 2, 1]).is_(False)
    assert f([0, 1, 2, 3]).is_(False)
    assert f([1, 1, 1, 1]).is_(False)
    assert f([2, 2, 2, 2]).is_(True)
    assert f([2]).is_(True)
    assert f([]).is_(True)

@test()
def test_list_contains_element():
    """functie `list_contains_element` werkt correct"""
    f = defined("list_contains_element")
    assert loops_without_search("list_contains_element")
    assert f([1, 2, 3, 4], 4).is_(True)
    assert f([4, 3, 2, 1], 4).is_(True)
    assert f([2], 0).is_(False)
    assert f([], 0).is_(False)
    assert f([0, 1, 2, 3], -1).is_(False)
    assert f([1, 1, 1, 1], 'a').is_(False)
    assert f(['a'], 'a').is_(True)
    assert f(['a'], 'b').is_(False)

@test()
def test_list_contains_no_element():
    """functie `list_contains_no_element` werkt correct"""
    f = defined("list_contains_no_element")
    assert loops_without_search("list_contains_no_element")
    assert not call_in_module("list_contains_element"), "je mag `list_contains_element` niet aanroepen"
    assert f([1, 2, 3, 4], 4).is_(False)
    assert f([4, 3, 2, 1], 4).is_(False)
    assert f([2], 0).is_(True)
    assert f([], 0).is_(True)
    assert f([0, 1, 2, 3], -1).is_(True)
    assert f([1, 1, 1, 1], 'a').is_(True)
    assert f(['a'], 'a').is_(False)
    assert f(['a'], 'b').is_(True)
