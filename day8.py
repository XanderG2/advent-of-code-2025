import math
with open("inputs/day8.txt", "r") as f:
    INPUT = [x.strip() for x in f.readlines()]

TOMAKE = 1000

def euclideanDistance3D(p, q): # d(p, q) = sqrt((p1 - q1)^2 + (p2 - q2)^2 + (p3 - q3)^2) 
    p1, p2, p3 = p             # from https://en.wikipedia.org/wiki/Euclidean_distance#Higher_dimensions
    q1, q2, q3 = q
    d = math.sqrt((p1-q1)**2 + (p2-q2)**2 + (p3-q3)**2)
    return d

def containingCircuit(a, circuits):
    for circuit in circuits:
        if a in circuit:
            return circuit
    else:
        exit("should never gapped")

def connected(a, b, circuits):
    return containingCircuit(a, circuits) == containingCircuit(b, circuits)

def join(a, b, circuits):
    circuitsNew: list = circuits[:]
    circuitA = containingCircuit(a, circuits)
    circuitB = containingCircuit(b, circuits)
    if circuitA == circuitB:
        exit("should bever happen")
    newCircuit = set(list(circuitA)+list(circuitB))
    circuitsNew.remove(circuitA)
    circuitsNew.remove(circuitB)
    circuitsNew.append(newCircuit)
    return circuitsNew

def partone():
    coords = [tuple([int(x) for x in line.split(",")]) for line in INPUT]
    distanceByCoords = {}
    for a in (coords):
        for b in (coords):
            if a == b:
                continue
            if (b, a) not in distanceByCoords.keys():
                distanceByCoords[(a, b)] = euclideanDistance3D(a, b)
    distanceAndCoords = ((key, value) for key, value in distanceByCoords.items())
    ordered = sorted(distanceAndCoords, key=lambda x: x[1])
    distanceByCoords: dict = {key: value for key, value in ordered}
    circuits = [{c} for c in coords]
    i = 0
    for a, b in distanceByCoords.keys():
        if not connected(a, b, circuits):
            circuits = join(a, b, circuits)
        i += 1
        if i == TOMAKE:
            break
    print(math.prod(sorted([len(x) for x in circuits], reverse=True)[:3]))

def parttwo():
    coords = [tuple([int(x) for x in line.split(",")]) for line in INPUT]
    distanceByCoords = {}
    for a in (coords):
        for b in (coords):
            if a == b:
                continue
            if (b, a) not in distanceByCoords.keys():
                distanceByCoords[(a, b)] = euclideanDistance3D(a, b)
    distanceAndCoords = ((key, value) for key, value in distanceByCoords.items())
    ordered = sorted(distanceAndCoords, key=lambda x: x[1])
    distanceByCoords: dict = {key: value for key, value in ordered}
    circuits = [{c} for c in coords]
    for a, b in distanceByCoords.keys():
        if not connected(a, b, circuits):
            circuits = join(a, b, circuits)
            if len(circuits) == 1:
                print(a[0] * b[0])
                break
        

if __name__ == "__main__":
    partone()
    parttwo()