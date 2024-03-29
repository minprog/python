import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _basics import *

@t.test(0)
def check_no_output(test):
    def testMethod():
        return lib.outputOf(test.fileName) == ''

    test.test = testMethod
    test.description = lambda: "the code should not run automatically when imported"

@t.passed(check_no_output)
@t.test(1)
def check_example1(test):
    def testMethod():
        import lisp
        return lisp.LispValidator("(defun factorial (())(] (loop))))").is_valid() == False

    test.test = testMethod
    test.description = lambda: "the validator class works for a default example"

@t.passed(check_no_output)
@t.test(2)
def check_empty(test):
    def testMethod():
        import lisp
        return lisp.LispValidator("").is_valid() == True

    test.test = testMethod
    test.description = lambda: "the validator class works for an empty lisp program"
