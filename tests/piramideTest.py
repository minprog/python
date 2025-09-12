from checkpy import *
from _static_analysis import *

# TODO modernize
import checkpy.lib as lib
import checkpy.assertlib as assertlib

import re

from _python_checks import forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(forbidden_constructs, mypy_strict, doctest_all)
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

@passed(has_functions)
@test(10)
def exactMario0(test):
    """print een welgevormde pyramide van 1 hoog"""
    assert_output(run(1), "(# ?#)[ ]*(\n)", "##\n")

@passed(has_functions)
@test(20)
def exactMario3(test):
    """print een welgevormde pyramide van 3 hoog"""
    r = re.compile(
      ".*"
      "(  ?  ?# ?#)[ ]*(\n)"
      "(  ?# ?# ?#)[ ]*(\n)"
      "(# ?# ?# ?#)[ ]*"
      ".*", re.MULTILINE)
    assert_output(run(3), r, "  ##\n ###\n####\n")

@passed(has_functions)
@test(30)
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
    o = run(23)
    if not r.match(o):
        raise AssertionError(
            "gegeven input: 23 ⏎\n"
            "de piramide is niet wat we verwacht hadden (fix eerst de kleinere)")

@passed(has_functions)
@test(40)
def handlesWrongInput(test):
    """handelt verkeerde input netjes af"""
    assert_output(run(-100, 100, 24, 1), ".*(# ?#)[ ]*(\n)", "##\n")
