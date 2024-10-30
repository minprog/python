import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

from _static_analysis import *

import sys
import subprocess
import re
import os

def pl(n: int, desc: str):
    meervouden = {
        'voorbeeld': 'voorbeelden',
        'functie': 'functies',
        'slaagt': 'slagen'
    }
    if n == 1:
        return desc
    else:
        return meervouden[desc]

# @t.passed(mypy_ok, hide=False)
@t.test(2)
def require_doctests_for_all_functions(test):
    """elke functie heeft voldoende doctests en ze geven allemaal akkoord"""
    def testMethod():
        # retrieve functions from source
        with open(test.fileName, 'r') as source_file:
            source = source_file.read()
            functions = re.findall(r'def\s+(\w+)\(([^\)]*)\)[^-]+(->\s*([\w\[,\] _]+))?:', source)
            n_functions = len(functions)

        # bail out if no functions at all
        if n_functions == 0:
            return False, "je programma moet functies gebruiken (of type hints ontbreken!)"

        # run doctest and extract results
        p = subprocess.run([sys.executable or 'python3', '-m', 'doctest', '-v', test.fileName], capture_output=True, universal_newlines=True)
        if "Traceback" in p.stderr:
            return False, p.stderr.splitlines()[-1]
        test_stats_rex = re.compile('(\d*) tests in (\d*) items')
        test_pass_rex = re.compile('(\d*) passed and (\d*) failed')
        test_stats = test_stats_rex.search(p.stdout.splitlines()[-3])
        test_pass = test_pass_rex.search(p.stdout.splitlines()[-2])

        # number of doctests found anywhere
        n_tests = int(test_stats.group(1))
        # number of classes/functions (-1 is for module)
        n_items = int(test_stats.group(2))-1
        # test ratio
        if n_items > 0:
            n_tested_per_function = n_tests // n_items
        else:
            n_tested_per_function = 0
        # number of doctests succeeded in total
        n_pass  = int(test_pass.group(1))

        if n_tested_per_function < 2:
            return False, f"{n_tests} {pl(n_tests, 'voorbeeld')} bij {n_tested} {pl(n_tested, 'functie')} is niet genoeg"
        elif n_pass < n_tests:
            return False, f"{n_pass} van {n_tests} {pl(n_tests, 'voorbeeld')} {pl(n_pass, 'slaagt')}"
        return True

    test.test = testMethod
    test.fail = lambda info: info
    test.timeout = lambda: 120

# @t.passed(mypy_ok, hide=False)
@t.test(2)
def require_doctests_for_returning_functions(test):
    """doctests zijn voldoende aanwezig en geven allemaal akkoord"""
    def testMethod():
        with open(test.fileName, 'r') as source_file:
            source = source_file.read()
            functions = re.findall(r'def\s+(\w+)\(([^\)]*)\)[^-]+(->\s*([\w\[,\] _]+))?:', source)
            n_functions_not_returning = len([function for function in functions if ('file' in function[1] or function[3] == 'None' or function[3] == '')])
            n_functions = len(functions)
        p = subprocess.run([sys.executable or 'python3', '-m', 'doctest', '-v', test.fileName], capture_output=True, universal_newlines=True)
        if "Traceback" in p.stderr:
            return False, p.stderr.splitlines()[-1]
        test_stats_rex = re.compile('(\d*) tests in (\d*) items')
        test_pass_rex = re.compile('(\d*) passed and (\d*) failed')
        test_stats = test_stats_rex.search(p.stdout.splitlines()[-3])
        test_pass = test_pass_rex.search(p.stdout.splitlines()[-2])
        n_tests = int(test_stats.group(1))
        n_items = int(test_stats.group(2))-1
        n_tested = n_items-n_functions_not_returning
        n_pass  = int(test_pass.group(1))
        if n_functions == 0:
            return False, "je programma moet functies gebruiken (of type hints ontbreken!)"
        elif n_tested == 0:
            # geen testbare functies blijkbaar?
            return True
        elif n_tested > 0 and n_tests // n_tested < 2:
            return False, f"{n_tests} voorbeelden bij {n_tested} testbare functies is niet genoeg \n    (we tellen alleen functies die iets returnen)"
        elif n_pass < n_tests:
            return False, f"{n_pass} van {n_tests} voorbeelden slagen"
        return True

    test.test = testMethod
    test.fail = lambda info: info
    test.timeout = lambda: 120
