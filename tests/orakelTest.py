import _tests as tt
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

def expectedOutput(target, args):
    if language == "nl":
        return f"Het antwoord '{args}' geeft de uitvoer {target}"
    else:
        return f"The answer '{args}' produces the output {target}"

def orakelTest(test, value, target):
    def testMethod():
        output = test.runProgram(value)
        return asserts.exact(output.strip(), target)
    test.test = testMethod
    test.description = lambda : expectedOutput(target, value)

@tt.test(0)
def assign_language(test):
    source_no_comments = lib.removeComments(lib.source(test.fileName))
    global language
    if "veertig" in source_no_comments:
        language = "nl"
        test.description = lambda: f"{test.fileName} bestaat en het programma lijkt Nederlandstalig"
    else:
        language = "en"
        test.description = lambda: f"{test.fileName} exists and the program seems to be in English"
    test.test = lambda: True

@tt.test(1)
def checks_answer0(test):
    if language == "nl":
        orakelTest(test, "42", "Ja")
    else:
        orakelTest(test, "42", "Yes")

@tt.test(2)
def checks_answer1(test):
    if language == "nl":
        orakelTest(test, "tweeenveertig", "Ja")
    else:
        orakelTest(test, "fortytwo", "Yes")

@tt.test(3)
def checks_answer2(test):
    if language == "nl":
        orakelTest(test, "tweeënveertig", "Ja")
    else:
        orakelTest(test, "forty two", "Yes")

@tt.test(4)
def checks_answer3(test):
    if language == "nl":
        orakelTest(test, "TWEEENVEERTIG", "Nee")
    else:
        orakelTest(test, "FORTYTWO", "No")

@tt.test(5)
def checks_answer4(test):
    if language == "nl":
        orakelTest(test, "53", "Nee")
    else:
        orakelTest(test, "53", "No")
