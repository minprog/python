import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

language = "en"

def expectedOutput(target, args):
    if language == "nl":
        return f"{args} is tijd voor {target[0]}." 
    else:
        return f"At {args} it is time for {target[1]}." 

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
def checks_convert(test):
    def testMethod():
        converted = lib.getFunction("convert", test.fileName)
        time = converted("11:15")
        if time == 11.15:
            return True
        else:
            return False, time

    test.test = testMethod
    test.description = lambda : (
        "De functie 'convert' werkt correct." 
        if language == "nl" else
        "The function 'convert' works correctly."
    )


@t.test(1)
def checks_breakfast(test):
    target = ["ontbijt", "breakfast"]
    args = "7:25"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return any([asserts.contains(output.strip(), target) for target in target])

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)


@t.test(2)
def checks_lunch(test):
    target = ["lunch", "lunch"]
    args = "13:00"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return any([asserts.contains(output.strip(), target) for target in target])

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)


@t.test(3)
def checks_dinner(test):
    target = ["avondeten", "dinner"]
    args = "18:01"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return any([asserts.contains(output.strip(), target) for target in target])

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)


@t.test(4)
def checks_nomeal(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["19:01"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "")

    test.test = testMethod
    test.description = lambda : (
        "19:01 is niet een tijdstip voor een maaltijd."
        if language == "nl" else
        "19:01 is not a proper moment for a meal."
    )
