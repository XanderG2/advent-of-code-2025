# this program doesnt work, however im still proud of it as it was my first try at day 8 part 1

import math

with open("inputs/day8.txt", "r") as f:
    INPUT = f.readlines()

HOWMANYTOJOIN = 10 # example: 10, real thing: 1000

def euclideanDistance3D(p, q): # d(p, q) = sqrt((p1 - q1)^2 + (p2 - q2)^2 + (p3 - q3)^2) 
    p1, p2, p3 = p             # from https://en.wikipedia.org/wiki/Euclidean_distance#Higher_dimensions
    q1, q2, q3 = q
    d = math.sqrt((p1-q1)**2 + (p2-q2)**2 + (p3-q3)**2)
    return d

def orderSmallests(smallests):
    return sorted(smallests, key=lambda x: x[0])

def joinCircuits(circuits, toJoin1, toJoin2):
    dictionaryOfCoordinatesToWhatCircuitTheyAreIn = {coord: i for i, circuit in enumerate(circuits) for coord in circuit} # name is self-explanatory.
    inSameCircuit = dictionaryOfCoordinatesToWhatCircuitTheyAreIn[toJoin1] == dictionaryOfCoordinatesToWhatCircuitTheyAreIn[toJoin2]
    if inSameCircuit:
        joined = circuits
    else:
        joined = []
        circuit1 = dictionaryOfCoordinatesToWhatCircuitTheyAreIn[toJoin1]
        circuit2 = dictionaryOfCoordinatesToWhatCircuitTheyAreIn[toJoin2]
        realCircuit1 = circuits[circuit1]
        realCircuit2 = circuits[circuit2]
        combinedCircuit1And2 = realCircuit1+realCircuit2
        joined = circuits[:]
        del joined[circuit1]
        if circuit2 == len(joined) or circuits[circuit2] != joined[circuit2]:
            i = 1
        else:
            i = 0
        del joined[circuit2-i]
        joined.append(combinedCircuit1And2)
    return inSameCircuit, joined

def partone():
    smallests = []
    for x, y, z, i in [(int(a), int(b), int(c), i) for i, line in enumerate(INPUT) for a, b, c in [line.strip().split(",")]]: # trust
        #smallest = []
        for opposingX, opposingY, opposingZ, opposingI in [(int(a), int(b), int(c), j) for j, w in enumerate(INPUT) if j != i for a, b, c in [w.strip().split(",")]]: # god this was so confusing to write
            p = (opposingX, opposingY, opposingZ)
            q = (x, y, z)
            d = abs(euclideanDistance3D(p, q))
            #if len(smallest) == 0 or d < smallest[0]:
            smallests.append([d, p, q, i, opposingI])
        #smallests.append(smallest)
    ordered = orderSmallests(smallests)
    #ordered = [ordered[x] for x in range(len(ordered)) if x % 2 == 1] # note to self (so i can explain ts later): this cuts out every other one, 
    #print(ordered)                                                   # bc it calculates distance both ways and we only need 1
    circuits = [[(int(a), int(b), int(c))] for i, line in enumerate(INPUT) for a, b, c in [line.strip().split(",")]]
    #print(circuits)
    joinages = 0
    for x in ordered:
        inSameCircuit, circuits = joinCircuits(circuits, x[1], x[2])
        joinages += 1
        if joinages == HOWMANYTOJOIN:
            break
    threeLargestCircuits = sorted(circuits, key=len, reverse=True)[:3]
    print(math.prod([len(x) for x in threeLargestCircuits]))

if __name__ == "__main__":
    partone()