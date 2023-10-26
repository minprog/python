import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from checkpy import *

from _basics import *

include("indexer.py")
download("stopwords.txt", "https://raw.githubusercontent.com/minprog/pyprog/2022/opdrachten/week6/indexer/dist/indexer/stopwords.txt")
download("test.txt", "https://raw.githubusercontent.com/minprog/pyprog/2022/opdrachten/week6/indexer/dist/indexer/texts/birdman.txt")

@t.passed(doctest_ok)
@t.test(10)
def checks_type(test):
    """functie 'create_index' geeft een index van het juiste type met ingeladen data"""
    def testMethod():
        fn = lib.getFunction("create_index", test.fileName)
        index = fn("stopwords.txt", [])
        if len(index) != 138:
            return False, "de index heeft niet het juiste aantal woorden"

        for key, value in index.items():

            if not isinstance(key, str):
                return False, "de keys in de index zijn geen strings"

            if not isinstance(value, list):
                return False, "de values in de index zijn geen lists"

            try:
                if not isinstance(value[0], int):
                    return False, "de values in de index zijn geen lists met daarin integers"
            except:
                return False, "sommige values bevatten lege lijsten"

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def checks_tekst1(test):
    """vindt het woord 'dinner' op regels 549 en 1542 in birdman.txt"""
    def testMethod():
        output = lib.outputOf(
            test.fileName,
            argv=["indexer.py", "test.txt"],
            stdinArgs=["dinner", ""],
            overwriteAttributes=[("__name__", "__main__")],
        )
        return re.search(r".*dinner.*\ 549, 1542", output) is not None
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(30)
def checks_crash(test):
    """er mag nog eens gezocht worden als een woord niet gevonden wordt"""
    def testMethod():
        output = lib.outputOf(
            test.fileName,
            argv=["indexer.py", "test.txt"],
            stdinArgs=["women", "dinner", ""],
            overwriteAttributes=[("__name__", "__main__")],
        )
        return re.search(r".*dinner.*\ 549, 1542", output) is not None
    test.test = testMethod
