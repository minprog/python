from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `travel_costs` is aanwezig"""
    assert function_defined_in_module("travel_costs")

@passed(has_functions)
@test(10)
def calculatesTravelCostsWithHint(test):
    """functie `travel_costs` berekent correct de vervoerkosten"""
    result = getFunction("travel_costs")(1000)
    if result == 130:
        raise AssertionError("vergeet niet om de kosten voor zowel heen als terug te berekenen")
    elif result == 260:
        return True
    else:
        raise AssertionError

@passed(has_functions)
@test(20)
def calculatesZeroCosts(test):
    """run: print correct 'Jouw vakantie kost: 0' bij [0, 0] als invoer"""
    assert run(0, 0).number() == '0'

@passed(has_functions)
@test(20)
def calculatesTravelCosts(test):
    """run: print correct 'Jouw vakantie kost: 260' bij [1000, 0] als invoer"""
    assert run(1000, 0).number() == '260'

@passed(has_functions)
@test(30)
def calculatesSleepingCosts(test):
    """run: print correct 'Jouw vakantie kost: 600' bij [0, 10] als invoer"""
    assert run(0, 10).number() == '600'

@passed(has_functions)
@test(40)
def calculatesCosts(test):
    """run: print correct 'Jouw vakantie kost: 589' bij [650, 7] als invoer"""
    assert run(650, 7).number() == '589'

@passed(has_functions)
@test(50)
def calculatesCostsAndRoundsCorrectly(test):
    """run: print correct 'Jouw vakantie kost: 371' bij [1425, 0] als invoer"""
    assert run(1425, 0).number() == '371'
