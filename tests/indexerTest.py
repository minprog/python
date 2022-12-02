import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

def sandbox():
    lib.require("stopwords.txt", "https://raw.githubusercontent.com/minprog/pyprog/2022/opdrachten/week6/indexer/dist/indexer/stopwords.txt")
    lib.require("test.txt", "https://raw.githubusercontent.com/minprog/pyprog/2022/opdrachten/week6/indexer/dist/indexer/texts/birdman.txt")

@t.test(1)
def checks_type(test):
    def testMethod():
        fn = lib.getFunction("create_index", test.fileName)
        index = fn("stopwords.txt", [])
        if len(index) != 138:
            return False, "the index does not have the correct amount of words"

        for key, value in index.items():

            if not isinstance(key, str):
                return False, "the keys in the index are not strings"

            if not isinstance(value, list):
                return False, "the values in the index are not lists"

            try:
                if not isinstance(value[0], int):
                    return False, "the values in the index are not lists that contain integers"
            except:
                return (
                    False,
                    "some of the values in the index have emtpy lists",
                )

        return True

    test.test = testMethod
    test.description = lambda: "'create_index' returns a well-formed index with correctly loaded data"


@t.test(2)
def checks_tekst1(test):
    def testMethod():
        output = lib.outputOf(
            test.fileName,
            argv=["indexer.py", "test.txt"],
            stdinArgs=["dinner", ""],
            overwriteAttributes=[("__name__", "__main__")],
        )
        return re.search(r".*dinner.*\ 549, 1542", output)

    test.test = testMethod
    test.description = (
        lambda: "finds the word 'dinner' on lines 549 and 1542 in birdman.txt"
    )


@t.test(3)
def checks_crash(test):
    def testMethod():
        output = lib.outputOf(
            test.fileName,
            argv=["indexer.py", "test.txt"],
            stdinArgs=["women", "dinner", ""],
            overwriteAttributes=[("__name__", "__main__")],
        )
        return re.search(r".*dinner.*\ 549, 1542", output)

    test.test = testMethod
    test.description = lambda: "allows for another search if a word is not found"
