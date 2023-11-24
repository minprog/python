from _static_analysis import *

@test(0)
def remove_main(test):
    """voorbewerking van het bestand voor testen"""

    with open(test.fileName, 'r') as f:
        file_contents = f.readlines()

    with open(test.fileName, 'w') as f:
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
