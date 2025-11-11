from checkpy import *
from _pyprog_tools import *

from checkpy.lib import io

from _python_checks import checkstyle, forbidden_constructs, mypy_strict#, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict)#, doctest_all)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("print_collatz")
    assert function_defined_in_module("collatz_length")

    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert construct_not_in_ast(ast.In)

@passed(has_functions)
def test_print_collatz():
    """functie `print_collatz` werkt correct voor 3 en 9"""
    func = get_function("print_collatz")
    res = "3 10 5 16 8 4 2 1"
    res = res.replace(" ", "\n") + "\n"
    with io.captureStdout() as stdout:
        func(3)
        assert RunResult(stdout.content) == res
    res = "9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1"
    res = res.replace(" ", "\n") + "\n"
    with io.captureStdout() as stdout:
        func(9)
        assert RunResult(stdout.content) == res

@passed(has_functions)
def test_collatz_length():
    """functie `collatz_length` werkt correct"""
    collatz_length = get_function("collatz_length")
    assert no_input_output_in_function(collatz_length)
    assert collatz_length(3) == 8
