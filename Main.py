from Evolver import Evolver

import GenerationStrategy
import SelectionStrategy
import MutationStrategy
import CrossoverStrategy

def main():
    chromN = int(input("Počet Chromosómov:\n"))
    
    e = Evolver(chromN)
    e.t.printMap()
    
    gen = int(input("Generovanie:\n1.Náhodne\n2.Heuristikou\n"))
    if (gen == 1):
        e.generationStrategy = GenerationStrategy.Random
    elif (gen == 2):
        e.generationStrategy = GenerationStrategy.Heuristic
    else:
        print("Zlé argumenty")

    gen = int(input("Selekcia:\n1.Turnament\n2.Ruleta\n3.Rank\n"))
    if (gen == 1):
        e.selectionStragegy = SelectionStrategy.DoubleTrournamentSelection
    elif (gen == 2):
        e.selectionStragegy = SelectionStrategy.RouletSelection
    elif (gen == 3):
        e.selectionStrategy = SelectionStrategy.RankSelection
    else:
        print("Zlé argumenty")

    gen = int(input("Kríženie:\n1.Dvoch náhodne\n2.Pól na pól\n3.Polovica bajtu\n"))
    if (gen == 1):
        e.crossoverStrategy = CrossoverStrategy.Take2Random
    elif (gen == 2):
        e.crossoverStrategy = CrossoverStrategy.HalfHalf
    elif (gen == 3):
        e.crossoverStrategy = CrossoverStrategy.HalfByte
    else:
        print("Zlé argumenty")

    gen = int(input("Mutácia:\n1.Náhodné resetovania\n2.Prepni bit\n3.Náhodne vymeň\n"))
    if (gen == 1):
        e.mutationStrategy = MutationStrategy.RandomResetting
    elif (gen == 2):
        e.mutationStrategy = MutationStrategy.BitFlip
    elif (gen == 3):
        e.mutationStrategy = MutationStrategy.SwapMutation
    else:
        print("Zlé argumenty")
    
    e.evolve(5000)

if __name__ == '__main__':
    main()
