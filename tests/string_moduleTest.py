from checkpy import *
from _basics_no_listcomp import *
from _static_analysis import *

import ast

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("isalpha")
    assert function_defined_in_module("islower")
    assert function_defined_in_module("isupper")
    assert function_defined_in_module("isdigit")
    assert function_defined_in_module("isblank")
    assert not string_in_module("defghijklmnopqrstuvw"), "gebruik de variabelen uit de string-module voor deze opdracht"
    assert not string_in_module("DEFGHIJKLMNOPQRSTUVW"), "gebruik de variabelen uit de string-module voor deze opdracht"
    assert not string_in_module("123456789"), "gebruik de variabelen uit de string-module voor deze opdracht"
    assert string_in_module(".ascii_lowercase"), "gebruik de variabelen uit de string-module voor deze opdracht"
    assert string_in_module(".ascii_uppercase"), "gebruik de variabelen uit de string-module voor deze opdracht"
    assert string_in_module(".whitespace"), "gebruik de variabelen uit de string-module voor deze opdracht"

@t.passed(has_functions)
def test_isalpha(test):
    """functie `isalpha` werkt correct"""
    assert getFunction("isalpha")('a') == True
    assert getFunction("isalpha")('9') == False
    assert getFunction("isalpha")('e') == True
    assert getFunction("isalpha")('á') == False
    assert getFunction("isalpha")(' ') == False

@t.passed(has_functions)
def test_islower(test):
    """functie `islower` werkt correct"""
    assert getFunction("islower")('a') == True
    assert getFunction("islower")('9') == False
    assert getFunction("islower")('e') == True
    assert getFunction("islower")('A') == False
    assert getFunction("islower")(' ') == False

@t.passed(has_functions)
def test_isupper(test):
    """functie `isupper` werkt correct"""
    assert getFunction("isupper")('A') == True
    assert getFunction("isupper")('9') == False
    assert getFunction("isupper")('e') == False
    assert getFunction("isupper")('á') == False
    assert getFunction("isupper")(' ') == False

@t.passed(has_functions)
def test_isdigit(test):
    """functie `isdigit` werkt correct"""
    assert getFunction("isdigit")('A') == False
    assert getFunction("isdigit")('9') == True
    assert getFunction("isdigit")('e') == False
    assert getFunction("isdigit")('á') == False
    assert getFunction("isdigit")(' ') == False

@t.passed(has_functions)
def test_isblank(test):
    """functie `isblank` werkt correct"""
    assert getFunction("isblank")('A') == False
    assert getFunction("isblank")('9') == False
    assert getFunction("isblank")('e') == False
    assert getFunction("isblank")('á') == False
    assert getFunction("isblank")(' ') == True
