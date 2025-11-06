from checkpy import *
from _pyprog_tools import *
import re

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def checks_no_index(test):
    """oplossing gebruikt geen `.index()` of `.find()`"""
    if string_in_module(".index") or string_in_module(".find") or call_in_module("ord"):
        raise AssertionError("gebruik geen .index() of .find() of ord() voor deze opdracht")

@passed(checks_no_index)
def checks_compute_score(test):
    """functie 'compute_score' werkt correct"""
    compute_score = get_function("compute_score")
    assert compute_score("word") == 8
    assert compute_score("WORD") == 8
    assert compute_score("Test") == 4
    assert compute_score("abcdefghijklmnopqrstuvwxyz") == 87

@passed(checks_no_index)
def check_S1(test):
    """speler 1 met 'Pizza' wint van speler 2 met 'Kaas'"""
    output = run("Pizza", "Kaas")
    assert output.strip().is_one_of(["Speler 1 wint!", "Player 1 wins!"])

@passed(checks_no_index)
def check_S2(test):
    """speler 1 met 'Hotel' verliest van speler 2 met 'Kamperen'"""
    output = run("Hotel", "Kamperen")
    assert output.strip().is_one_of(["Speler 2 wint!", "Player 2 wins!"])

@passed(checks_no_index)
def check_gelijkspel(test):
    """speler 1 met 'Vrijdag' speelt gelijk met speler 2 met 'Zaterdag'"""
    output = run("Vrijdag", "Zaterdag")
    assert output.strip().is_one_of(["Gelijkspel!", "It's a tie!"])

@passed(checks_no_index)
def check_gelijkspel2(test):
    """speler 1 met 'Hardly?' speelt gelijk met speler 2 met 'Hardly!'"""
    output = run("Hardly?", "Hardly!")
    assert output.strip().is_one_of(["Gelijkspel!", "It's a tie!"])
