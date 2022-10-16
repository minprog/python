import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

@t.test(0)
def check_example1(test):
    def testMethod():
        import lisp
        return lisp.LispValidator("(defun factorial (())(] (loop))))").is_valid() == False

    test.test = testMethod
    test.description = lambda: "the validator class works for a default example"

@t.test(1)
def check_empty(test):
    def testMethod():
        import lisp
        return lisp.LispValidator("").is_valid() == True

    test.test = testMethod
    test.description = lambda: "the validator class works for an empty lisp program"
