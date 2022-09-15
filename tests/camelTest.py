import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def checks_convert0(test):
    def testMethod():
        convert = lib.getFunction("convert", test.fileName)
        if convert("check") == "check":
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "'check' blijft onveranderd."

@t.test(1)
def checks_convert1(test):
    def testMethod():
        convert = lib.getFunction("convert", test.fileName)
        if convert("convertInput") == "convert_input":
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "'convertInput' wordt succesvol geconverteerd naar 'convert_input'."

@t.test(2)
def checks_convert2(test):
    def testMethod():
        convert = lib.getFunction("convert", test.fileName)
        if convert("readFromFile") == "read_from_file":
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "'readFromFile' wordt succesvol geconverteerd naar 'read_from_file'."
