import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

def expectedOutput(target, args):
    return f"print correct 'Jouw vakantie kost: {target}' bij {str(args)} als invoer" 

@t.test(10)
def calculatesZeroCosts(test):
    target = "0"
    args = [0, 0]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args, overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda: expectedOutput(target, args)

@t.test(20)
def calculatesTravelCostsWithHint(test):
  def testMethod():
    travelCosts = lib.getFunction("travel_costs", test.fileName, stdinArgs=[1000, 0])(1000)
    if travelCosts == 130:
        return (False, 
                "vergeet niet om de kosten voor zowel heen als terug te berekenen"
                # if language == "nl" else
                # "Don't forget to calculate costs for a round trip."
            )
    elif travelCosts == 260:
        return True
    else:
        return False

  test.test = testMethod
  test.description = lambda : (
    "de functie 'travel_costs' berekent correct de vervoerkosten"
    # if language == "nl" else
    # "The function 'travel_costs' calculates the costs of travel correctly."
  )

@t.test(20)
def calculatesTravelCosts(test):
    target = "260"
    args = [1000, 0]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args, overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda: expectedOutput(target, args)

@t.test(30)
def calculatesSleepingCosts(test):
    target = "600"
    args = [0, 10]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args, overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda: expectedOutput(target, args)

@t.test(40)
def calculatesCosts(test):
    target = "589"
    args = [650, 7]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args, overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda: expectedOutput(target, args)

@t.test(50)
def calculatesCostsAndRoundsCorrectly(test):
    target = "371"
    args = [1425, 0]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args, overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda: expectedOutput(target, args)
