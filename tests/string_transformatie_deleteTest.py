from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("verwijder_n")
    assert function_defined_in_module("verwijder_n_eind")
    assert function_defined_in_module("verwijder_n_begin")

    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)

@passed(has_functions)
def test_function_verwijder_n(test):
    """functie `verwijder_n` werkt correct"""
    verwijder_n = get_function("verwijder_n")
    assert verwijder_n("aanvang") == "aavag"
    assert verwijder_n("noodgeval") == "oodgeval"
    assert verwijder_n("verwijder_n") == "verwijder_"
    assert verwijder_n("leen leen") == "lee lee"
    assert verwijder_n("n") == ""
    assert verwijder_n("") == ""

@passed(has_functions)
def test_function_verwijder_n_eind(test):
    """functie `verwijder_n_eind` werkt correct"""
    verwijder_n_eind = get_function("verwijder_n_eind")
    assert verwijder_n_eind("ik meen het") == "ik mee het"
    assert verwijder_n_eind("niet doen") == "niet doe"
    assert verwijder_n_eind("zo'n hele maan") == "zo' hele maa"
    assert verwijder_n_eind("leen leen") == "lee lee"
    assert verwijder_n_eind("n") == ""
    assert verwijder_n_eind("") == ""

@passed(has_functions)
def test_function_verwijder_n_begin(test):
    """functie `verwijder_n_begin` werkt correct"""
    verwijder_n_begin = get_function("verwijder_n_begin")
    assert verwijder_n_begin("namens deze") == "amens deze"
    assert verwijder_n_begin("niet doen") == "iet doen"
    assert verwijder_n_begin("zo'n hele maan") == "zo'n hele maan"
    assert verwijder_n_begin("leen neel") == "leen eel"
    assert verwijder_n_begin("n") == ""
    assert verwijder_n_begin("") == ""
