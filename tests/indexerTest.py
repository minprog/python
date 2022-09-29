import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

## CHECKS FROM CHECK50

# @check50.check(exists)
# def test_dinner():
#     """correctly identifies \"dinner\" in birdman.txt"""
#     check50.run("python3 indexer.py texts/birdman.txt").stdin("dinner").stdout("The word \"dinner\" can be found on lines: 549, 1542.\n", "The word \"dinner\" can be found on lines: 549, 1542.\n", timeout=5)
#
# @check50.check(test_dinner)
# def test_crash():
#     """handles nonexistent words gracefully (i.e. does not crash)"""
#     check50.run("python3 indexer.py texts/birdman.txt").stdin("women").stdout("Enter search term: ", "Enter search term:", timeout=5)

## EXAMPLE CHECKS FROM LEESBAARHEID

@t.test(1)
def checks_coleman_liau(test):
    def testMethod():
        coleman_liau = lib.getFunction("coleman_liau", test.fileName)
        if coleman_liau(537, 4.2) == 14.532399999999996:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "'coleman_liau' works correctly."

@t.test(2)
def checks_calculate_grade(test):
    def testMethod():
        calculate_grade = lib.getFunction("calculate_grade", test.fileName)
        if calculate_grade(119, 5, 639) == 15:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "'calculate_grade' works correctly."

@t.test(3)
def checks_tekst1(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since."],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Grade 7")

    test.test = testMethod
    test.description = lambda : "Determines the correct Grade 7 for a short sentence."


@t.test(4)
def checks_tekst2(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Grade 10")

    test.test = testMethod
    test.description = lambda : "Determines the correct Grade 10 for a long sentence."
