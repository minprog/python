from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `calculate_cafeine` is aanwezig"""
    assert function_defined_in_module("calculate_cafeine")

# TODO overweeg "\d+ mg"-patroon te kunnen zoeken ipv alleen number()

@passed(has_functions)
@test(10)
def calculatesZeroCaffeine(test):
    """print 'Je krijgt 0 mg cafeine binnen.' bij [0, 0, 0, 0] als invoer"""
    assert run(0, 0, 0, 0).number() == "0"

@passed(has_functions)
@test(20)
def calculatesCoffee(test):
    """print 'Je krijgt 90 mg cafeine binnen.' bij [1, 0, 0, 0] als invoer"""
    assert run(1, 0, 0, 0).number() == "90"

@passed(has_functions)
@test(20)
def calculatesTea(test):
    """print 'Je krijgt 45 mg cafeine binnen.' bij [0, 1, 0, 0] als invoer"""
    assert run(0, 1, 0, 0).number() == "45"

@passed(has_functions)
@test(20)
def calculatesEnergy(test):
    """print 'Je krijgt 80 mg cafeine binnen.' bij [0, 0, 1, 0] als invoer"""
    assert run(0, 0, 1, 0).number() == "80"

@passed(has_functions)
@test(20)
def calculatesCola(test):
    """print 'Je krijgt 40 mg cafeine binnen.' bij [0, 0, 0, 1] als invoer"""
    assert run(0, 0, 0, 1).number() == "40"

@passed(has_functions)
@test(30)
def calculatesSomeCafeine(test):
    """print 'Je krijgt 580 mg cafeine binnen.' bij [1, 2, 3, 4] als invoer"""
    assert run(1, 2, 3, 4).number() == "580"
