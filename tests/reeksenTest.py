from checkpy import *
from _pyprog_tools import *

from checkpy.lib import  io

from _python_checks import checkstyle, forbidden_constructs, mypy_strict#, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict)#, doctest_all)
def has_functions():
    """functies `reeks1` t/m `reeks8` zijn aanwezig"""
    for n in range(1, 9):
        assert function_defined_in_module(f"reeks{n}")

@passed(has_functions)
def test_reeks1(test):
    """functie `reeks1` werkt correct"""
    func = get_function("reeks1")
    res = "0 2 4 6 8 10 12 14 16 18"
    res = res.replace(" ", "\n") + "\n"
    with io.captureStdout() as stdout:
        func()
        assert RunResult(stdout.content) == res

@passed(has_functions)
def test_reeks2(test):
    """functie `reeks2` werkt correct"""
    func = get_function("reeks2")
    res = "1 3 5 7 9 11 13 15 17 19 21 23"
    res = res.replace(" ", "\n") + "\n"
    with io.captureStdout() as stdout:
        func()
        assert RunResult(stdout.content) == res

@passed(has_functions)
def test_reeks3(test):
    """functie `reeks3` werkt correct"""
    func = get_function("reeks3")
    res = "1 2 5 10 17 26 37 50 65 82 101 122 145 170 197"
    res = res.replace(" ", "\n") + "\n"
    with io.captureStdout() as stdout:
        func()
        assert RunResult(stdout.content) == res

@passed(has_functions)
def test_reeks4(test):
    """functie `reeks4` werkt correct"""
    func = get_function("reeks4")
    res = "5 4 3 2 1 0 -1 -2 -3"
    res = res.replace(" ", "\n") + "\n"
    with io.captureStdout() as stdout:
        func()
        assert RunResult(stdout.content) == res

@passed(has_functions)
def test_reeks5(test):
    """functie `reeks5` werkt correct"""
    func = get_function("reeks5")
    res = "1 3 9 27 81 243 729"
    res = res.replace(" ", "\n") + "\n"
    with io.captureStdout() as stdout:
        func()
        assert RunResult(stdout.content) == res

@passed(has_functions)
def test_reeks6(test):
    """functie `reeks6` werkt correct"""
    func = get_function("reeks6")
    res = "1000 100 10 1 0 0 0 0 0 0"
    res = res.replace(" ", "\n") + "\n"
    with io.captureStdout() as stdout:
        func()
        assert RunResult(stdout.content) == res

@passed(has_functions)
def test_reeks7(test):
    """functie `reeks7` werkt correct"""
    func = get_function("reeks7")
    res = "1 2 * 4 5 * 7 8 * 10"
    res = res.replace(" ", "\n") + "\n"
    with io.captureStdout() as stdout:
        func()
        assert RunResult(stdout.content) == res

@passed(has_functions)
def test_reeks8(test):
    """functie `reeks8` werkt correct"""
    func = get_function("reeks8")
    res = "1 2 # 8 16 # 64 128 # 512"
    res = res.replace(" ", "\n") + "\n"
    with io.captureStdout() as stdout:
        func()
        assert RunResult(stdout.content) == res
