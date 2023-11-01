from checkpy import *
from _basics_no_listcomp import *
from _static_analysis import *

import ast

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert defines_function("isalpha")
    assert defines_function("islower")
    assert defines_function("isupper")
    assert defines_function("isdigit")
    assert defines_function("isblank")
    assert not has_string("defgh"), "gebruik de variabelen uit de string-module voor deze opdracht"
    assert not has_string("DEFGH"), "gebruik de variabelen uit de string-module voor deze opdracht"
    assert not has_string("1234"), "gebruik de variabelen uit de string-module voor deze opdracht"
    assert has_string(".ascii_lowercase"), "gebruik de variabelen uit de string-module voor deze opdracht"
    assert has_string(".ascii_uppercase"), "gebruik de variabelen uit de string-module voor deze opdracht"
    assert has_string(".whitespace"), "gebruik de variabelen uit de string-module voor deze opdracht"

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
