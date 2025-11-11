from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `convert` is aanwezig"""
    assert function_defined_in_module("convert")
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()
    assert no_string_methods_used()

@passed(has_functions)
def test_function():
    """functie `convert` werkt correct"""
    convert = get_function("convert")
    assert convert('convertInput') == 'convert_input'
    assert convert('readFromFile') == 'read_from_file'
    assert convert('check') == 'check'
    assert convert('') == ''
