from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `convert` is aanwezig"""
    assert defines_function("convert")
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

@passed(has_functions)
def test_function(test):
    """functie `convert` werkt correct"""
    convert = get_function("convert")
    assert convert('convertInput') == 'convert_input'
    assert convert('readFromFile') == 'read_from_file'
    assert convert('check') == 'check'
    assert convert('') == ''
