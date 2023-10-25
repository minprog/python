import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

@t.passed(doctest_ok)
@t.test(10)
def calculatesTravelCostsWithHint(test):
    """functie 'travel_costs' berekent correct de vervoerkosten"""
    def testMethod():
        travelCosts = lib.getFunction("travel_costs", test.fileName, stdinArgs=[1000, 0])(1000)
        if travelCosts == 130:
            return (False, 
                    "vergeet niet om de kosten voor zowel heen als terug te berekenen"
            )
        elif travelCosts == 260:
            return True
        else:
            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def calculatesZeroCosts(test):
    """print correct 'Jouw vakantie kost: 0' bij [0, 0] als invoer"""
    target = "0"
    args = [0, 0]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args, overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def calculatesTravelCosts(test):
    """print correct 'Jouw vakantie kost: 260' bij [1000, 0] als invoer"""
    target = "260"
    args = [1000, 0]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args, overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(30)
def calculatesSleepingCosts(test):
    """print correct 'Jouw vakantie kost: 600' bij [0, 10] als invoer"""
    target = "600"
    args = [0, 10]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args, overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(40)
def calculatesCosts(test):
    """print correct 'Jouw vakantie kost: 589' bij [650, 7] als invoer"""
    target = "589"
    args = [650, 7]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args, overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(50)
def calculatesCostsAndRoundsCorrectly(test):
    """print correct 'Jouw vakantie kost: 371' bij [1425, 0] als invoer"""
    target = "371"
    args = [1425, 0]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args, overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)
    test.test = testMethod
