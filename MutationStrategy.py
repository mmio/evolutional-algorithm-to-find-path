# TODO: add - addOne()

from random import randrange

def RandomResetting(e, ch):
    for i in range(e.chromLen):
        if e.mutationChance*1000 >= randrange(100000):
            ch.program[i] = randrange(256)
    return ch

def BitFlip(e, ch):
    for i in range(e.chromLen):
        if e.mutationChance >= randrange(100):
            ch.program[i] ^= (1 << randrange(7))
    return ch

def SwapMutation(e, ch):
    for i in range(e.chromLen):
        if e.mutationChance >= randrange(100):
            rnd1, rnd2 = randrange(8), randrange(8)
            tmp = ch.program[rnd1]
            ch.program[rnd1] = ch.program[rnd2]
            ch.program[rnd2] = tmp
    return ch
