from checkpy import *
from _static_analysis import *

from _basics_no_listcomp import *
# from _check_doctests import require_doctests_for_all_functions

@t.passed(doctest_ok)
def has_functions():
    """functie `print_bits` is aanwezig"""
    assert defines_function("print_bits")

# @t.passed(has_functions)
# def test_print_bits(test):
#     """functie `print_bits` werkt correct"""
#     assert getFunction("print_bits")(3) == 4
#     assert getFunction("print_bits")(50) == 15
#     assert getFunction("print_bits")(0) == 5
#     assert getFunction("print_bits")(10) == 0

@t.passed(has_functions)
def test_program_50(test):
    """het programma werkt correct met invoer 50"""
    assert outputOf(stdinArgs=[50], overwriteAttributes=[("__name__", "__main__")]) == "0\n0\n1\n1\n0\n0\n1\n0\n"

@t.passed(has_functions)
def test_program_1(test):
    """het programma werkt correct met invoer 1"""
    assert outputOf(stdinArgs=[1], overwriteAttributes=[("__name__", "__main__")]) == "0\n0\n0\n0\n0\n0\n0\n1\n"

@t.passed(has_functions)
def test_program_128(test):
    """het programma werkt correct met invoer 128"""
    assert outputOf(stdinArgs=[128], overwriteAttributes=[("__name__", "__main__")]) == "1\n0\n0\n0\n0\n0\n0\n0\n"
