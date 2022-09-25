import _tests as tt
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

@tt.test(10)
def check_is_same_rectangle(test):
    def testCase():
        is_same_rectangle = test.getFunction("is_same_rectangle")
        return (not is_same_rectangle(1,2,3,4) and
                    is_same_rectangle(1,2,1,2))
    test.test = testCase
    test.description = lambda : "De functie 'is_same_rectangle' werkt correct"

@tt.test(20)
def check_is_same_square(test):
    def testCase():
        is_same_square = test.getFunction("is_same_square")
        return (not is_same_square(1,2,1,2) and
                not is_same_square(1,1,2,2) and
                    is_same_square(1,1,1,1) and
                    is_same_square(2,2,2,2))
    test.test = testCase
    test.description = lambda : "De functie 'is_same_square' werkt correct"

@tt.test(30)
def check_calculate_length(test):
    def testCase():
        calculate_length = test.getFunction("calculate_length")
        return (calculate_length(-2,  2) == 4 and
                calculate_length( 2, -2) == 4 and
                calculate_length( 0,  4) == 4 and
                calculate_length( 4,  0) == 4 and
                calculate_length( 3,  9) == 6)
    test.test = testCase
    test.description = lambda : "De functie 'calculate_length' werkt correct"

@tt.test(40)
def check_identical_rectangle(test):
    def testCase():
        input_entries = ["0,7", "0,4", "6,13", "2,6"]
        target_1 = ['zijn gelijk!', 'are identical!']
        target_2 = ['vierkant!', ' square,']
        target_3 = ['niks aan', 'to report']
        output = test.runProgram(input_entries)
        return (    any([asserts.contains(output.strip(), target) for target in target_1]) and
                not any([asserts.contains(output.strip(), target) for target in target_3]))
    test.test = testCase
    test.description = lambda : ("Het programma identificeert gelijke rechthoeken")

@tt.test(50)
def check_identical_square(test):
    def testCase():
        input_entries = ["0,7", "0,7", "6,13", "2,9"]
        target_1 = ['zijn gelijk!', 'are identical!']
        target_2 = ['vierkant!', ' square,']
        target_3 = ['niks aan', 'to report']
        output = test.runProgram(input_entries)
        return (any([asserts.contains(output.strip(), target) for target in target_1]) and
                any([asserts.contains(output.strip(), target) for target in target_2]))
    test.test = testCase
    test.description = lambda : ("Het programma identificeert gelijke vierkanten")

@tt.test(60)
def check_no_result(test):
    def testCase():
        input_entries = ["0,7", "0,7", "6,15", "2,9"]
        target_1 = ['zijn gelijk!', 'are identical!']
        target_2 = ['vierkant!', ' square,']
        target_3 = ['niks aan', 'to report']
        output = test.runProgram(input_entries)
        return (    any([asserts.contains(output.strip(), target) for target in target_3]) and
                not any([asserts.contains(output.strip(), target) for target in target_1]) and
                not any([asserts.contains(output.strip(), target) for target in target_2]))
    test.test = testCase
    test.description = lambda : ("Het programma rapporteert teleurstelling bij gebrek aan gelijkheid")
