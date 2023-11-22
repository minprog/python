from checkpy import *
from _basics import *
from _static_analysis import *

import ast

@t.passed(doctest_ok)
def test_country(test):
    """class `Country` werkt correct"""
    canada = getModule().Country('Canada', 34482779, 9984670)
    assert canada.name == 'Canada'
    assert canada.population == 34482779
    assert canada.area == 9984670
    usa = getModule().Country('United States of America', 313914040, 9826675)
    assert canada.is_larger(usa)
    assert canada.population_density() == 3.4535722262227995
    usa = getModule().Country('United States of America', 313914040, 9826675)
    assert usa.__str__() == 'United States of America has a population of 313914040 and is 9826675 square km.'
    if has_call('isinstance'):
        raise AssertionError("let op dat je geen isinstance() gebruikt")
