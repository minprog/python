import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

import hashlib

from checkpy import *
from _typecheck import *

download("climate.txt", "https://raw.githubusercontent.com/minprog/pyprog/2022/opdrachten/week5/eca2csv/climate.txt")

@t.test(1)
def output_test(test):
    def testMethod():
        output = lib.outputOf(test.fileName, overwriteAttributes = [("__name__", "__main__")]).strip()
        with open('climate-noheader.txt') as cnh:
            hash = hashlib.md5(cnh.read().strip().encode('utf-8')).hexdigest()
            if hash != 'a9c7b2346db2f89eedb77e8915f583c5':
                return False, f"'climate-noheader.txt' does not contain exactly what is expected"
        with open('climate-noheader-no2020.txt') as cnh:
            hash = hashlib.md5(cnh.read().strip().encode('utf-8')).hexdigest()
            if hash != '87defdce3b585d4fe3d59be8a07d61e1':
                return False, f"'climate-noheader-no2020.txt' does not contain exactly what is expected"
        with open('climate-cleaned.txt') as cnh:
            content = cnh.read().strip()
            if not '19010225' in content:
                return False, "'climate-cleaned.txt' appears to be missing data for 19010225"
            hash = hashlib.md5(content.encode('utf-8')).hexdigest()
            if hash != 'aa7138f0b4e8eb25a5982afe21ef79f0':
                return False, f"'climate-cleaned.txt' does not contain exactly what is expected"
        with open('climate.csv') as cnh:
            hash = hashlib.md5(cnh.read().strip().encode('utf-8')).hexdigest()
            if hash != '1ed8ae701fd107d64a35f1e0e8abfefd':
                return False, f"'climate.csv' does not contain exactly what is expected"
        return True
    test.test = testMethod
    test.description = lambda : "generates files with exactly the right contents"
