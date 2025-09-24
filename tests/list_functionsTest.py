from checkpy import *
from _basics_no_listcomp import *
from _static_analysis import *

import ast

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("same_first_last")
    assert function_defined_in_module("is_longer")
    assert function_defined_in_module("is_palindromish")
    assert function_defined_in_module("is_palindromish_eff")
    assert function_defined_in_module("filter_even")
    assert function_defined_in_module("all_even")
    assert function_defined_in_module("max_element")
    assert function_defined_in_module("element_exists")
    assert function_defined_in_module("count_occurrences")
    assert function_defined_in_module("remove_duplicates")
    assert function_defined_in_module("merge_sorted_lists")
    # assert construct_not_in_ast(ast.While)
    # assert construct_not_in_ast(ast.For)

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

@t.passed(has_functions)
def test_is_palindromish(test):
    """functie `is_palindromish` werkt correct"""
    assert getFunction("is_palindromish")([1, 2, 1]) == True
    assert getFunction("is_palindromish")([]) == True
    assert getFunction("is_palindromish")([1]) == True
    assert getFunction("is_palindromish")([0,0,1,0,0]) == True
    assert getFunction("is_palindromish")([0,0,1,0,1]) == False

@t.passed(has_functions)
def test_is_palindromish_eff(test):
    """functie `is_palindromish_eff` werkt correct"""
    assert getFunction("is_palindromish_eff")([1, 2, 1]) == True
    assert getFunction("is_palindromish_eff")([]) == True
    assert getFunction("is_palindromish_eff")([1]) == True
    assert getFunction("is_palindromish_eff")([0,0,1,0,0]) == True
    assert getFunction("is_palindromish_eff")([0,0,1,0,1]) == False

@t.passed(has_functions)
def test_filter_even(test):
    """functie `filter_even` werkt correct"""
    inp = [1,2,1]
    assert getFunction("filter_even")(inp) == [2]
    assert inp == [1,2,1], "input-lijst is aangepast, dat mag niet"

    inp = [20, 10, 34]
    assert getFunction("filter_even")(inp) == [20, 10, 34]
    assert inp == [20, 10, 34], "input-lijst is aangepast, dat mag niet"

    inp = [1]
    assert getFunction("filter_even")(inp) == []
    assert inp == [1], "input-lijst is aangepast, dat mag niet"

    inp = []
    assert getFunction("filter_even")(inp) == []
    assert inp == [], "input-lijst is aangepast, dat mag niet"

@t.passed(has_functions)
def test_all_even(test):
    """functie `all_even` werkt correct"""
    inp = [1,2,1]
    assert getFunction("all_even")(inp) == False
    assert inp == [1,2,1], "input-lijst is aangepast, dat mag niet"

    inp = [20, 10, 34]
    assert getFunction("all_even")(inp) == True
    assert inp == [20, 10, 34], "input-lijst is aangepast, dat mag niet"

    inp = [1]
    assert getFunction("all_even")(inp) == False
    assert inp == [1], "input-lijst is aangepast, dat mag niet"

    inp = []
    assert getFunction("all_even")(inp) == True
    assert inp == [], "input-lijst is aangepast, dat mag niet"

@t.passed(has_functions)
def test_max_element(test):
    """functie `max_element` werkt correct"""
    inp = [1,2,1]
    assert getFunction("max_element")(inp) == 2
    assert inp == [1,2,1], "input-lijst is aangepast, dat mag niet"

    inp = [20, 10, 34]
    assert getFunction("max_element")(inp) == 34
    assert inp == [20, 10, 34], "input-lijst is aangepast, dat mag niet"

    inp = [1]
    assert getFunction("max_element")(inp) == 1
    assert inp == [1], "input-lijst is aangepast, dat mag niet"

@t.passed(has_functions)
def test_element_exists(test):
    """functie `element_exists` werkt correct"""
    inp = [1,2,1]
    assert getFunction("element_exists")(inp,3) == False
    assert inp == [1,2,1], "input-lijst is aangepast, dat mag niet"

    inp = [20, 10, 34]
    assert getFunction("element_exists")(inp,10) == True
    assert inp == [20, 10, 34], "input-lijst is aangepast, dat mag niet"

    inp = [[1]]
    assert getFunction("element_exists")(inp,[1]) == True
    assert inp == [[1]], "input-lijst is aangepast, dat mag niet"

    inp = []
    assert getFunction("element_exists")(inp,1000) == False
    assert inp == [], "input-lijst is aangepast, dat mag niet"

@t.passed(has_functions)
def test_count_occurrences(test):
    """functie `count_occurrences` werkt correct"""
    inp = [1,2,1]
    assert getFunction("count_occurrences")(inp,1) == 2
    assert inp == [1,2,1], "input-lijst is aangepast, dat mag niet"

    inp = [20, 10, 34]
    assert getFunction("count_occurrences")(inp,10) == 1
    assert inp == [20, 10, 34], "input-lijst is aangepast, dat mag niet"

    inp = [[1]]
    assert getFunction("count_occurrences")(inp,[1]) == 1
    assert inp == [[1]], "input-lijst is aangepast, dat mag niet"

    inp = []
    assert getFunction("count_occurrences")(inp,1000) == 0
    assert inp == [], "input-lijst is aangepast, dat mag niet"

@t.passed(has_functions)
def test_remove_duplicates(test):
    """functie `remove_duplicates` werkt correct"""
    inp = [1,2,1]
    assert getFunction("remove_duplicates")(inp) == [1,2]
    assert inp == [1,2,1], "input-lijst is aangepast, dat mag niet"

    inp = ['a', 'a', 'a']
    assert getFunction("remove_duplicates")(inp) == ['a']
    assert inp == ['a', 'a', 'a'], "input-lijst is aangepast, dat mag niet"

    inp = [1]
    assert getFunction("remove_duplicates")(inp) == [1]
    assert inp == [1], "input-lijst is aangepast, dat mag niet"

    inp = []
    assert getFunction("remove_duplicates")(inp) == []
    assert inp == [], "input-lijst is aangepast, dat mag niet"

    inp = [True, False, True, False]
    assert getFunction("remove_duplicates")(inp) == [True, False]
    assert inp == [True, False, True, False], "input-lijst is aangepast, dat mag niet"

@t.passed(has_functions)
def test_merge_sorted_lists(test):
    """functie `merge_sorted_lists` werkt correct"""
    inp1 = [1,2,3]
    inp2 = [2]
    assert getFunction("merge_sorted_lists")(inp1, inp2) == [1,2,2,3]
    assert inp1 == [1,2,3] and inp2 == [2], "een input-lijst is aangepast, dat mag niet"

    inp1 = []
    inp2 = [2,2]
    assert getFunction("merge_sorted_lists")(inp1, inp2) == [2,2]
    assert inp1 == [] and inp2 == [2,2], "een input-lijst is aangepast, dat mag niet"

    inp2 = []
    inp1 = [2,2]
    assert getFunction("merge_sorted_lists")(inp1, inp2) == [2,2]
    assert inp2 == [] and inp1 == [2,2], "een input-lijst is aangepast, dat mag niet"

    inp1 = [1,2,6,7]
    inp2 = [4,5]
    assert getFunction("merge_sorted_lists")(inp1, inp2) == [1,2,4,5,6,7]
    assert inp1 == [1,2,6,7] and inp2 == [4,5], "een input-lijst is aangepast, dat mag niet"

    inp2 = [1,2,6,7]
    inp1 = [4,5]
    assert getFunction("merge_sorted_lists")(inp1, inp2) == [1,2,4,5,6,7]
    assert inp2 == [1,2,6,7] and inp1 == [4,5], "een input-lijst is aangepast, dat mag niet"
