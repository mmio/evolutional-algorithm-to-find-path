from Tester import Tester

class VM:
    def __init__(self):
        self.prog = bytearray()
        self.progPtr = 0x000000;
        self.ops = {
            0b00: self.add_op,
            0b01: self.sub_op,
            0b10: self.jmp_op,
            0b11: self.prt_op
        }
        # self.mapa = mapa
        self.moves = ""
        self.t = Tester()
        self.numOfCycles = 0
        self.printCount = 0

    def reset(self):
        self.prog = bytearray()
        self.progPtr = 0x000000;
        self.ops = {
            0b00: self.add_op,
            0b01: self.sub_op,
            0b10: self.jmp_op,
            0b11: self.prt_op
        }
        self.moves = ""
        self.t = Tester()
        self.numOfCycles = 0
        
    def add_op(self):
        cell = self.prog[self.progPtr]
        data = (cell & 0b00111111)

        if self.prog[data] + 1 <= 255:
            self.prog[data] += 1
        else:
            self.prog[data] = 0

    def sub_op(self):
        cell = self.prog[self.progPtr]
        data = (cell & 0b00111111)

        if self.prog[data] - 1 >= 0:
            self.prog[data] -= 1
        else:
            self.prog[data] = 255

    def jmp_op(self):
        self.progPtr = (self.prog[self.progPtr] & 0b00111111) - 1

    def prt_op(self):
        cell = self.prog[self.progPtr]
        adr = (cell & 0b00111111)
        count = bin(self.prog[adr]).count('1')
        self.printCount += 1

        if count <= 2:
            self.moves += 'H'
        elif count <= 4:
            self.moves += 'D'
        elif count <= 6:
            self.moves += 'P'
        elif count <= 8:
            self.moves += 'L'
        
    def load(self, barr):
        self.prog = barr[:]

    def run(self):
        cykly = 0

        while cykly != 500:     # 1.st condition
            cell = self.prog[self.progPtr]
            inst = (cell & 0b11000000) >> 6
            
            self.ops[inst]()
            cykly += 1
            self.numOfCycles += 1
            # print(inst, self.progPtr)

            if (self.progPtr + 1 < len(self.prog)):
                self.progPtr += 1
            else:               # 2.nd condition
                break
                
    def printMoves(self):
        for i in self.moves:
            print(i)

    def testProg(self):
        return self.t.load(self.moves)  - self.numOfCycles

    # def reset(self):
    #     pass
