from collections import namedtuple


class RAM:

    valid_functions = {}

    def __init__(self, ram):
        self.__ram = ram
        self.pc = 0

    def dec(self, r):
        num = self.__ram[r]

        if num > 0:
            num -= 1
            self.pc += 2
        else:
            self.pc += 1

        self.__ram[r] = num

    def inc(self, r):
        self.__ram[r] += 1
        self.pc += 1

    def goto(self, r):
        self.pc = r

    def halt(self):
        print(self.__ram[0])

    def clear(self, r):
        self.__ram[r] = 0
        self.pc += 1

    def move(self, r, s):
        toS = self.__ram[r]

        self.__ram[r] = 0
        self.__ram[s] = toS

        self.pc += 1

    def copy(self, r, s):
        toS = self.__ram[r]
        self.__ram[s] = toS

        self.pc += 1


def input_to_program(input, mem):

    Program = namedtuple('Program', ['code', 'memory'])

    input = input.strip().split('\n')
    # print(input)
    input = [entry.strip() for entry in input if entry != '']

    Program.code = input

    mem = mem.strip().split(',')
    mem = [int(pos.strip()) for pos in mem if pos != '' and pos.isnumeric()]

    Program.memory = mem

    return Program


def run_program(Program):

    return Program
