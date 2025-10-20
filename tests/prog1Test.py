from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs)
def test_eisen():
    """dubbelcheck toegestane/verplichte Python-constructies"""
    assert construct_not_in_ast(ast.If)
    assert construct_not_in_ast(ast.While)
    assert construct_not_in_ast(ast.For)
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert construct_not_in_ast(ast.In)

@passed(checkstyle, forbidden_constructs)
def test_program1(test):
    """het programma print na invoer van `hallo` dit woord nog eens op drie losse regels"""
    assert run('hallo') == "hallo\nhallo\nhallo\n"

@passed(checkstyle, forbidden_constructs)
def test_program2(test):
    """het programma print na invoer van `Toedeloe` dit woord nog eens op drie losse regels"""
    assert run('Toedeloe') == "Toedeloe\nToedeloe\nToedeloe\n"
