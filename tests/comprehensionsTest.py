from checkpy import *
from _basics import *
from _static_analysis import *

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert defines_function("four_random_letters")
    assert defines_function("ten_odd_plus_five")
    assert defines_function("password_numeric_analysis")
    assert defines_function("numbers_list_from_password")
    assert defines_function("numbers_from_password")
    assert not_in_code(ast.If)
    assert not_in_code(ast.While)
    assert not_in_code(ast.For)

@t.passed(has_functions)
def test_four_random_letters(test):
    """functie `four_random_letters` werkt correct"""
    assert getFunction("four_random_letters")("A") == ['A','A','A','A']
    assert getFunction("four_random_letters")("BBB") == ['B','B','B','B']
    assert len(getFunction("four_random_letters")("A")) == 4

@t.passed(has_functions)
def test_ten_odd_plus_five(test):
    """functie `ten_odd_plus_five` werkt correct"""
    if getFunction("ten_odd_plus_five")(3) != [6, 8, 10]:
        raise AssertionError("als n=3 moet er [6, 8, 10] uitkomen")
    if getFunction("ten_odd_plus_five")(1) != [6]:
        raise AssertionError("als n=1 moet er [6] uitkomen")
    if getFunction("ten_odd_plus_five")(0) != []:
        raise AssertionError("als n=0 moet er [] uitkomen")

@t.passed(has_functions)
def test_password_numeric_analysis(test):
    """functie `password_numeric_analysis` werkt correct"""
    assert getFunction("password_numeric_analysis")('1') == [True]
    assert getFunction("password_numeric_analysis")('a') == [False]
    assert getFunction("password_numeric_analysis")('1ab4A') == [True, False, False, True, False]

@t.passed(has_functions)
def test_numbers_list_from_password(test):
    """functie `numbers_list_from_password` werkt correct"""
    if getFunction("numbers_list_from_password")('a1m!') != [1]:
        raise AssertionError("bij input 'a1m!' moet er [1] uitkomen")
    if getFunction("numbers_list_from_password")('') != []:
        raise AssertionError("bij input '' moet er [] uitkomen")
    if getFunction("numbers_list_from_password")('a') != []:
        raise AssertionError("bij input 'a' moet er [] uitkomen")

@t.passed(has_functions)
def test_numbers_from_password(test):
    """functie `numbers_from_password` werkt correct"""
    assert getFunction("numbers_from_password")('a1m!') == "1"
    assert getFunction("numbers_from_password")('') == ""
    assert getFunction("numbers_from_password")('a') == ""
