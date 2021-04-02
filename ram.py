from collections import namedtuple


class RAMMachine:

    def __init__(self, ram, *args):
        self.__ram = ram
        self.pc = 0

        self.valid_functions = {'dec': self.dec,
                                'inc': self.inc,
                                'goto': self.goto,
                                'halt': self.halt,
                                'clear': self.clear,
                                'move': self.move,
                                'copy': self.copy,
                                'add': self.add,
                                }

    def dec(self, r, *args):
        num = self.__ram[r]

        if num > 0:
            num -= 1
            self.pc += 2
        else:
            self.pc += 1

        self.__ram[r] = num

    def inc(self, r, *args):
        self.__ram[r] += 1
        self.pc += 1

    def goto(self, r, *args):
        self.pc = r

    def halt(self, *args):
        self.pc = -1
        return self.__ram[0]

    def clear(self, r, *args):
        self.__ram[r] = 0
        self.pc += 1

    def move(self, r, s, *args):
        toS = self.__ram[r]

        self.__ram[r] = 0
        self.__ram[s] = toS

        self.pc += 1

    def copy(self, r, s, *args):
        toS = self.__ram[r]
        self.__ram[s] = toS

        self.pc += 1

    def add(self, r, s, t, *args):
        self.__ram[s] += self.__ram[r]
        self.__ram[t] += self.__ram[r]
        self.__ram[r] = 0
        self.pc += 1


Program = namedtuple('Program', ['code', 'memory'])
Function = namedtuple('Function', ['name', 'arg'])


def input_to_program(to_code, mem):

    to_code = to_code.split('\n')
    to_code = [line for line in to_code if line != '']
    code = []
    for entry in to_code:
        entry = entry.replace(')', '')
        entry = entry.replace(' ', '')
        entry = entry.split('(')
        if len(entry) == 2:
            entry[1] = entry[1].split(',')
            entry[1] = [int(number)
                        for number in entry[1] if number.isnumeric()]
            code.append(entry)

    mem = mem.replace(' ', '')
    mem = mem.split(',')
    mem = [int(pos) for pos in mem]

    CurrentProgram = Program(code, mem)

    return CurrentProgram


def run_program(CurrentProgram):

    RamProgram = RAMMachine(CurrentProgram.memory)
    while RamProgram.pc < len(CurrentProgram.code) and RamProgram.pc != -1:
        func, args = CurrentProgram.code[RamProgram.pc]
        # print(func, args)
        RamProgram.valid_functions[func](*args)
    output = RamProgram.halt()
    return output


if __name__ == '__main__':

    program = input_to_program(
        """
dec(1)
goto(8)
dec(2)
goto(5)
goto(0)
inc(1)
copy(1,0)
halt()
clear(0)
goto(7)
""",
        '0, 4, 6'
    )

    print(run_program(program))
