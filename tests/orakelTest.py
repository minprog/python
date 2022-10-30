import _tests as tt
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

def orakelTest(test, value, target):
    def testMethod():
        output = test.runProgram(value)
        return asserts.exact(output.strip(), target)
    def expectedOutput():
        if test.language == "nl":
            return f"het antwoord '{value}' geeft de uitvoer '{target}'"
        else:
            return f"the answer '{value}' produces the output '{target}'"
    test.test = testMethod
    test.description = expectedOutput


def detect_language(keyword, test):
    source_no_comments = lib.removeComments(lib.source(test.fileName))
    if keyword in source_no_comments:
        test.language = "nl"
        test.description = lambda: f"{test.fileName} bestaat en het programma lijkt Nederlandstalig"
    else:
        test.language = "en"
        test.description = lambda: f"{test.fileName} exists and the program seems to be in English"
    test.test = lambda: True



@tt.test(0)
def assign_language(test):
    detect_language("veertig", test)

@tt.test(1)
def checks_answer0(test):
    if test.language == "nl":
        orakelTest(test, "42", "Ja")
    else:
        orakelTest(test, "42", "Yes")

@tt.test(2)
def checks_answer1(test):
    if test.language == "nl":
        orakelTest(test, "tweeenveertig", "Ja")
    else:
        orakelTest(test, "fortytwo", "Yes")

@tt.test(3)
def checks_answer2(test):
    if test.language == "nl":
        orakelTest(test, "tweeënveertig", "Ja")
    else:
        orakelTest(test, "forty two", "Yes")

@tt.test(4)
def checks_answer3(test):
    if test.language == "nl":
        orakelTest(test, "TWEEENVEERTIG", "Nee")
    else:
        orakelTest(test, "FORTYTWO", "No")

@tt.test(5)
def checks_answer4(test):
    if test.language == "nl":
        orakelTest(test, "53", "Nee")
    else:
        orakelTest(test, "53", "No")
