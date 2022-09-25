import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

language = "en"

def expectedOutput(target, args):
    if language == "nl":
        return f"Bepaalt correct de tijd voor {target[0]}." 
    else:
        return f"Correctly determines the time for {target[1]}." 

@t.test(0)
def validFile(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["7:01"],
                    overwriteAttributes = [("__name__", "__main__")])
        if "ontbijt" in output:
            global language
            language = "nl"
        elif not "breakfast" in output:
            return False, "Output not recognized; please double check examples on the assignment page."
        return asserts.fileExists(test.fileName)

    test.test = testMethod
    test.description = lambda : (
        "Het bestand is in orde."
        if language == "nl" else
        "The file is valid."
    )

@t.test(1)
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


@t.test(2)
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


@t.test(3)
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
