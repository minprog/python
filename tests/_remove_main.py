from _static_analysis import *

@test(0)
def remove_main(test):
    """voorbewerking van het bestand voor testen"""

    global _originalFileName
    global _fileName

    _originalFileName = _fileName

    with open(_fileName, 'r') as f:
        file_contents = f.readlines()

    tempfile = f"_{_fileName}.tmp"

    with open(tempfile, 'w') as f:
        state = 0
        for line in file_contents:
            if state == 0:
                if line.startswith('def '):
                    state = 1
                f.write(line)
            elif state == 1:
                if not (line.strip() == '' or line.startswith(' ') or line.startswith("\t") or line.startswith("def ") or line.startswith("#")):
                    state = 2
                    continue
                f.write(line)
            elif state == 2:
                if line.startswith('def '):
                    f.write(line)
                    state = 1

    _fileName = tempfile
