import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

from _static_analysis import *

import sys
import subprocess
import re
import os

@t.test(1)
def basic_style(test):
    """het bestand is in orde"""
    def testMethod():
        if lineno := has_syntax_error():
            return False, f"de code bevat een syntax error op regel {lineno}"
        if has_string("	"):
            return False, "let op dat je geen tabs gebruikt"
        if has_string("Optional"):
            return False, "let op dat je niet Optional[...] gebruikt als type hint maar ... | None"
        if has_string("List[", "Tuple[", "Dict[", "Set["):
            return False, "let op dat je niet List[...] e.d. gebruikt als type hint maar list[...]"
        # if has_call('min', 'max'):
        #     return False, "let op dat je geen min() of max() gebruikt"
        if has_call('sorted'):
            return False, "let op dat je geen sorted() gebruikt"
        if has_call('map'):
            return False, "let op dat je geen map() gebruikt"
        if has_call('eval'):
            return False, "let op dat je geen eval() gebruikt"
        if has_import('math'):
            return False, "let op dat je geen import math gebruikt"

        # run pycodestyle for a couple of basic checks
        try:
            max_line_length = os.environ['MAX_LINE_LENGTH']
        except KeyError:
            max_line_length = 99
        try:
            max_doc_length = os.environ['MAX_DOC_LENGTH']
        except KeyError:
            max_doc_length = 79
        p = subprocess.run([
                'pycodestyle',
                '--select=E101,E112,E113,E115,E116,E117,E501,E502,W505,W291',
                f"--max-line-length={max_line_length}",
                f"--max-doc-length={max_doc_length}",
                test.fileName
            ], capture_output=True, universal_newlines=True)
        if p.returncode != 0:
            if "E1" in p.stdout:
                test.fail = lambda info : f"let op juiste indentatie"
                return False, p.stdout
            if "E501" in p.stdout or "W505" in p.stdout:
                test.fail = lambda info : f"regel(s) te lang, code max {max_line_length} tekens, comments max {max_doc_length} tekens"
                return False, p.stdout
            if "E502" in p.stdout:
                test.fail = lambda info: f"gebruik tussen haakjes geen \\ om de regel af te breken"
                return False, p.stdout
            if "W291" in p.stdout:
                pattern = r'[^:\n]+:(\d+):\d+: W291'
                matches = re.findall(pattern, p.stdout)
                test.fail = lambda info: f"zorg dat er geen spaties aan het eind van een regel staan (regel {', '.join(matches)})"
                return False, p.stdout
        return True
    test.test = testMethod

@t.passed(basic_style, hide=False)
@t.test(2)
def mypy_ok(test):
    """type hints zijn ingevuld en consistent bevonden"""
    def testMethod():
        p = subprocess.run(['mypy', '--strict', '--ignore-missing-imports', '--disable-error-code=name-defined', test.fileName], capture_output=True, universal_newlines=True)
        return p.returncode == 0, p.stdout
    test.test = testMethod
    def report(output):
        return '- line ' + '\n- line '.join([':'.join(i.split(':')[1:])[:60] for i in output.splitlines()[:-1]])
    test.fail = report

@t.passed(mypy_ok, hide=False)
@t.test(3)
def doctest_ok(test):
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
