import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import re

from _basics_no_listcomp import *

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert in_code(ast.While)
    assert in_code(ast.For)
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_in_code(ast.Try)
    assert not_has_stringmult()

@t.passed(has_functions)
@t.test(10)
def exactMario0(test):
    """print een welgevormde pyramide van 1 hoog"""
    r = re.compile(".*(# #)[ ]*(\n)")
    o = lib.outputOf(_fileName, stdinArgs=[1], overwriteAttributes = [("__name__", "__main__")])
    assert r.match(o), "redenerend uit de opgave is 1-hoog gelijk aan '# #' op één regel"

@t.passed(has_functions)
@t.test(20)
def exactMario3(test):
    """print een welgevormde pyramide van 3 hoog"""
    r = re.compile(".*"
      "(    # #)[ ]*(\n)"
      "(  # # #)[ ]*(\n)"
      "(# # # #)[ ]*"
      ".*", re.MULTILINE)
    o = lib.outputOf(_fileName, stdinArgs=[3], overwriteAttributes = [("__name__", "__main__")])
    assert r.match(o)

@t.passed(has_functions)
@t.test(30)
def exactMario23(test):
    """print een welgevormde pyramide van 23 hoog"""
    r = re.compile(".*"
      "(                                            # #)[ ]*(\n)"
      "(                                          # # #)[ ]*(\n)"
      "(                                        # # # #)[ ]*(\n)"
      "(                                      # # # # #)[ ]*(\n)"
      "(                                    # # # # # #)[ ]*(\n)"
      "(                                  # # # # # # #)[ ]*(\n)"
      "(                                # # # # # # # #)[ ]*(\n)"
      "(                              # # # # # # # # #)[ ]*(\n)"
      "(                            # # # # # # # # # #)[ ]*(\n)"
      "(                          # # # # # # # # # # #)[ ]*(\n)"
      "(                        # # # # # # # # # # # #)[ ]*(\n)"
      "(                      # # # # # # # # # # # # #)[ ]*(\n)"
      "(                    # # # # # # # # # # # # # #)[ ]*(\n)"
      "(                  # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(                # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(              # # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(            # # # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(          # # # # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(        # # # # # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(      # # # # # # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(    # # # # # # # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(  # # # # # # # # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(# # # # # # # # # # # # # # # # # # # # # # # #)[ ]*"
      ".*", re.MULTILINE)
    o = lib.outputOf(_fileName, stdinArgs=[23], overwriteAttributes = [("__name__", "__main__")])
    assert r.match(o)

@t.passed(has_functions)
@t.test(40)
def handlesWrongInput(test):
    """handelt verkeerde input netjes af"""
    r = re.compile(".*(# #)[ ]*(\n)")
    o = lib.outputOf(_fileName, stdinArgs=[-100, 100, 24, 1], overwriteAttributes = [("__name__", "__main__")])
    assert r.match(o)
