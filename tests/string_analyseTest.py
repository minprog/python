from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("isspace")
    assert function_defined_in_module("isvowel")
    assert function_defined_in_module("has_single_vowel")
    assert function_defined_in_module("count_vowels")

    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    # assert construct_not_in_ast(ast.In)

@passed(has_functions)
def test_function_isspace():
    """functie `isspace` werkt correct"""
    isspace = get_function("isspace")
    assert isspace(" ") == True
    assert isspace("\t") == True
    assert isspace("\n") == True
    assert isspace("\\n") == False
    assert isspace("A") == False
    assert isspace("a") == False
    assert isspace("space") == False
    assert isspace("") == False

@passed(has_functions)
def test_function_isvowel():
    """functie `isvowel` werkt correct"""
    isvowel = get_function("isvowel")
    assert isvowel("a") == True
    assert isvowel("e") == True
    assert isvowel("i") == True
    assert isvowel("o") == True
    assert isvowel("u") == True
    assert isvowel("y") == False
    assert isvowel("aa") == True
    assert isvowel("slim") == False
    assert isvowel("im") == False
    assert isvowel("imma") == False
    assert isvowel("A") == False
    assert isvowel("aeiou") == True
    assert isvowel("") == True

@passed(has_functions)
def test_function_has_single_vowel():
    """functie `has_single_vowel` werkt correct"""
    has_single_vowel = get_function("has_single_vowel")
    assert has_single_vowel("a") == True
    assert has_single_vowel("e") == True
    assert has_single_vowel("i") == True
    assert has_single_vowel("o") == True
    assert has_single_vowel("u") == True
    assert has_single_vowel("y") == False
    assert has_single_vowel("bims") == True
    assert has_single_vowel("smib") == True
    assert has_single_vowel("yolo") == False
    assert has_single_vowel("rough") == False
    assert has_single_vowel("") == False

@passed(has_functions)
def test_function_count_vowels():
    """functie `count_vowels` werkt correct"""
    count_vowels = get_function("count_vowels")
    assert count_vowels("a") == 1
    assert count_vowels("e") == 1
    assert count_vowels("i") == 1
    assert count_vowels("o") == 1
    assert count_vowels("u") == 1
    assert count_vowels("y") == 0
    assert count_vowels("t") == 0
    assert count_vowels("A") == 0
    assert count_vowels("bam") == 1
    assert count_vowels("space") == 2
    assert count_vowels("yolo") == 2
    assert count_vowels("hoedan") == 3
    assert count_vowels("") == 0
