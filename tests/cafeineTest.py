import _tests as tt
import checkpy.lib as lib
import checkpy.assertlib as asserts

language = "en"

def expectedOutput(target, args):
    if language == "nl":
        return f"Print 'Je krijgt {target} cafeine binnen.' bij {str(args)} als invoer"
    else:
        return f"Prints 'Your intake is {target} of caffeine.' for {str(args)} as input"

def caffeineTest(test, values, target):
    def testMethod():
        output = test.runProgram(values)
        return asserts.contains(output.strip(), target)
    test.test = testMethod
    test.description = lambda: expectedOutput(target, values)

@tt.test(0)
def assign_language(test):
    source_no_comments = lib.removeComments(lib.source(test.fileName))
    global language
    if "binnen" in source_no_comments:
        language = "nl"
        test.description = lambda: f"{test.fileName} bestaat en het programma lijkt Nederlandstalig"
    else:
        language = "en"
        test.description = lambda: f"{test.fileName} exists and the program seems to be in English"
    test.test = lambda: True

@tt.test(1)
def calculatesZeroCaffeine(test):
    caffeineTest(test, [0, 0, 0, 0], "0 mg")

@tt.test(2)
def calculatesCoffee(test):
    caffeineTest(test, [1, 0, 0, 0], "90 mg")

@tt.test(2)
def calculatesTea(test):
    caffeineTest(test, [0, 1, 0, 0], "45 mg")

@tt.test(2)
def calculatesEnergy(test):
    caffeineTest(test, [0, 0, 1, 0], "80 mg")

@tt.test(2)
def calculatesCola(test):
    caffeineTest(test, [0, 0, 0, 1], "40 mg")

@tt.test(3)
def calculatesSomeCafeine(test):
    caffeineTest(test, [1, 2, 3, 4], "580 mg")
