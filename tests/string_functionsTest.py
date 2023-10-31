from checkpy import *
from _basics_no_listcomp import *
from _static_analysis import *

import ast

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert "repeat" in static.getFunctionDefinitions(), "`repeat` is niet aanwezig"
    assert "total_length" in static.getFunctionDefinitions(), "`total_length` is niet aanwezig"
    
    assert ast.If not in static.AbstractSyntaxTree()
    assert ast.While not in static.AbstractSyntaxTree()
    assert ast.For not in static.AbstractSyntaxTree()

@t.passed(has_functions)
def test_repeat(test):
    """functie `repeat` werkt correct"""
    assert getFunction("repeat")('yes', 4) == 'yesyesyesyes'
    assert getFunction("repeat")('no', 0) == ''
    assert getFunction("repeat")('no', -2) == ''
    assert getFunction("repeat")('yesno', 3) == 'yesnoyesnoyesno'

@t.passed(has_functions)
def test_total_length(test):
    """functie `total_length` werkt correct"""
    assert getFunction("total_length")('yes', 'no') == 5
    assert getFunction("total_length")('', '') == 0
    assert getFunction("total_length")('', 'yes') == 3
