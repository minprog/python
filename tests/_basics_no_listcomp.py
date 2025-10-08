import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

from _pyprog_tools import *

import sys
import subprocess
import re
import os

def module_has_syntax_error():
    try:
        compile(static.getSource(), "<your program>", "exec")
    except SyntaxError as error:
        return error.lineno
    return False

def has_generators() -> bool:
    return static.getAstNodes(ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp)


@t.test(0)
def basic_style(test):
    """het bestand is in orde"""
    def testMethod():
        if lineno := module_has_syntax_error():
            return False, f"de code bevat een syntax error op regel {lineno}"
        if string_in_module("	"):
            return False, "let op dat je geen tabs gebruikt"
        if string_in_module("Optional"):
            return False, "let op dat je niet Optional[...] gebruikt als type hint maar ... | None"
        if string_in_module("List[", "Tuple[", "Dict[", "Sequence["):
            return False, "let op dat je niet List[...] gebruikt als type hint maar list[...]"
        # if call_in_module('min', 'max'):
        #     return False, "let op dat je geen min() of max() gebruikt"
        # if call_in_module('sorted'):
        #     return False, "let op dat je geen sorted() gebruikt"
        if call_in_module('map'):
            return False, "let op dat je geen map() gebruikt"
        if call_in_module('eval'):
            return False, "let op dat je geen eval() gebruikt"
        if call_in_module('zip'):
            return False, "let op dat je geen zip() gebruikt"
        if call_in_module('all', 'any'):
            return False, "let op dat je geen all() of any() gebruikt"
        # if import_in_module('math'):
        #     return False, "let op dat je geen import math gebruikt"
        if has_generators():
            return False, "let op dat je geen [... for ...] gebruikt"

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

from _mypy_strict import mypy_ok

from _check_doctests import require_doctests_for_returning_functions as doctest_ok
