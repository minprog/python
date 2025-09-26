from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functies `coleman_liau` en `calculate_grade` zijn aanwezig"""
    assert function_defined_in_module("coleman_liau")
    assert function_defined_in_module("calculate_grade")
    assert construct_in_ast(ast.For)
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()
    assert no_string_methods_used()

@passed(has_functions)
def checks_coleman_liau(test):
    """functie `coleman_liau` werkt correct"""
    coleman_liau = get_function("coleman_liau")
    assert coleman_liau(100, 5, 500) == 12

@passed(has_functions)
def checks_calculate_grade(test):
    """functie `calculate_grade` werkt correct"""
    calculate_grade = get_function("calculate_grade")
    assert calculate_grade("One fish. Two fish. Red fish. Blue fish.") == -9

@passed(has_functions)
def checks_tekst1(test):
    """geeft Grade 7 voor "In my younger and more..." """
    run(
        "In my younger and more vulnerable years my father gave me "
        "some advice that I've been turning over in my mind ever since."
    ).strip() == "Grade 7"
    # hint: "zorg dat de output exact zo is als in de voorbeelden"

@passed(has_functions)
def checks_tekst2(test):
    """geeft Grade 10 voor "It was a bright cold day..." """
    run(
        "It was a bright cold day in April, and the clocks were striking "
        "thirteen. Winston Smith, his chin nuzzled into his breast in an "
        "effort to escape the vile wind, slipped quickly through the glass "
        "doors of Victory Mansions, though not quickly enough to prevent a "
        "swirl of gritty dust from entering along with him."
    ).strip() == "Grade 10"
