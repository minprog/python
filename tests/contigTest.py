from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `contig` is aanwezig"""
    assert function_defined_in_module("contig")
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()
    assert no_string_methods_used()

@passed(has_functions)
def test_function(test):
    """functie `contig` werkt correct"""
    contig = get_function("contig")
    assert contig([0,1,2,4,5]) == [[0,1,2], [4,5]]
    assert contig([0,1,2,3])   == [[0,1,2,3]]
    assert contig([2,3,5])     == [[2,3], [5]]
    assert contig([2,4,6])     == [[2], [4], [6]]
    assert contig([])          == []

@passed(has_functions)
def test_no_changes_to_list(test):
    """functie `contig` doet geen aanpassing aan originele lijst"""
    arg = HistoryList([1, 3])
    result = getFunction("contig")(arg)
    if len(arg.history) > 1:
        raise AssertionError("originele lijst is toch aangepast")
