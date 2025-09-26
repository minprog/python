from _pyprog_tools import *

import checkpy

@test(0)
def remove_main(test):
    """voorbewerking van het bestand voor testen"""
    # lees file via checkpy API, voeg weer \n toe na splitten
    file_contents = [f"{x}\n" for x in checkpy.static.getSource().split("\n")]

    # wat het echt doet is het verwijderen van alle code die niet
    # in een functie staat, maar wel pas vanaf de eerste functie
    # (zodat dingen als imports en globals wel bewaard blijven mits
    # ze boven de bovenste functie staan)
    with open(checkpy.file.name, 'w') as f:
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

    # debug code
    # with open(checkpy.file.name, 'r') as f:
    #     print(f.read())
