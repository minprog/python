import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

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
    target = ["ontbijt", "breakfast"]
    args = ["7:25", "8:00"]
    def testMethod():
        outputs = [lib.outputOf(test.fileName, stdinArgs=[arg],
                    overwriteAttributes = [("__name__", "__main__")]) for arg in args]
        return all([any([asserts.contains(output.strip(), target) for target in target]) for output in outputs])

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)


@t.test(2)
def checks_lunch(test):
    target = ["lunch", "lunch"]
    args = ["13:00", "12:00"]
    def testMethod():
        outputs = [lib.outputOf(test.fileName, stdinArgs=[arg],
                    overwriteAttributes = [("__name__", "__main__")]) for arg in args]
        return all([any([asserts.contains(output.strip(), target) for target in target]) for output in outputs])

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)


@t.test(3)
def checks_dinner(test):
    target = ["avondeten", "dinner"]
    args = ["18:53", "18:00", "19:00"]
    def testMethod():
        outputs = [lib.outputOf(test.fileName, stdinArgs=[arg],
                    overwriteAttributes = [("__name__", "__main__")]) for arg in args]
        return all([any([asserts.contains(output.strip(), target) for target in target]) for output in outputs])

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)


@t.test(4)
def checks_nomeal(test):
    target = [""]
    args = ["8:01", "11:59", "22:12"]
    def testMethod():
        outputs = [lib.outputOf(test.fileName, stdinArgs=[arg],
                    overwriteAttributes = [("__name__", "__main__")]) for arg in args]
        return all([any([asserts.contains(output.strip(), target) for target in target]) for output in outputs])

    test.test = testMethod
    test.description = lambda : (
        "Herkent wanneer het niet een tijdstip voor een maaltijd is."
        if language == "nl" else
        "Knows when it is not a proper moment for a meal."
    )
