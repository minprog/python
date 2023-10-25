import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

@t.passed(doctest_ok)
@t.test(10)
def checks_check_leap_year(test):
    """functie `is_leap_year` werkt correct"""
    def testMethod():
        fn = lib.getFunction("is_leap_year", test.fileName)
        if fn(2000) and fn(2020) and not fn(2100):
            return True
        else:
            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def checks_days_from_1800(test):
    """functie `days_from_1800` werkt correct"""
    def testMethod():
        fn = lib.getFunction("days_from_1800", test.fileName)
        if fn(5, 2022) == 81204 and fn(8, 1996) == 71800:
            return True
        else:
            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(30)
def checks_days_from_1800_till_year(test):
    """functie `days_from_1800_until_year` werkt correct"""
    def testMethod():
        fn = lib.getFunction("days_from_1800_until_year", test.fileName)
        if fn(2022) == 81084 and fn(1996) == 71587:
            return True
        else:
            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(40)
def checks_days_in_month(test):
    """functie `days_in_month` werkt correct"""
    def testMethod():
        fn = lib.getFunction("days_in_month", test.fileName)
        if fn(5, 2022) == 31 and fn(2, 2022) == 28 and fn(2, 2020) == 29:
            return True
        else:
            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(50)
def checks_days_until_month(test):
    """functie `days_until_month` werkt correct"""
    def testMethod():
        fn = lib.getFunction("days_until_month", test.fileName)
        if (
            fn(1, 1800) == 0
            and fn(5, 1804) == 121
            and fn(5, 1800) == 120
        ):
            return True
        else:
            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(60)
def checks_first_weekday_month(test):
    """functie `first_weekday_month` werkt correct"""
    def testMethod():
        fn = lib.getFunction("first_weekday_month", test.fileName)
        if fn(5, 2022) == 0 and fn(12, 2020) == 2:
            return True
        else:
            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(70)
def check_header(test):
    """print jaar en maand in de header"""
    def testMethod():
        output = lib.outputOf(
            test.fileName,
            stdinArgs=[1800, 1],
            overwriteAttributes=[("__name__", "__main__")],
        )
        if not asserts.contains(output.strip(), "Jan 1800"):
            return False
        output = lib.outputOf(
            test.fileName,
            stdinArgs=[2021, 11],
            overwriteAttributes=[("__name__", "__main__")],
        )
        if not asserts.contains(output.strip(), "Nov 2021"):
            return False

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(80)
def check_grid(test):
    """print het grid op de juiste manier"""
    def testMethod():
        output = lib.outputOf(
            test.fileName,
            stdinArgs=[1900, 2],
            overwriteAttributes=[("__name__", "__main__")],
        )

        if not (asserts.contains(output, "Sun Mon Tue Wed Thu Fri Sat\n") or
            asserts.contains(output, "Zon Maa Din Woe Don Vri Zat\n")):
            return False, "namen van dagen missen of zijn verkeerd gespeld"

        output = lib.outputOf(
            test.fileName,
            stdinArgs=[1800, 1],
            overwriteAttributes=[("__name__", "__main__")],
        )
        if not re.search(r"\ *1   2   3   4\ *\n", output):
            return False, "de eerste week van januari 1800 wordt verkeerd geprint"

        output = lib.outputOf(
            test.fileName,
            stdinArgs=[1800, 12],
            overwriteAttributes=[("__name__", "__main__")],
        )
        if not re.search(r"\ *28  29  30  31", output):
            return False, "de laatste week van december 1800 wordt verkeerd geprint"

        if not re.search(r"\ *28  29  30  31\ *\n", output):
            return False, "er staat geen newline aan het eind van de laatste regel"

        return True

    test.test = testMethod

@t.passed(check_grid, hide=False)
@t.test(90)
def checks_leap_years(test):
    """print een juiste kalender voor schrikkeljaren"""
    def testMethod():
        output = lib.outputOf(
            test.fileName,
            stdinArgs=[1900, 2],
            overwriteAttributes=[("__name__", "__main__")],
        )
        if re.search(r"\ *25  26  27  28  29\ *\n", output):
            return False, "het jaar 1900 moet geen schrikkeljaar zijn, maar is dat wel in dit programma"

        output = lib.outputOf(
            test.fileName,
            stdinArgs=[2000, 2],
            overwriteAttributes=[("__name__", "__main__")],
        )
        if not re.search(r"\ *27  28  29\ *\n", output):
            return False, "het jaar 2000 moet een schrikkeljaar zijn, maar is dat niet in dit programma"

        return True

    test.test = testMethod
