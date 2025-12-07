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

        



if __name__ == "__main__":
    partone()
