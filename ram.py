from collections import namedtuple


class RAMMachine:

    def __init__(self, ram, *args):
        self._ram = ram
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

    def _fill(self, r):

        lenght = len(self._ram)
        max_index = lenght - 1

        if r > max_index:
            to_add = r+1 - lenght

            for _ in range(to_add):
                self._ram.append(0)

    def dec(self, r, *args):

        self._fill(r)

        num = self._ram[r]

        if num > 0:
            num -= 1
            self.pc += 2
        else:
            self.pc += 1

        self._ram[r] = num

    def inc(self, r, *args):
        self._fill(r)
        self._ram[r] += 1
        self.pc += 1

    def goto(self, r, *args):
        self.pc = r

    def halt(self, *args):
        self.pc = -1
        return self._ram[0]

    def clear(self, r, *args):
        self._fill(r)
        self._ram[r] = 0
        self.pc += 1

    def move(self, r, s, *args):
        self._fill(r)
        self._fill(s)

        toS = self._ram[r]

        self._ram[r] = 0
        self._ram[s] = toS

        self.pc += 1

    def copy(self, r, s, *args):
        self._fill(r)
        self._fill(s)

        toS = self._ram[r]
        self._ram[s] = toS

        self.pc += 1

    def add(self, r, s, t, *args):

        self._fill(r)
        self._fill(s)
        self._fill(t)

        self._ram[s] += self._ram[r]
        self._ram[t] += self._ram[r]
        self._ram[r] = 0
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
    log = []
    RamProgram = RAMMachine(CurrentProgram.memory)
    n = 0
    while RamProgram.pc < len(CurrentProgram.code) and RamProgram.pc != -1:
        n += 1
        func, args = CurrentProgram.code[RamProgram.pc]
        # print(func, args)
        previous_ram = RamProgram._ram.copy()
        RamProgram.valid_functions[func](*args)
        current_ram = RamProgram._ram

        if n == 100_000:
            RamProgram.pc = -1

        log.append(f'{func.upper()}{args}\n{previous_ram} -> {current_ram}\n')
    output = RamProgram.halt()
    log.insert(0, f'CANTIDAD DE PASOS: {n}\n')
    write_log(log)
    return output


def write_log(log):
    with open('logs.txt', 'w') as f:
        for entry in log:
            print(entry, file=f)


def get_log():
    with open('logs.txt') as f:
        return f.read()


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
