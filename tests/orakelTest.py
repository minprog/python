import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

language = "en"

def expectedOutput(target, args):
    if language == "nl":
        return f"Het antwoord '{args}' leidt tot de output {target[0]}." 
    else:
        return f"The answer '{args}' produces the output {target[1]}." 

@t.test(0)
def validFile(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[""],
                    overwriteAttributes = [("__name__", "__main__")])
        if "Nee" in output:
            global language
            language = "nl"
        elif not "No" in output:
            return False, f"Output not recognized; please double check examples on the assignment page."
        return asserts.fileExists(test.fileName)

    test.test = testMethod
    test.description = lambda : (
        "Het bestand is in orde."
        if language == "nl" else
        "The file is valid."
    )

@t.test(0)
def checks_answer0(test):
    target = ["Ja", "Yes"]
    args = "42"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return any([asserts.exact(output.strip(), target) for target in target])

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

@t.test(1)
def checks_answer1(test):
    target = ["Ja", "Yes"]
    args = "tweeenveertig" if language == "nl" else "fortytwo"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return any([asserts.exact(output.strip(), target) for target in target])

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

@t.test(2)
def checks_answer2(test):
    target = ["Ja", "Yes"]
    args = "tweeen veertig" if language == "nl" else "forty two"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return any([asserts.exact(output.strip(), target) for target in target])

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

@t.test(3)
def checks_answer3(test):
    target = ["Nee", "No"]
    args = "TWEEENVEERTIG" if language == "nl" else "FORTYTWO"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return any([asserts.exact(output.strip(), target) for target in target])

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

@t.test(4)
def checks_answer4(test):
    target = ["Nee", "No"]
    args = "53"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return any([asserts.exact(output.strip(), target) for target in target])

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)
