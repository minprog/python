from checkpy import *
from _basics_no_listcomp import *

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert "pie_percent" in static.getFunctionDefinitions()
    assert "triple" in static.getFunctionDefinitions()
    assert "absdiff" in static.getFunctionDefinitions()
    assert "kmmiles" in static.getFunctionDefinitions()
    assert "avg3" in static.getFunctionDefinitions()
    assert "avg3of4" in static.getFunctionDefinitions()

@t.passed(has_functions)
def test_pie_percent(test):
    """functie `pie_percent` werkt correct"""
    assert getFunction("pie_percent")(20) == 5
    assert getFunction("pie_percent")(5) == 20
    assert getFunction("pie_percent")(18) == 5

@t.passed(has_functions)
def test_triple(test):
    """functie `triple` werkt correct"""
    assert getFunction("triple")(3) == 9
    assert getFunction("triple")(1) == 3
    assert getFunction("triple")(0) == 0
    assert getFunction("triple")(-4) == -12

@t.passed(has_functions)
def test_absdiff(test):
    """functie `absdiff` werkt correct"""
    assert getFunction("absdiff")(3,-4) == 7
    assert getFunction("absdiff")(3,4) == 1
    assert getFunction("absdiff")(4,3) == 1
    assert getFunction("absdiff")(-4,3) == 7
    assert getFunction("absdiff")(0,0) == 0
    assert getFunction("absdiff")(-1,0) == 1

@t.passed(has_functions)
def test_kmmiles(test):
    """functie `kmmiles` werkt correct"""
    assert getFunction("kmmiles")(100) == 62.5
    assert getFunction("kmmiles")(20) == 12.5
    assert getFunction("kmmiles")(21) == 13.125
    assert getFunction("kmmiles")(22) == 13.75
    assert getFunction("kmmiles")(0) == 0

@t.passed(has_functions)
def test_avg3(test):
    """functie `avg3` werkt correct"""
    assert getFunction("avg3")(0,1,2) == 1.0
    assert getFunction("avg3")(4,5,6) == 5.0
    assert getFunction("avg3")(20,100,50) == approx(56.66666)
    assert getFunction("avg3")(0,0,0) == 0.0

@t.passed(has_functions)
def test_avg3of4(test):
    """functie `avg3of4` werkt correct"""
    assert getFunction("avg3of4")(0,1,2,0) == 1.0
    assert getFunction("avg3of4")(4,5,6,7) == 6.0
    assert getFunction("avg3of4")(20,100,50,0) == approx(56.66666)
    assert getFunction("avg3of4")(0,0,0,0) == 0.0
