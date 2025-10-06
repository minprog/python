from checkpy import *
from _pyprog_tools import *

import re

from _python_checks import forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("longest_word_from_list")
    assert function_defined_in_module("print_banner")
    assert function_defined_in_module("string_to_list")
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    if string_in_module(".split("):
        raise AssertionError("je mag geen .split() gebruiken voor deze opdracht")

@passed(has_functions)
def test_longest_word_from_list():
    """functie `longest_word_from_list` werkt correct"""
    longest_word_from_list = get_function("longest_word_from_list")
    assert longest_word_from_list(['A']) == 'A'
    assert longest_word_from_list(['Aap', 'Nootje', 'Mies']) == 'Nootje'
    assert longest_word_from_list(['Werkt']) == 'Werkt'

@passed(has_functions)
def test_string_to_list():
    """functie `string_to_list` werkt correct voor simpele strings"""
    string_to_list = get_function("string_to_list")
    assert string_to_list('A') == ['A']
    assert string_to_list('Aap Noot Mies') == ['Aap', 'Noot', 'Mies']
    assert string_to_list('Werkt') == ['Werkt']
    assert string_to_list('') == []

@passed(has_functions)
def test_pizza(test):
    """print de juiste banner voor de pizza-zaak"""
    from checkpy.lib import  io
    # import contextlib

    inp = ["Margherita",
           "Tutta",
           "la",
           "Vita"]

    res = ("##########\n"
           "Margherita\n"
           "Tutta\n"
           "la\n"
           "Vita\n"
           "##########\n")

    print_banner = get_function("print_banner")
    # buf = io.StringIO()
    with io.captureStdout() as stdout:
        print_banner(inp)
        assert stdout.content == res

@passed(has_functions)
def test_run_pizza():
    """programma: print de juiste banner voor de pizza-zaak"""
    res = ("##########\n"
           "Margherita\n"
           "Tutta\n"
           "la\n"
           "Vita\n"
           "##########\n")
    assert run("Margherita Tutta la Vita") == res
