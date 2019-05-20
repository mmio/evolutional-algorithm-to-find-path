# TODO: Optimize based on prints no cycles
from random import randrange

from Chromosome import Chromosome
from VirtualMachine import VM
from Tester import Tester

import GenerationStrategy
import SelectionStrategy
import CrossoverStrategy
import MutationStrategy

import sys
import time

def getKey(custom):
    return custom.fit

class Evolver:
    def __init__(self, n=20, chromLen=64,
                 generationStrategy=None,
                 selectionStragegy=None,
                 crossoverStrategy=None,
                 mutationStrategy=None
    ):
        
        self.numOfChrom = n
        self.chromLen = chromLen
        self.mutationChance = 7 # for now
        self.population = []

        # self.mapa = mapa
        self.t = Tester()
        self.heur = self.t.treasureCount
        self.area = self.t.x + self.t.y
        
        self.generator = GenerationStrategy.Heuristic
        self.selection = SelectionStrategy.DoubleTrournamentSelection
        self.cross = CrossoverStrategy.Take2Random
        self.mutation = MutationStrategy.RandomResetting

        self.generate()

    def generate(self):
        self.population = self.generator(self)

    def select(self):
        return self.selection(self)
    
    def crossover(self):
        return self.cross(self)

    def mutate(self, chrome):
        return self.mutation(self, chrome)

    def evolve(self, generations):
        pEl = 0.1
        pCr = 0.7
        vm = VM()
        dots = "."
        for i in range(generations):
            # create n-threads of vms
            for j in range(len(self.population)):
                vm = VM()
                vm.load(self.population[j].program)
                vm.run()
                self.population[j].fit = vm.testProg()
                if vm.t.foundAll():
                    print('\n------------------')
                    print("Posledná najlepšia fitnes:", self.population[j].fit)
                    print("cesta:", end=' ')
                    vm.t.printValid(self.population[j].program)
                    print("Počet generácií", i)
                    return
                # vm.reset()
            # Barrier here 

            srtd = sorted(self.population, key=getKey, reverse=True)
            p10 = round(len(self.population)*pEl)
            best = srtd[0:p10]


            sys.stdout.write("\rgen:{}\t\tmax:{}".format(i, srtd[0].fit))
            sys.stdout.flush()

            newPopulation = []

            while len(newPopulation) <= round(self.numOfChrom*pCr):
                ch = self.crossover()
                newPopulation.append(ch)

            while len(newPopulation) <= round(self.numOfChrom * (1 - pEl)):
                tmpCh = Chromosome(bytearray(self.chromLen))
                for k in range(self.chromLen):
                    tmpCh.program[k] = randrange(256)
                newPopulation.append(tmpCh)

            # newPopulation = removeDuplicates(newPopulation)
                
            counter = 0
            for k in range(self.chromLen):
                if (tmpCh.program[k] >= 0b11000000):
                    counter += 1
                    if (counter == self.heur):
                        newPopulation.append(tmpCh)

            self.population = newPopulation
        
            for k in range(len(self.population)):
                self.population[k] = self.mutate(self.population[k])

            for k in best:
                self.population.append(k)

# def removeDuplicates(population):
#     checked = []
#     newPopulation = []
#     for i in population:
#         if i.program not in checked:
#             checked.append(i.program)
#             newPopulation.append(i)
#     return newPopulation
