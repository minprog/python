from checkpy import *
from _basics_no_listcomp import *
from _pyprog_tools import *

import ast

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("number_of_Os")
    assert function_defined_in_module("first_O")
    assert function_defined_in_module("number_of_letters")
    assert function_defined_in_module("where_letter")
    assert function_defined_in_module("total_occurrences")
    assert string_in_module(".count"), "gebruik de opgegeven methodes in je oplossing"
    assert string_in_module(".find"), "gebruik de opgegeven methodes in je oplossing"
    assert construct_not_in_ast(ast.While)
    assert construct_not_in_ast(ast.For)

@t.passed(has_functions)
def test_number_of_Os(test):
    """functie `number_of_Os` werkt correct"""
    assert getFunction("number_of_Os")('ooo') == 3
    assert getFunction("number_of_Os")('') == 0
    assert getFunction("number_of_Os")('yoyoyo') == 3
    assert getFunction("number_of_Os")('blo') == 1

@t.passed(has_functions)
def test_first_O(test):
    """functie `first_O` werkt correct"""
    assert getFunction("first_O")('ooo') == 0
    assert getFunction("first_O")('yo') == 1

@t.passed(has_functions)
def test_number_of_letters(test):
    """functie `number_of_letters` werkt correct"""
    assert getFunction("number_of_letters")('a', 'a') == 1
    assert getFunction("number_of_letters")('aaa', 'a') == 3
    assert getFunction("number_of_letters")('o', 'o') == 1
    assert getFunction("number_of_letters")('', 'a') == 0

@t.passed(has_functions)
def test_where_letter(test):
    """functie `where_letter` werkt correct"""
    assert getFunction("where_letter")('ooo', 'o') == 0
    assert getFunction("where_letter")('ao', 'o') == 1
    assert getFunction("where_letter")('aaa', 'a') == 0
    assert getFunction("where_letter")('ya', 'a') == 1

@t.passed(has_functions)
def test_total_occurrences(test):
    """functie `total_occurrences` werkt correct"""
    assert getFunction("total_occurrences")('color', 'yellow', 'l') == 3
    assert getFunction("total_occurrences")('red', 'blue', 'l') == 1
    assert getFunction("total_occurrences")('green', 'purple', 'b') == 0
    assert getFunction("total_occurrences")('', 'glitter', 'r') == 1
