from checkpy import *
from _pyprog_tools import *

import re

from _python_checks import forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert construct_in_ast(ast.While)
    assert construct_in_ast(ast.For)
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert construct_not_in_ast(ast.Try)
    assert no_string_mult_used()

@passed(has_functions)
@test(10)
def exactMario0(test):
    """print een welgevormde pyramide van 1 hoog"""
    assert run(1) == "##\n"

@passed(has_functions)
@test(20)
def exactMario3(test):
    """print een welgevormde pyramide van 3 hoog"""
    assert run(3) == "  ##\n ###\n####\n"

@passed(has_functions)
@test(30)
def exactMario23(test):
    """print een welgevormde pyramide van 23 hoog"""
    e = (""
      "                      ##\n"
      "                     ###\n"
      "                    ####\n"
      "                   #####\n"
      "                  ######\n"
      "                 #######\n"
      "                ########\n"
      "               #########\n"
      "              ##########\n"
      "             ###########\n"
      "            ############\n"
      "           #############\n"
      "          ##############\n"
      "         ###############\n"
      "        ################\n"
      "       #################\n"
      "      ##################\n"
      "     ###################\n"
      "    ####################\n"
      "   #####################\n"
      "  ######################\n"
      " #######################\n"
      "############## ##########\n")
    o = run(23)
    # trucje met f-string om er een normale string van te maken
    # in plaats van een string met een overloaded ==
    if not e == f"{o}":
        raise AssertionError(
            "gegeven input: 23 ⏎\n"
            "de piramide is niet wat we verwacht hadden (fix eerst de kleinere)")

@passed(has_functions)
@test(40)
def handlesWrongInput(test):
    """handelt verkeerde input netjes af"""
    assert run(-100, 100, 24, 1).match(".*(##)[ ]*(\n)", "##\n")
