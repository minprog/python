import _tests as tt
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

def expectedOutput(target, args):
    if language == "nl":
        return f"Het antwoord '{args}' geeft de uitvoer {target[0]}." 
    else:
        return f"The answer '{args}' produces the output {target[1]}." 

@tt.test(0)
def assign_language(test):
    source_no_comments = lib.removeComments(lib.source(test.fileName))
    global language
    if "veertig" in source_no_comments:
        language = "nl"
    else:
        language = "en"
    test.test = lambda: True
    test.description = lambda: f"{test.fileName} exists and seems to be written in {language.upper()}"

@tt.test(1)
def checks_answer0(test):
    target = ["Ja", "Yes"]
    input_entries = "42"
    def testMethod():
        output = test.runProgram(input_entries)
        return any([asserts.exact(output.strip(), target) for target in target])
    test.test = testMethod
    test.description = lambda : expectedOutput(target, input_entries)

@tt.test(2)
def checks_answer1(test):
    target = ["Ja", "Yes"]
    input_entries = "tweeenveertig" if language == "nl" else "fortytwo"
    def testMethod():
        output = test.runProgram(input_entries)
        return any([asserts.exact(output.strip(), target) for target in target])
    test.test = testMethod
    test.description = lambda : expectedOutput(target, input_entries)

@tt.test(3)
def checks_answer2(test):
    target = ["Ja", "Yes"]
    input_entries = "tweeënveertig" if language == "nl" else "forty two"
    def testMethod():
        output = test.runProgram(input_entries)
        return any([asserts.exact(output.strip(), target) for target in target])
    test.test = testMethod
    test.description = lambda : expectedOutput(target, input_entries)

@tt.test(4)
def checks_answer3(test):
    target = ["Nee", "No"]
    input_entries = "TWEEENVEERTIG" if language == "nl" else "FORTYTWO"
    def testMethod():
        output = test.runProgram(input_entries)
        return any([asserts.exact(output.strip(), target) for target in target])
    test.test = testMethod
    test.description = lambda : expectedOutput(target, input_entries)

@tt.test(5)
def checks_answer4(test):
    target = ["Nee", "No"]
    input_entries = "53"
    def testMethod():
        output = test.runProgram(input_entries)
        return any([asserts.exact(output.strip(), target) for target in target])
    test.test = testMethod
    test.description = lambda : expectedOutput(target, input_entries)
