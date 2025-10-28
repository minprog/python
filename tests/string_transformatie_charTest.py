from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("l337sp34k")
    assert function_defined_in_module("blackout")
    assert function_defined_in_module("replace_char")

    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)

@passed(has_functions)
def test_function_l337sp34k(test):
    """functie `l337sp34k` werkt correct"""
    l337sp34k = get_function("l337sp34k")
    assert l337sp34k("leetspeak") == "l337sp34k"
    assert l337sp34k("leeTspeaK") == "l337sp34K"
    assert l337sp34k("l337sp34k") == "l337sp34k"
    assert l337sp34k("leet leet") == "l337 l337"
    assert l337sp34k("") == ""

@passed(has_functions)
def test_function_blackout(test):
    """functie `blackout` werkt correct"""
    blackout = get_function("blackout")
    assert blackout("blackout") == "########"
    assert blackout("black out") == "##### ###"
    assert blackout("secret8hundred") == "######8#######"
    assert blackout("A") == "#"
    assert blackout("") == ""

@passed(has_functions)
def test_function_replace_char(test):
    """functie `replace_char` werkt correct"""
    replace_char = get_function("replace_char")
    assert replace_char("replace_char", 'a', 'b') == 'replbce_chbr'
    assert replace_char("replace_char", 'r', 'R') == 'Replace_chaR'
    assert replace_char("replace_char", '_', '-') == "replace-char"
    assert replace_char("R", 'R', 'r') == "r"
    assert replace_char("R", 'R', 'R') == "R"
    assert replace_char("", 'R', 'r') == ""
    assert replace_char("R", 'R', '') == ""
