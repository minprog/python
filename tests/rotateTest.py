from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `rotate` is aanwezig"""
    assert defines_function("rotate")
    if has_string("import Any", "[Any]"):
        raise AssertionError("gebruik geen Any als type in deze opdracht")
    assert not_in_code(ast.Set)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

@passed(has_functions)
def test_function(test):
    """functie `rotate` werkt correct"""
    rotate = get_function("rotate")

    lst = [2,3,1]; rotate(lst);
    if lst != [3,1,2]:
        raise AssertionError(f"l = [2,3,1]; rotate(l): verwachtte [3, 1, 2] maar kreeg {lst}")

    lst = [2,1,3]; rotate(lst);
    if lst != [1,3,2]:
        raise AssertionError(f"l = [2,1,3]; rotate(l): verwachtte [1, 3, 2] maar kreeg {lst}")

    lst = [2,1];   rotate(lst)
    if lst != [1,2]:
        raise AssertionError(f"l = [2,1]; rotate(l): verwachtte [1, 2] maar kreeg {lst}")

    lst = [1,2];   rotate(lst)
    if lst != [2,1]:
        raise AssertionError(f"l = [1,2]; rotate(l): verwachtte [2, 1] maar kreeg {lst}")

    lst = [1];     rotate(lst)
    if lst != [1]:
        raise AssertionError(f"l=[1]; rotate(l): verwachtte [1] maar kreeg {lst}")

    lst = [];      rotate(lst)
    if lst != []:
        raise AssertionError(f"l=[]; rotate(l): verwachtte [] maar kreeg {lst}")
