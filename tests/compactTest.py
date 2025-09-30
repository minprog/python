import typing

from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `compact` is aanwezig"""
    assert function_defined_in_module("compact")
    if string_in_module("import Any", "[Any]"):
        raise AssertionError("gebruik geen Any als type in deze opdracht")
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()
    assert no_string_methods_used()
    # assert construct_not_in_ast(typing.Any)

def check_mutated(f, inp, out):
    f_name = f._func.name

    org = inp.copy()
    f(inp)
    if inp != out:
        raise AssertionError(
            f"gebruik deze doctest:\n"
            f"    >>> t_lst = {org}\n"
            f"    >>> {f_name}(t_lst)\n"
            f"    >>> t_lst\n"
            f"    {out}\n"
            f"dus dit zou de aangepaste waarde van t_lst moeten zijn,\n"
            f"maar bij check bleek de waarde van t_lst: {inp}")

@passed(has_functions)
def test_function(test):
    """functie `compact` werkt correct"""
    compact = get_function("compact")

    assert compact([0]) == []
    assert compact([False]) == []
    assert compact(['']) == []
    assert compact([[]]) == []
    assert compact([0, False, '']) == []
    assert compact([2, 0, False, '']) == [2]
    assert compact([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert compact([False, 1, 2, 3, 4]) == [1, 2, 3, 4]
