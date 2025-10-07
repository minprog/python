from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
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

def check_mutated(f, inp, out):
    f_name = f._func.name

    org = inp.copy()
    try:
        f(inp)
    except Exception as e:
        inp = str(e).split('(')[0].strip('"')
    if inp != out:
        raise AssertionError(
            f"gebruik deze doctest:\n"
            f"    >>> t_lst = {org}\n"
            f"    >>> {f_name}(t_lst)\n"
            f"    >>> t_lst\n"
            f"    {out}\n"
            f"je checkt zo of de waarde van t_lst goed wordt aangepast,\n"
            f"maar nu komt dit er uit: {inp}")

@passed(has_functions)
def test_function(test):
    """functie `rotate` werkt correct"""
    rotate = get_function("rotate")
    assert no_print_return_in_function(rotate)
    check_mutated(rotate, [2,3,1], [3,1,2])
    check_mutated(rotate, [2,1,3], [1,3,2])
    check_mutated(rotate, [2,1], [1,2])
    check_mutated(rotate, [1,2], [2,1])
    check_mutated(rotate, [1], [1])
    check_mutated(rotate, [], [])
