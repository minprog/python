from checkpy import *
from _basics import *
from _static_analysis import *

import ast

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert defines_function("least_prob")
    assert defines_function("count_duplicates")
    assert defines_function("is_balanced")
    assert defines_function("dict_intersect")

@t.passed(has_functions)
def test_least_prob(test):
    """functie `least_prob` werkt correct"""
    assert getFunction("least_prob")({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14}) == 'meson'
    assert getFunction("least_prob")({'neutron': 0.55}) == 'neutron'

@t.passed(has_functions)
def test_count_duplicates(test):
    """functie `count_duplicates` werkt correct"""
    assert getFunction("count_duplicates")({'raar': 'bn', 'tafel': 'zn', 'woord': 'zn', 'ruimte': 'zn', 'erg': 'bw', 'aardig': 'bn'}) == 2
    assert getFunction("count_duplicates")({}) == 0

@t.passed(has_functions)
def test_is_balanced(test):
    """functie `is_balanced` werkt correct"""
    assert getFunction("is_balanced")({'R': 0.2, 'G': 0.4, 'B': 0.4}) == True
    assert getFunction("is_balanced")({'R': 0.0, 'G': 0.6, 'B': 0.1}) == False

@t.passed(has_functions)
def test_dict_intersect(test):
    """functie `dict_intersect` werkt correct"""
    assert getFunction("dict_intersect")({'on': 'zin', 'waar': 'heid'}, {}) == {}
    assert getFunction("dict_intersect")({'on': 'zin', 'waar': 'heid'}, {'on': 'zin'}) == {'on': 'zin'}
    assert getFunction("dict_intersect")({'on': 'zin', 'waar': 'heid'}, {'roos': 'kleurig'}) == {}
