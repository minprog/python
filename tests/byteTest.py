from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `print_bits` is aanwezig"""
    assert function_defined_in_module("print_bits")
    assert construct_not_in_ast(ast.For)
    assert construct_not_in_ast(ast.While)

# @passed(has_functions)
# def test_print_bits(test):
#     """functie `print_bits` werkt correct"""
#     assert getFunction("print_bits")(3) == 4
#     assert getFunction("print_bits")(50) == 15
#     assert getFunction("print_bits")(0) == 5
#     assert getFunction("print_bits")(10) == 0

@passed(has_functions)
def test_program_50(test):
    """het programma werkt correct met invoer 50"""
    assert run(50) == "0\n0\n1\n1\n0\n0\n1\n0\n"

@passed(has_functions)
def test_program_1(test):
    """het programma werkt correct met invoer 1"""
    assert run(1) == "0\n0\n0\n0\n0\n0\n0\n1\n"

@passed(has_functions)
def test_program_128(test):
    """het programma werkt correct met invoer 128"""
    assert run(128) == "1\n0\n0\n0\n0\n0\n0\n0\n"
