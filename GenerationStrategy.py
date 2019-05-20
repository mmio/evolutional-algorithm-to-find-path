from random import randrange
from Chromosome import Chromosome


def Random(e):
    for i in range(e.numOfChrom):
        tmpCh = Chromosome(bytearray(e.chromLen))
        for j in range(e.chromLen):
            tmpCh.program[j] = randrange(256)
        e.population.append(tmpCh)
    return e.population


def Heuristic(e):
    noft = e.heur
    while len(e.population) < e.numOfChrom:
        tmpCh = Chromosome(bytearray(e.chromLen))
        for j in range(e.chromLen):
            tmpCh.program[j] = randrange(256)

        counter = 0
        for j in range(e.chromLen):
            if (tmpCh.program[j] >= 0b11000000):
                counter += 1
                if (counter >= noft and counter <= e.area):
                    e.population.append(tmpCh)
    return e.population
