import checkpy.tests as t

import subprocess

@t.test()
def mypy_ok(test):
    """type hints zijn ingevuld en consistent bevonden"""
    def testMethod():
        p = subprocess.run(['mypy', '--strict', '--ignore-missing-imports', '--disable-error-code=name-defined', test.fileName], capture_output=True, universal_newlines=True)
        return p.returncode == 0, p.stdout
    test.test = testMethod
    def report(output):
        return '- line ' + '\n- line '.join([':'.join(i.split(':')[1:])[:60] for i in output.splitlines()[:-1]])
    test.fail = report
