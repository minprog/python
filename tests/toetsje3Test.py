import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(1000)
def mypy_ok(test):
    def testMethod():
        p = subprocess.run(['mypy', '--strict', test.fileName], stdout=subprocess.PIPE, universal_newlines=True)
        return p.returncode == 0, p.stdout

    def report(output):
        return 'Line ' + '\n  - Line '.join([':'.join(i.split(':')[1:]) for i in output.splitlines()[:-1]])

    test.description = lambda: "Types are specified and correctly used."
    test.test = testMethod
    test.fail = report

@t.test(1001)
def doctest_ok(test):
    def testMethod():
        p = subprocess.run([sys.executable or 'python3', '-m', 'doctest', '-v', test.fileName], stdout=subprocess.PIPE, universal_newlines=True)
        test_stats_rex = re.compile('(\d*) tests in (\d*) items')
        test_pass_rex = re.compile('(\d*) passed and (\d*) failed')
        test_stats = test_stats_rex.search(p.stdout)
        test_pass = test_pass_rex.search(p.stdout)
        n_tests = int(test_stats.group(1))
        n_items = int(test_stats.group(2))-1
        n_pass  = int(test_pass.group(1))
        if n_tests // n_items < 2:
            return False, f"{n_tests} examples in {n_items} functions is not quite enough"
        elif n_pass < n_tests:
            return False, f"{n_pass} out of {n_tests} examples failed"
        return True

    test.description = lambda: "Doctests are specified and all examples pass."
    test.test = testMethod
    test.fail = lambda info: info
