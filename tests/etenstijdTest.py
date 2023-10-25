import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

@t.passed(doctest_ok)
@t.test(8)
def correct_meal_if_meal(test):
    """functie 'meal' geeft de juiste maaltijd voor elke tijd"""
    def testMethod():
        f = lib.getFunction("meal", test.fileName)
        return (
            f('7:30') == 'ontbijt' and
            f('7:31') == 'ontbijt' and
            f('07:31') == 'ontbijt' and
            f('18:30') == 'avondeten' and
            f('13:00') == 'lunch' and
            f('12:00') == 'lunch'
        )
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(9)
def correct_none_if_no_meal(test):
    """functie 'meal' geeft None als er geen maaltijd van toepassing is"""
    def testMethod():
        f = lib.getFunction("meal", test.fileName)
        return (
            f('6:30') is None and
            f('8:01') is None and
            f('08:31') is None and
            f('14:01') is None and
            f('13:01') is None and
            f('17:59') is None
        )
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(10)
def checks_breakfast(test):
    """bepaalt correct de tijd voor ontbijt"""
    correct_meal_descriptions = ["ontbijt", "breakfast"]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["7:25"], overwriteAttributes = [("__name__", "__main__")])
        if not any([asserts.contains(output, meal) for meal in correct_meal_descriptions]):
            return False

        output = lib.outputOf(test.fileName, stdinArgs=["8:00"], overwriteAttributes = [("__name__", "__main__")])
        if not any([asserts.contains(output, meal) for meal in correct_meal_descriptions]):
            return False

        output = lib.outputOf(test.fileName, stdinArgs=["8:01"], overwriteAttributes = [("__name__", "__main__")])
        if any([asserts.contains(output, meal) for meal in correct_meal_descriptions]):
            return False

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def checks_lunch(test):
    """bepaalt correct de tijd voor lunch"""
    correct_meal_descriptions = ["lunch"]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["13:00"], overwriteAttributes = [("__name__", "__main__")])
        if not any([asserts.contains(output, meal) for meal in correct_meal_descriptions]):
            return False

        output = lib.outputOf(test.fileName, stdinArgs=["12:00"], overwriteAttributes = [("__name__", "__main__")])
        if not any([asserts.contains(output, meal) for meal in correct_meal_descriptions]):
            return False

        output = lib.outputOf(test.fileName, stdinArgs=["13:40"], overwriteAttributes = [("__name__", "__main__")])
        if any([asserts.contains(output, meal) for meal in correct_meal_descriptions]):
            return False

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(30)
def checks_dinner(test):
    """bepaalt correct de tijd voor avondeten"""
    correct_meal_descriptions = ["avondeten", "dinner"]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["18:53"], overwriteAttributes = [("__name__", "__main__")])
        if not any([asserts.contains(output, meal) for meal in correct_meal_descriptions]):
            return False

        output = lib.outputOf(test.fileName, stdinArgs=["18:00"], overwriteAttributes = [("__name__", "__main__")])
        if not any([asserts.contains(output, meal) for meal in correct_meal_descriptions]):
            return False

        output = lib.outputOf(test.fileName, stdinArgs=["19:00"], overwriteAttributes = [("__name__", "__main__")])
        if not any([asserts.contains(output, meal) for meal in correct_meal_descriptions]):
            return False

        output = lib.outputOf(test.fileName, stdinArgs=["19:59"], overwriteAttributes = [("__name__", "__main__")])
        if any([asserts.contains(output, meal) for meal in correct_meal_descriptions]):
            return False

        return True
    test.test = testMethod
