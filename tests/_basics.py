import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

import sys
import subprocess
import re

import os

@t.test(0)
def basic_style(test):
    """het bestand is in orde"""
    def testMethod():
        source = lib.source(test.fileName)
        if "	" in source:
            return False, "let op dat je geen tabs gebruikt"
        if re.search(r'(min|max)\s*\(', source):
            return False, "let op dat je geen min() of max() gebruikt"
        if re.search(r'sorted\s*\(', source):
            return False, "let op dat je geen sorted() gebruikt"
        try:
            max_line_length = os.environ['MAX_LINE_LENGTH']
        except KeyError:
            max_line_length = 99
        try:
            max_doc_length = os.environ['MAX_DOC_LENGTH']
        except KeyError:
            max_doc_length = 79
        p = subprocess.run(['pycodestyle', '--select=E101,E112,E113,E115,E116,E117,E501,W505', f"--max-line-length={max_line_length}", f"--max-doc-length={max_doc_length}", test.fileName], capture_output=True, universal_newlines=True)
        if p.returncode != 0:
            test.fail = lambda info : f"let op juiste indentatie, code >{max_line_length} tekens, comments >{max_doc_length} tekens"
            return False, p.stdout
        return True
    test.test = testMethod

@t.passed(basic_style, hide=False)
@t.test(1)
def mypy_ok(test):
    """type hints zijn ingevuld en consistent bevonden"""
    def testMethod():
        p = subprocess.run(['mypy', '--strict', '--ignore-missing-imports', test.fileName], capture_output=True, universal_newlines=True)
        return p.returncode == 0, p.stdout
    test.test = testMethod
    def report(output):
        return '- line ' + '\n- line '.join([':'.join(i.split(':')[1:])[:60] for i in output.splitlines()[:-1]])
    test.fail = report

@t.passed(mypy_ok, hide=False)
@t.test(2)
def doctest_ok(test):
    """doctests zijn voldoende aanwezig en geven allemaal akkoord"""
    def testMethod():
        with open(test.fileName, 'r') as source_file:
            source = source_file.read()
            functions = re.findall(r'def\s+(\w+)\(([^\)]*)\)[^-]+(->\s*([\w\[,\] _]+))?:', source)
            n_functions_not_returning = len([function for function in functions if ('file' in function[1] or function[3] == 'None' or function[3] == '')])
        p = subprocess.run([sys.executable or 'python3', '-m', 'doctest', '-v', test.fileName], capture_output=True, universal_newlines=True)
        if "Traceback" in p.stderr:
            return False, p.stderr.splitlines()[-1]
        test_stats_rex = re.compile('(\d*) tests in (\d*) items')
        test_pass_rex = re.compile('(\d*) passed and (\d*) failed')
        test_stats = test_stats_rex.search(p.stdout.splitlines()[-3])
        test_pass = test_pass_rex.search(p.stdout.splitlines()[-2])
        n_tests = int(test_stats.group(1))
        n_items = int(test_stats.group(2))-1-n_functions_not_returning
        n_pass  = int(test_pass.group(1))
        if n_items == 0:
            return False, "je programma moet functies gebruiken (of type hints ontbreken!)"
        elif n_tests // n_items < 2:
            return False, f"{n_tests} voorbeelden bij {n_items} functies is niet genoeg \n    (we tellen alleen functies die iets returnen)"
        elif n_pass < n_tests:
            return False, f"{n_pass} van {n_tests} voorbeelden slagen"
        return True

    test.test = testMethod
    test.fail = lambda info: info
    test.timeout = lambda: 120
