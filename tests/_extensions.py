import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

import sys
import subprocess
import re

@t.test(1000)
def mypy_ok(test):
    def testMethod():
        p = subprocess.run(['mypy', '--strict', '--ignore-missing-imports', test.fileName], capture_output=True, universal_newlines=True)
        return p.returncode == 0, p.stdout

    def report(output):
        return 'line ' + '\n  - line '.join([':'.join(i.split(':')[1:]) for i in output.splitlines()[:-1]])

    test.description = lambda: "types are specified and correctly used"
    test.test = testMethod
    test.fail = report

@t.test(1001)
def doctest_ok(test):
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
            return False, "Your program must use functions"
        elif n_tests // n_items < 2:
            return False, f"{n_tests} examples in {n_items} functions is not quite enough \n    (we only count functions that return something)"
        elif n_pass < n_tests:
            return False, f"{n_pass} out of {n_tests} examples passed"
        return True

    test.description = lambda: "doctests are specified and all examples pass"
    test.test = testMethod
    test.fail = lambda info: info
