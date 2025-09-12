import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _basics_no_listcomp import *

# TODO modernize

@t.passed(doctest_ok)
@t.test(10)
def check_is_same_rectangle(test):
    """functie 'is_same_rectangle' werkt correct"""
    def testCase():
        is_same_rectangle = lib.getFunction("is_same_rectangle")
        result = (not is_same_rectangle(1,2,3,4) and
                    is_same_rectangle(1,2,1,2))
        if result:
          return result
        else:
          return result, "let op dat we hier de werking van functie testen en niet van het programma als geheel"
    test.test = testCase

@t.passed(doctest_ok)
@t.test(20)
def check_is_same_square(test):
    """functie 'is_same_square' werkt correct"""
    def testCase():
        is_same_square = lib.getFunction("is_same_square")
        result = (not is_same_square(1,2,1,2) and
                  not is_same_square(1,1,2,2) and
                      is_same_square(1,1,1,1) and
                      is_same_square(2,2,2,2))
        if result:
          return result
        else:
          return result, "let op dat we hier de werking van functie testen en niet van het programma als geheel"
    test.test = testCase

@t.passed(doctest_ok)
@t.test(30)
def check_calculate_length(test):
    """functie 'calculate_length' werkt correct"""
    def testCase():
        calculate_length = lib.getFunction("calculate_length")
        result = (calculate_length(-2,  2) == 4 and
                  calculate_length( 2, -2) == 4 and
                  calculate_length( 0,  4) == 4 and
                  calculate_length( 4,  0) == 4 and
                  calculate_length( 3,  9) == 6)
        if result:
          return result
        else:
          return result, "let op dat we hier de werking van functie testen en niet van het programma als geheel"
    test.test = testCase

@t.passed(doctest_ok)
@t.test(40)
def check_identical_rectangle(test):
    """het programma identificeert gelijke rechthoeken"""
    def testCase():
        input_entries = ["0", "7", "0", "4", "6", "13", "2", "6"]
        target_1 = ['zijn gelijk!', 'are identical!']
        target_2 = ['vierkant!', ' square,']
        target_3 = ['niks aan', 'to report']
        output = lib.outputOf(_fileName, stdinArgs=input_entries, overwriteAttributes = [("__name__", "__main__")])
        return (    any([asserts.contains(output.strip(), target) for target in target_1]) and
                not any([asserts.contains(output.strip(), target) for target in target_3]))
    test.test = testCase

@t.passed(doctest_ok)
@t.test(50)
def check_identical_square(test):
    """het programma identificeert gelijke vierkanten"""
    def testCase():
        input_entries = ["0", "7", "0", "7", "6", "13", "2", "9"]
        target_1 = ['zijn gelijk!', 'are identical!']
        target_2 = ['vierkant!', ' square,']
        target_3 = ['niks aan', 'to report']
        output = lib.outputOf(_fileName, stdinArgs=input_entries, overwriteAttributes = [("__name__", "__main__")])
        return (any([asserts.contains(output.strip(), target) for target in target_1]) and
                any([asserts.contains(output.strip(), target) for target in target_2]))
    test.test = testCase

@t.passed(doctest_ok)
@t.test(60)
def check_no_result(test):
    """het programma rapporteert teleurstelling bij gebrek aan gelijkheid"""
    def testCase():
        input_entries = ["0", "7", "0", "7", "6", "15", "2", "9"]
        target_1 = ['zijn gelijk!', 'are identical!']
        target_2 = ['vierkant!', ' square,']
        target_3 = ['niks aan', 'to report']
        output = lib.outputOf(_fileName, stdinArgs=input_entries, overwriteAttributes = [("__name__", "__main__")])
        return (    any([asserts.contains(output.strip(), target) for target in target_3]) and
                not any([asserts.contains(output.strip(), target) for target in target_1]) and
                not any([asserts.contains(output.strip(), target) for target in target_2]))
    test.test = testCase
