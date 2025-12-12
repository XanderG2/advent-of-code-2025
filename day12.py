with open("inputs/day12.txt", "r") as f:
    INPUT = f.readlines()

def partone():
    for line in range(len(INPUT)):
        lin = INPUT[line]
        if "#" in lin and INPUT[line+1].strip() == "" and "#" not in INPUT[line+3]:
            lineofSplit = line+2
            break
    regions = [x.strip() for x in INPUT[lineofSplit:]]
    sizes = [x for z in regions for x in z.split(":")[0].split("x")]
    realsizes = [(int(sizes[x]), int(sizes[x+1])) for x in range(0, len(sizes), 2)]
    squares = [sum([int(x) for x in z.split(":")[1].split()]) for z in regions]
    total = 0
    for size, square in zip(realsizes, squares):
        print(size, square)
        x = size[0]
        y = size[1]
        if x < 3 or y < 3:
            continue
        canfit = (x // 3) * (y // 3)
        if canfit >= square:
            total += 1
    print(total)
        

if __name__ == "__main__":
    partone()