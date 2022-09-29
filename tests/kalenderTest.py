import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *


@t.test(0)
def checks_check_leap_year(test):
    def testMethod():
        fn = lib.getFunction("is_leap_year", test.fileName)
        if fn(2000) and fn(2020) and not fn(2100):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda: "'is_leap_year' works correctly."


@t.test(1)
def checks_days_from_1800(test):
    def testMethod():
        fn = lib.getFunction("days_from_1800", test.fileName)
        if fn(5, 2022) == 81204 and fn(8, 1996) == 71800:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda: "'days_from_1800' works correctly."


@t.test(2)
def checks_days_from_1800_till_year(test):
    def testMethod():
        fn = lib.getFunction("days_from_1800_until_year", test.fileName)
        if fn(2022) == 81084 and fn(1996) == 71587:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda: "'days_from_1800_until_year' works correctly."


@t.test(3)
def checks_days_in_month(test):
    def testMethod():
        fn = lib.getFunction("days_in_month", test.fileName)
        if fn(5, 2022) == 31 and fn(2, 2022) == 28 and fn(2, 2020) == 29:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda: "'days_in_month' works correctly."


@t.test(4)
def checks_days_until_month(test):
    def testMethod():
        fn = lib.getFunction("days_until_month", test.fileName)
        if (
            fn(1, 1800, True) == 0
            and fn(5, 1804, True) == 121
            and fn(5, 1800, False) == 120
        ):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda: "'days_until_month' works correctly."


@t.test(5)
def checks_first_weekday_month(test):
    def testMethod():
        fn = lib.getFunction("first_weekday_month", test.fileName)
        if fn(5, 2022) == 0 and fn(12, 2020) == 2:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda: "'first_weekday_month' works correctly."


@t.test(6)
def checks_first_weekday_month(test):
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
    test.description = lambda: "The correct year and month are printed in the table."


@t.test(7)
def checks_table(test):
    def testMethod():
        output = lib.outputOf(
            test.fileName,
            stdinArgs=[1900, 2],
            overwriteAttributes=[("__name__", "__main__")],
        )
        if not (asserts.contains(output, "Sun Mon Tue Wed Thu Fri Sat\n") or
            asserts.contains(output, "Zon Maa Din Woe Don Vri Zat\n")):
            return False, "The days of the month are missing."

        output = lib.outputOf(
            test.fileName,
            stdinArgs=[1800, 1],
            overwriteAttributes=[("__name__", "__main__")],
        )
        if not re.search(r"\ *1   2   3   4\ *\n", output):
            return False, "The first week of 1800 is printed incorrectly."

        output = lib.outputOf(
            test.fileName,
            stdinArgs=[1800, 12],
            overwriteAttributes=[("__name__", "__main__")],
        )
        if not re.search(r"\ *28  29  30  31\ *\n", output):
            return False, "The last week of 1800 is printed incorrectly."

        return True

    test.test = testMethod
    test.description = lambda: "The program correctly prints a month calendar."


@t.test(8)
def checks_leap_years(test):
    def testMethod():
        output = lib.outputOf(
            test.fileName,
            stdinArgs=[1900, 2],
            overwriteAttributes=[("__name__", "__main__")],
        )
        if re.search(r"\ *25  26  27  28  29\ *\n", output):
            return False, "The year 1900 should not a leap year, but is in your program."

        output = lib.outputOf(
            test.fileName,
            stdinArgs=[2000, 2],
            overwriteAttributes=[("__name__", "__main__")],
        )
        if not re.search(r"\ *27  28  29\ *\n", output):
            return False, "The year 2000 should be a leap year, but is in your program."

        return True

    test.test = testMethod
    test.description = lambda: "The program correctly accounts for leap years."
