import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _basics_no_listcomp import *

@t.passed(doctest_ok)
@t.test(10)
def checks_coleman_liau(test):
    """functie `coleman_liau` werkt correct"""
    def testMethod():
        coleman_liau = lib.getFunction("coleman_liau", test.fileName)
        if coleman_liau(537, 4.2) == 14.532399999999996:
            return True
        else:
            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def checks_calculate_grade(test):
    """functie `calculate_grade` werkt correct"""
    def testMethod():
        calculate_grade = lib.getFunction("calculate_grade", test.fileName)
        if calculate_grade(119, 5, 639) == 15:
            return True
        else:
            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(30)
def checks_tekst1(test):
    """geeft Grade 7 voor een bepaalde korte zin"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since."],
            overwriteAttributes = [("__name__", "__main__")])
        if asserts.exact(output.strip(), "Grade 7"):
            return True
        else:
            return False, "zorg dat je niet te vaak afrondt"
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(40)
def checks_tekst2(test):
    """geeft Grade 10 voor een bepaalde lange zin"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Grade 10")
    test.test = testMethod
