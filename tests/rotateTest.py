from ast import FunctionDef
from symtable import Function
from types import FunctionType, NoneType
from typing import Callable
from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `rotate` is aanwezig"""
    assert function_defined_in_module("rotate")
    if string_in_module("import Any", "[Any]"):
        raise AssertionError("gebruik geen Any als type in deze opdracht")
    assert construct_not_in_ast(ast.Slice)
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()
    assert no_string_methods_used()
    if string_in_module(".pop(", ".insert(", ".append(", ".copy("):
        raise AssertionError("wijzig de lijst alleen door elementen te kopiëren")

def check_mutated(f: TestableCallable, inp: list[object], out: object):
    f_name = f._func.name

    org = inp.copy()
    try:
        _ = f(inp)
        actual = inp
    except Exception as e:
        actual = str(e).split('(')[0].strip('"')
    if inp != out:
        raise AssertionError(
            f"we hebben een fout gevonden met input {org}\n"
            f"gebruik deze doctest:\n"
            f"    >>> t_lst = {org}\n"
            f"    >>> {f_name}(t_lst)\n"
            f"    >>> t_lst\n"
            f"    {out}\n"
            f"je checkt zo of de waarde van t_lst goed wordt aangepast,\n"
            f"maar nu komt dit er uit: {actual}")

@passed(has_functions)
def test_function():
    """functie `rotate` werkt correct"""
    rotate = get_function("rotate")
    assert no_input_output_in_function(rotate)
    check_mutated(rotate, [2,3,1], [3,1,2])
    check_mutated(rotate, [2,1,3], [1,3,2])
    check_mutated(rotate, [2,1], [1,2])
    check_mutated(rotate, [1,2], [2,1])
    check_mutated(rotate, [1], [1])
    check_mutated(rotate, [], [])
