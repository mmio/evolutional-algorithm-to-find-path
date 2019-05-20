from random import randrange

def TournamentSelection(e):
    k = 6
    best1 = None
    for i in range(k):
        curr = e.population[randrange(len(e.population))]
        if best1 == None or curr.fit > best1.fit:
            best1 = curr
        return best1

def DoubleTrournamentSelection(e):
    k = 6
    best1 = None
    for i in range(k):
        curr = e.population[randrange(len(e.population))]
        if best1 == None or curr.fit > best1.fit:
            best1 = curr

        best2 = None
        for i in range(k):
            curr = e.population[randrange(len(e.population))]
            if best2 == None or curr.fit > best2.fit:
                best2 = curr

        if (best1.fit > best2.fit):
            return best1
        else:
            return best2
    
def RouletSelection(e):
    total_weight = 0
    for i in e.population:
        total_weight += i.fit

    target_weight = randrange(round(total_weight))
    for i in e.population:
        target_weight -= i.fit
        if (target_weight <= 0):
            return i

def RankSelection(e):
    sortedPopulation = sorted(e.population, key=lambda x: x.fit)

    r = 1
    total = 0
    for i in sortedPopulation:
        i.rank = (r)
        total += (r)
        r += 1

    target_rank = randrange(total)
    for i in sortedPopulation:
        target_rank -= i.rank
        if (target_rank <= 0):
            return i
