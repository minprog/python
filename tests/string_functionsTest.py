from checkpy import *
from _basics_no_listcomp import *
from _static_analysis import *

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert "repeat" in static.getFunctionDefinitions(), "`repeat` is niet aanwezig"
    assert "total_length" in static.getFunctionDefinitions(), "`total_length` is niet aanwezig"
    assert not (has_string("if(") or has_string("if ")), "let op dat je geen `if` gebruikt"
    assert not (has_string("for ") or has_string("while ")), "let op dat je geen `for` of `while` gebruikt"

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
