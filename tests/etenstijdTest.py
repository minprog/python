import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

def expectedOutput(target, args):
    return f"bepaalt correct de tijd voor {target[0]}" 

@t.test(10)
def checks_breakfast(test):
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
    test.description = lambda : expectedOutput(correct_meal_descriptions, None)


@t.test(20)
def checks_lunch(test):
    correct_meal_descriptions = ["lunch", "lunch"]
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
    test.description = lambda : expectedOutput(correct_meal_descriptions, None)


@t.test(30)
def checks_dinner(test):
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
    test.description = lambda : expectedOutput(correct_meal_descriptions, None)
