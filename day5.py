with open("inputs/day5.txt", "r") as f:
    INPUT = f.read()
RANGES = INPUT.split("\n\n")[0].splitlines()
IDS = INPUT.split("\n\n")[1].splitlines()

def partone():
    total = 0
    ids = IDS[:]
    for rang in RANGES:
        rangE = range(int(rang.split("-")[0]), int(rang.split("-")[1])+1)
        for id in ids[:]:
            if int(id) in rangE:
                total += 1
                ids.remove(id)
    print(total)

def parttwo():
    #print(len(set(x for rang in RANGES for x in range(int(rang.split("-")[0]), int(rang.split("-")[1]) + 1))))
    def merged(r, overlaps):
        if len(overlaps) == 0:
            return r
        min = r[0]
        max = r[-1]
        for existing in overlaps:
            x = existing[0]
            y = existing[-1]
            if x < min:
                min = x
            if y > max:
                max = y
        return range(min, max+1)
    

    def doesOverlap(r1, r2):
        x1 = r1[0]
        y1 = r1[-1]
        x2 = r2[0]
        if x2 < x1:
            return doesOverlap(r2, r1)
        return x2 <= y1+1
    
    ranges = RANGES[:]
    exRanges = []
    for rang in ranges:
        smaller, larger = rang.split("-")
        r = range(int(smaller), int(larger)+1)
        overlaps = [existing for existing in exRanges if doesOverlap(existing, r)]
        for o in overlaps: exRanges.remove(o)
        r2 = merged(r, overlaps)
        exRanges.append(r2)

    counter = 0
    for r in exRanges:
        x = r[0]
        y = r[-1]
        counter += y-x+1
    print(counter)

if __name__ == "__main__":
    partone()
    parttwo()