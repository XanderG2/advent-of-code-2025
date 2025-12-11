with open("inputs/day11.txt", "r") as f:
    INPUT = [x.strip() for x in f.readlines()]

def loop(current, smfo):
    if current == "out":
        return 1
    total = 0
    for v in smfo[current]:
        total += loop(v, smfo)
    return total

def partone():
    suckmyfatone = {device: outputs.split() for device, outputs in (line.split(": ") for line in INPUT)}
    print(loop("you", suckmyfatone))

if __name__ == "__main__":
    partone()