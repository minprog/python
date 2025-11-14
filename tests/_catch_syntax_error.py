from checkpy import *

from _forbidden_constructs import module_has_syntax_error

@test()
def no_syntax_error(test):
    """het bestand is in orde"""
    def augment(define_location: int, lines: list[str]) -> tuple[int, int]:
        # start with the line that was provided
        start = define_location

        # try to go up from that line until empty line or indented line
        while True:
            start -= 1
            if lines[start].strip() == "":
                start += 1
                break
            elif lines[start].startswith("  ") or lines[start].startswith("\t"):
                break
            elif start <= 0:
                break

        # again, start with the line that was provided
        end = define_location

        # try to go down from that line
        waiting = False
        while True:
            end += 1
            if end > len(lines) - 1:
                # EOF reached
                if waiting != False:
                    # end = waiting
                    end = len(lines) - 1
                else:
                    end = len(lines) - 1
                break
            elif lines[end].strip() == "":
                # blank line found
                if waiting == False:
                    waiting = end-1
                continue
            elif (lines[end].startswith("  ") or
                  lines[start].startswith("\t") or
                  lines[start-1].endswith("\\")):
                # indented code line found, belongs to this function
                waiting = False
                continue
            else:
                # non-indented code probably means end of this function
                if waiting:
                    end = waiting
                else:
                    end -= 1
                break

        return start, end

    class MappedProgram():
        def __init__(self):
            self.program_map: list[tuple[int, int]] = []
            self.syntax_errors: list[int] = []

            with open(test.fileName, 'r') as f:
                self.lines: list[str] = f.readlines()
                self.size: int = len(self.lines)

            if self.size > 0:
                defs = []
                # find all function defs
                for i in range(self.size):
                    if self.lines[i].startswith('def '):
                        defs.append(i)

                # make list of all start-end line pairs of functions
                augmented = [augment(define, self.lines) for define in defs]
                self.program_map = augmented

        def write_program(self):
            with open(test.fileName, 'w') as f:

                # iterate over all the line numbers from the original file
                for no in range(self.size):
                    printed=False

                    # walk all the syntax errors we know of
                    for err_line in self.syntax_errors:
                        # a syntax error might fall into a function and we may be
                        # at a line in that exact function
                        if len(list(filter(lambda i: i[0] <= no <= i[1] and i[0] <= err_line <= i[1], self.program_map))) > 0:
                            # write that function, commented out
                            f.write(f"# {self.lines[no]}")
                            printed=True
                            break

                    # unless the line was already printed with a comment, we print it as-is
                    if printed==False:
                        f.write(f"{self.lines[no]}")

        def remove_syntax_errors(self):
            while lineno := module_has_syntax_error():
                # correction
                lineno -= 1

                # stop if we apparently already tried to remove this error but it did not succeed
                if lineno in self.syntax_errors:
                    return

                # stop if we already have 4 funcs with syntax errors commented out
                if len(self.syntax_errors) == 4:
                    return

                self.syntax_errors.append(lineno)
                self.write_program()
                # if len(self.syntax_errors)==1:
                    # break

    def testMethod():
        p = MappedProgram()
        # print(p.program_map)
        p.remove_syntax_errors()

        if _ := module_has_syntax_error():
            return False, f"er is minstens één syntax error die niet verwijderd kon worden"
        if len(p.syntax_errors) > 0:
            test.description = f"deel van code verwijderd ivm syntax errors op regel {', '.join([str(e+1) for e in p.syntax_errors])}"
        return True
    test.test = testMethod
