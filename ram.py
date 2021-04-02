class RAM:
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
