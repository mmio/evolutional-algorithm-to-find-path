from random import randrange
from Chromosome import Chromosome


def HalfHalf(e):
        p1 = e.select()
        p2 = e.select()

        ch1 = Chromosome(bytearray(e.chromLen))

        ch1.program[0:round(e.chromLen/2)] = p1.program[0:round(e.chromLen/2)];
        ch1.program[round(e.chromLen/2):] = p1.program[round(e.chromLen/2):];
        return ch1

def HalfByte(e):
        p1 = e.select()
        p2 = e.select()

        ch = Chromosome(bytearray(e.chromLen))

        for i in range(e.chromLen):
            ch.program[i] = ((p1.program[i] & 0b11110000)
                              | (p2.program[i] & 0b00001111))
        return ch

def Take2Random(e):
        p1 = e.select()
        p2 = e.select()

        ch = Chromosome(bytearray(e.chromLen))
        for i in range(e.chromLen):
            rnd = randrange(2)
            if rnd == 1:
                ch.program[i] = p1.program[i]
            else:
                ch.program[i] = p2.program[i]
        return ch
