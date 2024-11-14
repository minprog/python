import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

from _basics_no_listcomp import *

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    # assert in_code(ast.While)
    assert not_in_code(ast.For)
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_in_code(ast.In)

@t.passed(has_functions)
@t.test(10)
def exactChange0(test):
    """0$ aan wisselgeld staat gelijk aan 0 munten"""
    test.test = lambda : assertlib.numberOnLine(0, lib.getLine(lib.outputOf(_fileName, stdinArgs=[0], overwriteAttributes = [("__name__", "__main__")]), 0))

@t.passed(has_functions)
@t.test(20)
def exactChange41(test):
    """0.41$ aan wisselgeld staat gelijk aan 4 munten"""
    test.test = lambda : assertlib.numberOnLine(4, lib.getLine(lib.outputOf(_fileName, stdinArgs=[0.41], overwriteAttributes = [("__name__", "__main__")]), 0))

@t.passed(has_functions)
@t.test(30)
def exactChange9999(test):
    """9999$ aan wisselgeld staat gelijk aan 39996 munten"""
    test.test = lambda : assertlib.numberOnLine(39996, lib.getLine(lib.outputOf(_fileName, stdinArgs=[9999], overwriteAttributes = [("__name__", "__main__")]), 0))

@t.passed(has_functions)
@t.test(40)
def exactChange402(test):
    """4.02$ aan wisselgeld staat gelijk aan 18 munten"""
    test.test = lambda : assertlib.numberOnLine(18, lib.getLine(lib.outputOf(_fileName, stdinArgs=[4.02], overwriteAttributes = [("__name__", "__main__")]), 0))

@t.passed(has_functions)
@t.test(50)
def exactChange35(test):
    """0.35$ aan wisselgeld staat gelijk aan 2 munten"""
    test.test = lambda : assertlib.numberOnLine(2, lib.getLine(lib.outputOf(_fileName, stdinArgs=[0.35], overwriteAttributes = [("__name__", "__main__")]), 0))

@t.passed(has_functions)
@t.test(60)
def handlesWrongInput(test):
    """accepteert geen negatieve invoer"""
    test.test = lambda : assertlib.numberOnLine(4, lib.getLine(lib.outputOf(_fileName, stdinArgs=[-1, -1, 0.41], overwriteAttributes = [("__name__", "__main__")]), 0))
