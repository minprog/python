import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

import subprocess

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
