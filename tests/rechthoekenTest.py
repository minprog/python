import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def check_is_same_rectangle_1234(test):
    def testMethod():
        is_same_rectangle = lib.getFunction("is_same_rectangle", test.fileName)
        return not is_same_rectangle(1,2,3,4) and is_same_rectangle(1,2,1,2)

    test.test = testMethod
    test.description = lambda : "De functie 'is_same_rectangle' werkt correct."


@t.test(1)
def check_is_square(test):
    def testMethod():
        is_square = lib.getFunction("is_square", test.fileName)
        return not is_square(1,2,1,2) and not is_square(1,1,2,2) and is_square(1,1,1,1) and is_square(2,2,2,2)

    test.test = testMethod
    test.description = lambda : "De functie 'is_square' werkt correct."


@t.test(2)
def check_calculate_length(test):
    def testMethod():
        calculate_length = lib.getFunction("calculate_length", test.fileName)
        return calculate_length(-2,2)==4 and calculate_length(2,-2)==4 and calculate_length(0,4)==4 and calculate_length(4,0)==4 and calculate_length(3,9)==6

    test.test = testMethod
    test.description = lambda : "De functie 'calculate_length' werkt correct."

@t.test(3)
def check_identical_rectangle(test):
    args = ["0,7", "0,4", "6,13", "2,6"]
    target_1 = ['zijn gelijk!', 'are identical!']
    target_2 = ['vierkant!', ' square,']
    target_3 = ['niks aan', 'to report']
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args,
                    overwriteAttributes = [("__name__", "__main__")])
        return any([asserts.contains(output.strip(), target) for target in target_1]) and not any([asserts.contains(output.strip(), target) for target in target_3])

    test.test = testMethod
    test.description = lambda : ("Het programma identificeert gelijke rechthoeken.")

@t.test(4)
def check_identical_square(test):
    args = ["0,7", "0,7", "6,13", "2,9"]
    target_1 = ['zijn gelijk!', 'are identical!']
    target_2 = ['vierkant!', ' square,']
    target_3 = ['niks aan', 'to report']
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args,
                    overwriteAttributes = [("__name__", "__main__")])
        return any([asserts.contains(output.strip(), target) for target in target_1]) and any([asserts.contains(output.strip(), target) for target in target_2])

    test.test = testMethod
    test.description = lambda : ("Het programma identificeert gelijke vierkanten.")

@t.test(5)
def check_no_result(test):
    args = ["0,7", "0,7", "6,15", "2,9"]
    target_1 = ['zijn gelijk!', 'are identical!']
    target_2 = ['vierkant!', ' square,']
    target_3 = ['niks aan', 'to report']
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args,
                    overwriteAttributes = [("__name__", "__main__")])
        return any([asserts.contains(output.strip(), target) for target in target_3]) and not any([asserts.contains(output.strip(), target) for target in target_1]) and not any([asserts.contains(output.strip(), target) for target in target_2])

    test.test = testMethod
    test.description = lambda : ("Het programma rapporteert teleurstelling bij gebrek aan gelijkheid.")
