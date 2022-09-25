import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

@t.test(1)
def writers(test):
    def checkOutput():
        output = lib.outputOf(test.fileName, stdinArgs=["There are no good writers."], overwriteAttributes = [("__name__", "__main__")])
        return (lib.getLine(output, 0) == "5 words" and
                lib.getLine(output, 1) == "1 capitalized word" and
                lib.getLine(output, 2) == "1 punctuation mark")
    test.test = checkOutput
    test.description = lambda : "Correctly handles example 1"

@t.test(2)
def obiwan(test):
    def checkOutput():
        output = lib.outputOf(test.fileName, stdinArgs=["Obi-Wan Kenobi took their job quite seriously."], overwriteAttributes = [("__name__", "__main__")])
        return (lib.getLine(output, 0) == "7 words" and
                lib.getLine(output, 1) == "2 capitalized words" and
                lib.getLine(output, 2) == "2 punctuation marks")
    test.test = checkOutput
    test.description = lambda : "Correctly handles example 2"

@t.test(3)
def sunday(test):
    def checkOutput():
        output = lib.outputOf(test.fileName, stdinArgs=["The life on Sunday began without a speck of agitation."], overwriteAttributes = [("__name__", "__main__")])
        return (lib.getLine(output, 0) == "10 words" and
                lib.getLine(output, 1) == "2 capitalized words" and
                lib.getLine(output, 2) == "1 punctuation mark")
    test.test = checkOutput
    test.description = lambda : "Correctly handles example 3"

@t.test(4)
def sidney(test):
    def checkOutput():
        output = lib.outputOf(test.fileName, stdinArgs=["It's difficult when you're carrying other people's dreams"], overwriteAttributes = [("__name__", "__main__")])
        return (lib.getLine(output, 0) == "8 words" and
                lib.getLine(output, 1) == "1 capitalized word" and
                lib.getLine(output, 2) == "3 punctuation marks")
    test.test = checkOutput
    test.description = lambda : "Correctly handles example 4"
